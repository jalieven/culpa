import logging
import json
import urllib2
import base64

import time

from BeautifulSoup import BeautifulSoup as soup


class BambooAgent:

    def __init__(self, config, redis_repo):
        logging.info("Init BambooAgent!")
        self.config = config
        self.redis_repo = redis_repo
        self.redis_connection = self.redis_repo.redis_connection
        self.bamboo_state_key = "state"
        self.bamboo_reason_key = "buildReason"
        self.bamboo_failed_tests_key = "failedTestCount"
        self.bamboo_success_tests_key = "successfulTestCount"
        self.bamboo_failed_value = "Failed"
        self.bamboo_success_value = "Successful"
        self.redis_state_key = "state"
        self.redis_user_key = "user"
        self.redis_failed_tests_key = "testsFailed"
        self.redis_success_tests_key = "testsSuccess"

    def fetchBuildInfo(self, build):
        bamboo = self.config['bamboo']['apiUrl'] + build['key'] + "/latest.json"
        request = urllib2.Request(bamboo)
        base64string = base64.encodestring('%s:%s' % (self.config['bamboo']['username'],
                                                      self.config['bamboo']['password'])).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        bamboo_response = urllib2.urlopen(request)
        jdata = json.load(bamboo_response)
        return jdata

    def get(self, build_key):
        return self.redis_connection.hgetall(build_key)

    def saveOrUpdateBuild(self, build_key, build):
        for key, value in build.iteritems():
            self.redis_connection.hset(build_key, key, value)

    def checkBamboo(self):
        logging.info("BambooAgent is checking the state of the builds!")
        # call the Bamboo to check latest build results
        for build in self.config['bamboo']['builds']:
            self.saveOrUpdateBuild(build['key'], build)
            # retrieve the json result of the latest build
            jdata = self.fetchBuildInfo(build)
            # parse the json into variables
            build_state = jdata[self.bamboo_state_key]
            build_user = soup(jdata[self.bamboo_reason_key]).find("a")["href"].rsplit('/', 1)[1]
            build_failed_tests = jdata[self.bamboo_failed_tests_key]
            build_success_tests = jdata[self.bamboo_success_tests_key]
            # setting the state in redis and make the bunny talk if the state latched
            if self.redis_connection.hget(build['key'], self.redis_state_key) != build_state:
                self.redis_connection.hset(build['key'], self.redis_state_key, build_state)
                self.redis_connection.hset(build['key'], self.redis_user_key, build_user)
                self.redis_connection.hset(build['key'], self.redis_failed_tests_key, build_failed_tests)
                self.redis_connection.hset(build['key'], self.redis_success_tests_key, build_success_tests)
                build_speech = "Build+" + build['speak'] + "+" + build_state + "!" + "Brought+to+you+by:" + build_user + "!"
                test_speech = ""
                if build_state == self.bamboo_failed_value and build_failed_tests == 0:
                    test_speech = "Most+likely+a+compilation+error!+Shame+on+you!"
                elif build_state == self.bamboo_failed_value:
                    test_speech = str(build_failed_tests) + "+tests+failed!"
                bunny_speech = build_speech + test_speech
                print(bunny_speech)
                time.sleep(8)
            else:
                # if the build state didn't change but was still failed check the failed tests
                if build_state == self.bamboo_failed_value:
                    redis_failed_tests = self.redis_connection.hget(build['key'], self.redis_failed_tests_key)
                    build_speech = "Status quo for build " + build['speak']
                    if int(redis_failed_tests) > int(build_failed_tests):
                        improved_tests = abs(int(redis_failed_tests) - int(build_failed_tests))
                        build_speech = "Build+" + build['speak'] + "+still+failed!"
                        test_speech = "But:+test+success+improved+by+" \
                                      + str(improved_tests) + "!" + "Brought+to+you+by:" + build_user + "!"
                        bunny_speech = build_speech + test_speech
                        self.redis_connection.hset(build['key'], self.redis_failed_tests_key, build_failed_tests)
                        self.redis_connection.hset(build['key'], self.redis_success_tests_key, build_success_tests)
                        print(bunny_speech)
                        time.sleep(8)
                    elif int(redis_failed_tests) < int(build_failed_tests):
                        declined_tests = abs(int(redis_failed_tests) - int(build_failed_tests))
                        build_speech = "Build+" + build['speak'] + "+still+failed!"
                        test_speech = "But:+test+success+declined+by+" \
                                      + str(declined_tests) + "!" + "Brought+to+you+by:" + build_user + "!"
                        bunny_speech = build_speech + test_speech
                        self.redis_connection.hset(build['key'], self.redis_failed_tests_key, build_failed_tests)
                        self.redis_connection.hset(build['key'], self.redis_success_tests_key, build_success_tests)
                        print(bunny_speech)
                        time.sleep(8)
                    else:
                        # remove this line when integrated into the bunny
                        print(build_speech)
                elif build_state == self.bamboo_success_value:
                    redis_success_tests = self.redis_connection.hget(build['key'], self.redis_success_tests_key)
                    if int(redis_success_tests) < int(build_success_tests):
                        more_tests = abs(int(redis_success_tests) - int(build_success_tests))
                        build_speech = "Build+" + build['speak'] + "+improved!"
                        test_speech = "Hooray!+" + str(more_tests) + "+more+tests!" + "Brought+to+you+by:" + build_user + "!"
                        self.redis_connection.hset(build['key'], self.redis_failed_tests_key, build_failed_tests)
                        self.redis_connection.hset(build['key'], self.redis_success_tests_key, build_success_tests)
                        bunny_speech = build_speech + test_speech
                        print(bunny_speech)
                        time.sleep(8)
                    elif int(redis_success_tests) > int(build_success_tests):
                        less_tests = abs(int(redis_success_tests) - int(build_success_tests))
                        build_speech = "Build+" + build['speak'] + "+declined!"
                        test_speech = str(less_tests) + "+tests+were+removed!" + "Brought+to+you+by:" + build_user + "!"
                        self.redis_connection.hset(build['key'], self.redis_failed_tests_key, build_failed_tests)
                        self.redis_connection.hset(build['key'], self.redis_success_tests_key, build_success_tests)
                        bunny_speech = build_speech + test_speech
                        print(bunny_speech)
                        time.sleep(8)
                    else:
                        # remove this line when integrated into the bunny
                        print("Status quo for build " + build['speak'])
        logging.info("BambooAgent is done checking the state of the builds!")








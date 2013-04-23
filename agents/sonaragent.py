import logging
import json

from domain.event import SonarEvent
from failure.failures import FetchException
from util.apifetcher import ApiFetcher


class SonarAgent:
    def __init__(self, config, redis_repo):
        logging.info("Init component SonarAgent")
        self.config = config
        self.redis_repo = redis_repo

    def checkSonar(self):
        logging.info("SonarAgent is checking the state of the projects!")
        # call the Bamboo to check latest build results
        for project in self.config['projects']:
            logging.debug(project)
            self.updateMetricInfo(project)
        logging.info("SonarAgent is done checking the state of the builds!")

    def updateMetricInfo(self, project):
        if project['checkCoverage']:
            resource_param = "?resource={0}".format(project['key'])
            metrics_param = "&metrics=coverage"
            blocker_violations_param = "&depth=-1&priorities=BLOCKER"
            critical_violations_param = "&depth=-1&priorities=CRITICAL"
            sonar_metrics = "{0}{1}{2}".format(self.config['metricsApiUrl'], resource_param, metrics_param)
            sonar_violations = "{0}{1}{2}".format(self.config['violationsApiUrl'], resource_param, metrics_param)
            try:
                sonar_response = ApiFetcher.fetch(sonar_metrics, self.config['username'], self.config['password'])
                jdata = json.load(sonar_response)
                logging.debug("Fetched coverage from sonar: ", jdata)
            except FetchException, f:
                logging.error("Exception while updating metric info of project {0} -> {1}".format(project['key'], f))

                # if project['checkViolations']:
                #     resource_param = "?resource=", project['key']
                #     metrics_param = "&metrics=violations"
                #     sonar_metrics = self.config['metricsApiUrl'] + resource_param + metrics_param
                #     sonar_response = ApiFetcher.fetch(sonar_metrics, self.config['username'], self.config['password'])
                #     jdata = json.load(sonar_response)
                #     logging.debug("Fetched violations from sonar: " + jdata)

    def createSonarEvent(self, message, judgement, instigator, project_key, coverage, violations):
        sonar_event = SonarEvent(message, judgement, instigator, project_key, coverage, violations)
        self.redis_repo.saveEvent(sonar_event)

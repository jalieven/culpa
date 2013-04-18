import logging
import json

from domain.event import SonarEvent
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
            resource_param = "?resource=", project['key']
            metrics_param = "&metrics=coverage"
            sonar_metrics = self.config['metricsApiUrl'] + resource_param + metrics_param
            sonar_response = ApiFetcher.fetch(sonar_metrics, self.config['username'], self.config['password'])
            jdata = json.load(sonar_response)
            logging.debug("Fetched coverage from sonar: " + jdata)

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

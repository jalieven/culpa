import logging

from apscheduler.scheduler import Scheduler


class CulpaScheduler:
    def __init__(self, config, bamboo_agent, sonar_agent):
        logging.info("Init component CulpaScheduler")
        self.config = config
        self.bamboo_agent = bamboo_agent
        self.sonar_agent = sonar_agent
        self.sched = Scheduler()
        self.sched.start()
        if bamboo_agent is not None:
            self.sched.add_cron_job(self.runBambooCheck, minute=self.config['bamboo']['cronMinutes'])
        if sonar_agent is not None:
            self.sched.add_cron_job(self.runSonarCheck, minute=self.config['sonar']['cronMinutes'])

    def runBambooCheck(self):
        logging.info("Running scheduled bamboo check!")
        self.bamboo_agent.checkBamboo()

    def runSonarCheck(self):
        logging.info("Running scheduled sonar check!")
        self.sonar_agent.checkSonar()


import logging
from agents.bambooagent import BambooAgent
from agents.sonaragent import SonarAgent
from repo.redisrepo import RedisRepo
from util.scheduler import CulpaScheduler
from web.api import WebApi


class CulpaComponents:
    def __init__(self, config=None):
        logging.info("Assembling Culpa components")
        self.config = config
        # instantiate the different components with their respective config-dict parts
        self.redis_repo = RedisRepo(self.config['redis'])
        if self.config['agents']['bamboo'] is not None and self.config['agents']['bamboo']['enabled']:
            self.bamboo_agent = BambooAgent(self.config['agents']['bamboo'], self.redis_repo)
        else:
            self.bamboo_agent = None
        if self.config['agents']['sonar'] is not None and self.config['agents']['sonar']['enabled']:
            self.sonar_agent = SonarAgent(self.config['agents']['sonar'], self.redis_repo)
        else:
            self.sonar_agent = None
        self.karotz_scheduler = CulpaScheduler(self.config['scheduler'], self.bamboo_agent, self.sonar_agent)
        self.web_api = WebApi(self.config['api'])
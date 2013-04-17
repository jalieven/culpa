#!/usr/bin/python
import logging
import json

from repo.redisrepo import RedisRepo
from agents.bambooagent import BambooAgent
from agents.sonaragent import SonarAgent
from util.scheduler import KarotzScheduler
from web.api import WebApi


logging.basicConfig(filename='agents.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(thread)d:%(message)s')

config = json.load(open('config.json'))

# instantiate the different components with their respective config-dict parts
redis_repo = RedisRepo(config['redis'])

if config['agents']['bamboo'] is not None:
    bamboo_agent = BambooAgent(config['agents']['bamboo'], redis_repo)
else:
    bamboo_agent = None

if config['agents']['sonar'] is not None:
    sonar_agent = SonarAgent(config['agents']['sonar'], redis_repo)
else:
    sonar_agent = None

karotz_scheduler = KarotzScheduler(config['scheduler'], bamboo_agent, sonar_agent)

web_api = WebApi(config['api'])

#!/usr/bin/python
import logging
import json
from components.components import CulpaComponents

logging.basicConfig(filename='culpa.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(thread)d:%(message)s')
logging.info(" _______  __   __  ___      _______  _______")
logging.info("|       ||  | |  ||   |    |       ||   _   |")
logging.info("|       ||  | |  ||   |    |    _  ||  |_|  |")
logging.info("|       ||  |_|  ||   |    |   |_| ||       |")
logging.info("|      _||       ||   |    |    ___||       |")
logging.info("|     |  |  o o  ||   |___ |   |    |       |")
logging.info("|     |_ |   T   ||       ||   |    |   _   |")
logging.info("|_______||_______||_______||___|    |__| |__|")
logging.info("")
logging.info("Lets blame some devs...")

config = json.load(open('config.json'))

culpa = CulpaComponents(config)

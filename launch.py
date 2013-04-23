import logging
import json
from components.components import CulpaComponents

config = json.load(open('culpa-config.json'))

logging.basicConfig(filename=config['logging']['filename'], level=config['logging']['logLevel'],
                    format=config['logging']['format'])

logging.info(" _______  __   __  ___      _______  _______ ")
logging.info("|       ||  | |  ||   |    |       ||       |")
logging.info("|       ||  | |  ||   |    |    _  ||   _   |")
logging.info("|       ||  |_|  ||   |    |   |_| ||  | |  |")
logging.info("|      _||       ||   |    |    ___||  |_|  |")
logging.info("|     |  |  o o  ||   |___ |   |    |       |")
logging.info("|     |_ |   T   ||       ||   |    |   _   |")
logging.info("|_______||_______||_______||___|    |__| |__|")
logging.info("")
logging.info("Lets blame some devs...")

culpa = CulpaComponents(config)

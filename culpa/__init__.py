import logging
import json

from pyramid.config import Configurator
from components.components import CulpaComponents

log = logging.getLogger(__name__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    culpa(settings['culpa.config.file'])
    log.info("Init Culpa Pyramid app")
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    log.info("End init Culpa Pyramid app")
    return config.make_wsgi_app()


def culpa(culpa_config_location):
    config = json.load(open(culpa_config_location))

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

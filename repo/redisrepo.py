import logging
import redis
from domain.event import Event


class RedisRepo:

    EVENTS_HASH_KEY_PREFIX = "EVENTS:"

    def __init__(self, config):
        logging.info("Init RedisRepo")
        self.config = config
        self.pool = redis.ConnectionPool(host=self.config['host'],
                                         port=self.config['port'],
                                         max_connections=self.config['maxConnections'],
                                         db=0)
        self.redis = redis.Redis(connection_pool=self.pool)

    def saveEvent(self, event):
        try:
            self.redis.setex(RedisRepo.EVENTS_HASH_KEY_PREFIX + event.timestamp,
                             self.config['eventTimeToLiveSeconds'], event.pickle())
        except redis.RedisError, e:
            logging.error(e)

    def getEventStream(self):
        try:
            events = []
            event_keys = self.redis.keys(RedisRepo.EVENTS_HASH_KEY_PREFIX + '*')
            event_keys.sort()
            for event_key in event_keys:
                pickled_event = self.redis.get(event_key)
                if pickled_event is not None:
                    events.append(Event.unpickle(pickled_event))
            return events
        except redis.RedisError, e:
            logging.error(e)
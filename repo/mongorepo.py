from pymongo import MongoClient
from mongoengine import *
from domain.event import UserEvent, EventJudgement, UserEventTag

client = MongoClient('localhost', 27017)
db = client.culpa

mongo_events = db.events
event_id = mongo_events.insert(
    {"type": "IMPROVING", "timestamp": 1234567889, "instigator": "jalie", "message": "First culpa-event ever!",
     "project": "PRTR"})
print event_id
for event in mongo_events.find():
    print event


class Something(Document):
    title = StringField(max_length=100, required=True)
    message = StringField(max_length=100, required=True)

    def __init__(self, message=None, *args, **values):
        super(Something, self).__init__(*args, **values)
        self.message = message


connect('culpa')


user_event = UserEvent(message="Blabla", judgement=EventJudgement.herolike, instigators=["jalie", "jonas"], tags=UserEventTag.hack)
user_event.save()

somethong = Something(title="Blabla", message="gezever")
somethong.save()

for user_event in UserEvent.objects:
    print user_event.message

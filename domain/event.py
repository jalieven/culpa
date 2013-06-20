import time
from mongoengine import *
from flufl.enum import Enum


class Event(Document):
    timestamp = LongField(required=True)
    message = StringField(required=True, max_length=384, min_length=3)
    instigators = ListField(StringField(max_length=30))
    up_votes = LongField(required=True, default=0)
    down_votes = LongField(required=True, default=0)
    meta = {'allow_inheritance': True}

    def __init__(self, message=None, judgement=None, instigators=None, *args, **values):
        super(Event, self).__init__(*args, **values)
        self.timestamp = long(time.time() * 1000)
        self.message = message
        self.judgement = judgement
        self.instigators = instigators
        self.up_votes = 0
        self.down_votes = 0


class UserEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None, tags=None,
                 link=None, repeat_cron_expression=None, start_date=None, end_date=None,
                 *args, **values):
        Event.__init__(self, message, judgement, instigators, *args, **values)
        self.tags = tags
        self.repeat_cron_expression = repeat_cron_expression
        self.link = link
        self.start_date = start_date
        self.end_date = end_date


class BambooEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None,
                 build_key=None, build_state=None, tests=None, *args, **values):
        Event.__init__(self, message, judgement, instigators, *args, **values)
        self.build_key = build_key
        self.build_state = build_state
        self.tests = tests


class SonarEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None,
                 project_key=None, coverage=None, violations=None, *args, **values):
        Event.__init__(self, message, judgement, instigators, *args, **values)
        self.project_key = project_key
        self.coverage = coverage
        self.violations = violations


class ApiEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None,
                 key=None, endpoint=None, operation=None, *args, **values):
        Event.__init__(self, message, judgement, instigators, *args, **values)
        self.key = key
        self.endpoint = endpoint
        self.operation = operation


class EventJudgement():
    grave = 1
    shameful = 2
    herolike = 3
    improving = 4
    deteriorating = 5
    alarming = 6
    indifferent = 7
    informative = 8
    funny = 9
    fail = 10
    palm_face = 11


class UserEventTag():
    redeployment = 1
    server_restart = 2
    maintenance = 3
    compliance = 4
    help_request = 5
    functional_question = 6
    technical_question = 7
    hack = 8
    quibble = 9
    commit_and_run = 10
    complaint = 11
    praise = 12
    todo = 13
    quip = 14
    absence = 15


class BambooBuildState(Enum):
    FAILED = 1
    FIXED = 2

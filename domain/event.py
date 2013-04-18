import time

from flufl.enum import Enum
import jsonpickle


class Event:
    def __init__(self, message=None, judgement=None, instigators=None):
        self.timestamp = int(time.time() * 1000)
        self.message = message
        self.judgement = judgement
        self.instigators = instigators

    def pickle(self):
        return jsonpickle.encode(self)

    @staticmethod
    def unpickle(pickled_event):
        return jsonpickle.decode(pickled_event)


class EventJudgement(Enum):
    grave = 1
    shameful = 2
    improving = 3
    deteriorating = 4
    alarming = 5
    indifferent = 6


class BambooEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None,
                 build_key=None, build_state=None, tests=None):
        Event.__init__(self, message, judgement, instigators)
        self.build_key = build_key
        self.build_state = build_state
        self.tests = tests


class BambooBuildState(Enum):
    FAILED = 1
    FIXED = 2


class SonarEvent(Event):
    def __init__(self, message=None, judgement=None, instigators=None,
                 project_key=None, coverage=None, violations=None):
        Event.__init__(self, message, judgement, instigators)
        self.project_key = project_key
        self.coverage = coverage
        self.violations = violations
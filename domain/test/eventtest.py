import unittest
from domain.event import Event, BambooEvent, SonarEvent, EventJudgement, BambooBuildState


class TestEventHierarchy(unittest.TestCase):
    def setUp(self):
        self.name = "TestEventHierarchy"

    def testCreateSonarEventAndPickle(self):
        sonar_event = SonarEvent("OMG, something happened!", EventJudgement.grave, ["jalie"], "PRTR", 80.5, 15)
        self.assertEquals(sonar_event.violations, 15)
        self.assertEquals(sonar_event.coverage, 80.5)
        sonar_json_event = sonar_event.pickle()
        unpickled_sonar_event = Event.unpickle(sonar_json_event)
        self.assertTrue(type(sonar_event) == type(unpickled_sonar_event))
        self.assertEquals(unpickled_sonar_event.violations, 15)
        self.assertEquals(unpickled_sonar_event.coverage, 80.5)

    def testCreateBambooEventAndPickle(self):
        bamboo_event = BambooEvent("OMG, something happened!", EventJudgement.deteriorating, ["jalie"], "PRTR",
                                   BambooBuildState.FAILED, 2000)
        self.assertEquals(bamboo_event.build_state, BambooBuildState.FAILED)
        self.assertEquals(bamboo_event.tests, 2000)
        bamboo_json_event = bamboo_event.pickle()
        unpickled_bamboo_event = Event.unpickle(bamboo_json_event)
        self.assertTrue(type(bamboo_event) == type(unpickled_bamboo_event))
        self.assertEquals(bamboo_event.build_state, BambooBuildState.FAILED)
        self.assertEquals(bamboo_event.tests, 2000)
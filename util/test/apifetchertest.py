import unittest
from failure.failures import FetchException

from util.apifetcher import ApiFetcher


class TestApiFetcher(unittest.TestCase):
    def setUp(self):
        self.name = "TestApiFetcher"

    def testFetchTheGoogle(self):
        google_page = ApiFetcher.fetch("http://www.google.com", None, None, "text/html; charset=utf-8")
        self.assertIsNotNone(google_page)

    def testFetchUnAuthorized(self):
        self.assertRaises(FetchException, ApiFetcher.fetch,
                          "http://www.milieuinfo.be/sonar/violations", None, None, None)


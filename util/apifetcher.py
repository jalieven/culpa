import base64
import urllib2

from urllib2 import HTTPError
from failure.failures import FetchException

DEFAULT_CONTENT_TYPE = "application/json; charset=utf-8"


class ApiFetcher:
    @staticmethod
    def fetch(url=None, username=None, password=None, content_type=None):
        """
            Fetches the content from an url provided with optional content_type and basic auth credentials.
            Will throw a FetchException when something went wrong.
            The content_type defaults to:
        """
        request = urllib2.Request(url)
        if username is not None and password is not None:
            base64string = base64.encodestring('%s:%s' % (username, password.replace('\n', '')))
            request.add_header("Authorization", "Basic %s" % base64string)
        if content_type is not None:
            request.add_header("Content-Type:", content_type)
        else:
            request.add_header("Content-Type:", DEFAULT_CONTENT_TYPE)
        try:
            return urllib2.urlopen(request)
        except HTTPError, e:
            raise FetchException({"message": "Could not fetch url: {0}".format(url), "cause": e.__str__()})

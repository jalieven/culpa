import urllib2
import base64


class ApiFetcher:

    @staticmethod
    def fetch(url, username, password):
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (username, password.replace('\n', '')))
        request.add_header("Authorization", "Basic %s" % base64string)
        request.add_header("Content-Type:", "application/json; charset=utf-8")
        return urllib2.urlopen(request)

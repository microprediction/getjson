import grequests   # Must be imported first due to monkey patching :(
import requests, backoff
from requests.exceptions import RequestException


@backoff.on_exception(backoff.expo, exception=RequestException, max_time=30 )
def backoff_requests_get(url):
    return requests.get(url)


def request_json(url, failover_url=None):
    """ Tries to get json data from a URL for 30 seconds, then tries a failover url

        :param  url           str    e.g. 'https://config.microprediction.org/config.json'
        :param  failover_url  str    e.g. 'https://stableconfig.microprediction.org/config.json'
        :returns obj converted using json() method

        Does not throw exceptions. Fails quietly and returns None if data cannot be retrieved.

        If you don't like, use backoff directly.

    """

    res1 = backoff_requests_get(url)
    try:
        return res1.json()
    except:
        if failover_url:
            try:
                return backoff_requests_get(failover_url).json()
            except:
                pass

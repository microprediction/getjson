# getjson
Very limited mini-package for retrieving JSON data with backoff and failover


## Install 
    pip install getjson 
    
## Usage 

    data_or_none = getjson.getjson('https://config.microprediction.com/config.json')



## This does one thing

    def request_json(url, failover_url=None):
    """ Tries to get json data from a URL for 30 seconds, then tries a failover url

        :param  url           str    e.g. 'https://config.microprediction.org/config.json'
        :param  failover_url  str    e.g. 'https://stableconfig.microprediction.org/config.json'
        :returns obj converted using json() method

        Does not throw exceptions. Fails quietly and returns None if data cannot be retrieved.

        If you don't like, use backoff directly.

    """
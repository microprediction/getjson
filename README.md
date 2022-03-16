# getjson

A micro-package for retrieving JSON data, en masse potentially, with backoff and failover


## Install 

    pip install getjson 
    
## Usage 

    data_or_none = getjson.getjson('https://config.microprediction.com/config.json')

## Usage w/ failover

    data_or_none = getjson.getjson('https://config.microprediction.com/config.json','https://stableconfig.microprediction.com/config.json')

## Multiple urls

    urls = ['http://api.microprediction.org/lagged/traffic_absolute_speed.json','https://api.microprediction.org/lagged/die.json']
    data = getjson.mgetjson(urls=urls)    

## Multiple urls with failover

    urls = ['http://api.microprediction.org/lagged/traffic_absolute_speed.json','https://api.microprediction.org/lagged/die.json']
    failover_urls = ['http://stableapi.microprediction.org/lagged/traffic_absolute_speed.json','https://stableapi.microprediction.org/lagged/die.json']
    data = getjson.mgetjson(urls=urls, failover_urls=failover_urls)    

    
### Dude, what's microprediction?

New video tutorials are available at https://www.microprediction.com/python-1 to help you
get started running crawlers at www.microprediction.com and win $50,000. 

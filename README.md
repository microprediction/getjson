# getjson
Does one thing! 

A micro-package for retrieving JSON data with backoff and failover


## Install 
    pip install getjson 
    
## Usage 

    data_or_none = getjson.getjson('https://config.microprediction.com/config.json')

## Usage w/ failover

    data_or_none = getjson.getjson('https://config.microprediction.com/config.json','https://stableconfig.microprediction.com/config.json')

    
### Dude, what's microprediction?

New video tutorials are available at https://www.microprediction.com/python-1 to help you
get started running crawlers at www.microprediction.com and win $50,000. 

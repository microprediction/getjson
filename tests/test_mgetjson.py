from getjson import mgetjson


valid_url_1          = 'https://config.microprediction.org/config.json'
valid_url_2          = 'https://stableconfig.microprediction.org/config.json'


invalid_urls = ['http://api.microprediction.org/lagged/traffic_absolute_speed',
              'https://api.microprediction.org/lagged/die']

valid_urls = ['http://api.microprediction.org/lagged/traffic_absolute_speed.json',
              'https://api.microprediction.org/lagged/die.json']
valid_failover_urls = ['http://stableapi.microprediction.org/lagged/traffic_absolute_speed.json',
              'https://stableapi.microprediction.org/lagged/die.json']

almost_url_2          = 'https://stableconfig.microprediction.org/config.json1'
invalid_json_url_1   = 'https://www.smh.com.au/'
invalid_json_url_2   = 'https://www.cnn.com/'
invalid_url          = 'https://www.notaurl09098df0a9sdf8a09ds8fa09fas8d0f.com/nowaydataishere.json'


def test_mgetjson_valid_valid():
    data = mgetjson(urls=valid_urls, failover_urls=valid_failover_urls)
    assert isinstance(data,list)
    assert isinstance(data[0],list)


def test_getjson_invalid_valid():
    data = mgetjson(urls=invalid_urls,failover_urls=valid_urls)
    assert isinstance(data, list)
    assert isinstance(data[0], list)




if __name__=='__main__':
    test_mgetjson_valid_valid()
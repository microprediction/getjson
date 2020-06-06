from getjson import getjson


valid_url_1          = 'https://config.microprediction.org/config.json'
valid_url_2          = 'https://stableconfig.microprediction.org/config.json'
almost_url_2          = 'https://stableconfig.microprediction.org/config.json1'
invalid_json_url_1   = 'https://www.smh.com.au/'
invalid_url          = 'https://www.notaurl09098df0a9sdf8a09ds8fa09fas8d0f.com/nowaydataishere.json'


def test_getjson_valid_valid():
    data = getjson(url=valid_url_1,failover_url=invalid_json_url_1)
    assert isinstance(data,dict)

def test_getjson_invalid_valid():
    data = getjson(url=invalid_json_url_1,failover_url=valid_url_1)
    assert isinstance(data, dict)


def test_almost():
    data = getjson(url=almost_url_2,failover_url=valid_url_1)
    assert isinstance(data, dict)


def test_getjson_invalidalso_valid():
    try:
        data = getjson(url=invalid_url,failover_url=valid_url_1)
        raise NotImplementedError
    except:
        pass

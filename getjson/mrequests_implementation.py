from typing import List

# I really must warn you about usin this. If you import grequests it will monkey patch
# You need to read this issue and decide if it is worth it https://github.com/gevent/gevent/issues/1016

def mrequest_json(urls:[str], failover_urls=None)->List:
    return mrequest_json_no_failover(urls) if failover_urls is None else mrequest_json_with_failover(urls=urls, failover_urls=failover_urls)


def mrequest_json_no_failover(urls):
    try:
        import grequests
    except:
        raise EnvironmentError('pip install grequests')
    rs = (grequests.get(u) for u in urls)
    rs_map = grequests.map(rs)
    return [r.json() for r in rs_map]


def mrequest_json_with_failover(urls, failover_urls):
    n = len(urls)
    assert n==len(failover_urls)
    both = mrequest_json_no_failover(urls = list(urls)+list(failover_urls))
    orig_json = both[:n]
    fail_json = both[n:]
    return [ orig_data if orig_data is not None else fail_data for orig_data,fail_data in zip(orig_json,fail_json) ]


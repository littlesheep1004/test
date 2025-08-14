import requests

def test_baidu():
    r = requests.get("https://www.baidu.com")
    assert r.status_code == 200

def test_math():
    assert 1 + 1 == 2

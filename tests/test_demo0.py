import pytest
import requests

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -2) == -3

def test_httpbin_get():
    response = requests.get("https://httpbin.org/get")
    assert response.status_code == 200

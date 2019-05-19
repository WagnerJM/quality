import requests
import pytest

url = "http://localhost:5001/api/v1/qrk/6746138d-1d58-4584-9cc2-2be70911a712/messwert"

def test_messwerte():
    data = {
        "date": "19.05.2019",
        "wert": "10.01"
    }
    r = requests.post(
        "http://localhost:5001/api/v1/qrk/6746138d-1d58-4584-9cc2-2be70911a712/messwert", json=data)
    assert r.status_code == 201
    #data = {
    #    "datum": "16.05.2019",
    #    "wert": "10.05"
    #}
    #assert r.status_code == 201

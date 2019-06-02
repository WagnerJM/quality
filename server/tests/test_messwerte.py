import requests
import pytest
from app.worker import celery
import random


def test_messwerte():
    data = {
        "date": "22.05.2019",
        "wert": random.uniform(9,11)
    }
    r = requests.post(
        "http://localhost:5001/api/v1/qrk/899b3a62-7569-4244-b021-0b3d857eaa81/messwert", json=data)
    assert r.status_code == 201


url = "http://localhost:5001/api/v1/qrk/8343fddd-1fa3-458b-b2ef-a8c706fddce4/messwert"
"""
def test_messwerte():
    data = [
        {
        "date": "19.05.2019",
        "wert": random.uniform(9,11)
        },
        {
        "date": "20.05.2019",
        "wert": random.uniform(9,11)
        },
        {
        "date": "21.05.2019",
        "wert": random.uniform(9,11)
        },
        {
        "date": "22.05.2019",
        "wert": random.uniform(9,11)
        }
    ]
    for each in data:
        r = requests.post(url , json=each)
        assert r.status_code == 201

"""

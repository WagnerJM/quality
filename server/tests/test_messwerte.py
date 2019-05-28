import requests
import pytest
from app.worker import celery

url = "http://localhost:5001/api/v1/qrk/acfe19e0-3fcf-4084-ba4f-bab2b7b8f530/messwert"

def test_messwerte():
    data = {
        "date": "19.05.2019",
        "wert": "10.01"
    }
    r = requests.post(
        "http://localhost:5001/api/v1/qrk/acfe19e0-3fcf-4084-ba4f-bab2b7b8f530/messwert", json=data)
    assert r.status_code == 201



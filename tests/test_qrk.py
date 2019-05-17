import requests
import pytest

url = "http://localhost:5001/api/v1"

def test_create_qrk():
    post_data = {
        "titel": "Titel Test",
        "x_achse_titel": "X-Achse",
        "y_achse_titel": "Y-Achse"
    }
    r = requests.post(url + "/qrk", data=post_data)
    assert r.status_code = 201
    assert r.data == post_data
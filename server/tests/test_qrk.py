import requests
import pytest
import json

url = "http://localhost:5001/api/v1"

def test_create_qrk():
    post_data = {
	"titel": "Titel",
	"x_achse_titel": "Datum",
	"y_achse_titel": "Test"
    }
    r = requests.post("http://localhost:5001/api/v1/qrk", json=post_data)
    assert r.status_code == 201
    assert r.json() == {
        "msg": "Qrk wurde angelegt"
        }

def test_get_qrk():
    r = requests.get("http://localhost:5001/api/v1/qrk")
    assert r.status_code == 200

"""
def test_put_resource():
    data = {
	"titel": "Neuer Titel",
	"x_achse_titel": "X-Achse",
	"y_achse_titel": "Y-Achse"
    }
    r = requests.put(
        "http://localhost:5001/api/v1/qrk/899b3a62-7569-4244-b021-0b3d857eaa81", json=data)

    assert r.status_code == 200
    assert r.json() == {
        "msg": "Qrk Daten wurden geupdatet."
    }

def test_get_specific_qrk():
    r = requests.get(
        "http://localhost:5001/api/v1/qrk/acfe19e0-3fcf-4084-ba4f-bab2b7b8f530")
    assert r.status_code == 200
    assert r.json() == {
        "id": "acfe19e0-3fcf-4084-ba4f-bab2b7b8f530",
        "titel": "Neuer Titel"
    }
"""

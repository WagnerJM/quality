import requests
import pytest#
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

def test_get_specific_qrk():
    r = requests.get(
        "http://localhost:5001/api/v1/qrk/29786d25-d03e-4e42-abad-a0797118d36a")
    assert r.status_code == 200
    assert r.json() == {
        "id": "29786d25-d03e-4e42-abad-a0797118d36a",
        "titel": "Titel"
    }

def test_put_resource():
    data = {
	"titel": "Neuer Titel",
	"x_achse_titel": "X-Achse",
	"y_achse_titel": "Y-Achse"
    }
    r = requests.put(
        "http://localhost:5001/api/v1/qrk/29786d25-d03e-4e42-abad-a0797118d36a", json=data)

    assert r.status_code == 200
    assert r.json() == {
        "msg": "Qrk Daten wurden geupdatet."
    }

from flask import request
from flask_restful import Resource
from app.api.qrk.models import Qrk, QrkSchema, Messwert, MesswertSchema
from app.utils import str2uuid
from app.database import db
from sqlalchemy import and_
from datetime import datetime

class QrkListApi(Resource):
    def get(self):
        qmodel = QrkSchema()
        data = Qrk.query.all()
        return qmodel.dump(data, many=True).data, 200
    
    def post(self):
        schema = QrkSchema()
        data = request.get_json()
        qrk_schema = schema.load(data)
        qrk = Qrk(**data)
        erster_messpunkt = Messwert(wert=0.0, date="16.05.2019")
        qrk.messwerte.append(erster_messpunkt)
        qrk.save()
        return { 
            "msg": "Qrk wurde angelegt"
        }, 201

         

class QrkApi(Resource):
    def get(self, qrk_id):
        qrk = Qrk.find_by_id(id=str2uuid(qrk_id))
        qschema = QrkSchema()
        return qschema.dump(qrk).data, 200

    def put(self, qrk_id):
        query = Qrk.query.filter_by(id=str2uuid(qrk_id))
        query.update(request.json)

        db.session.commit()

        return {
            "msg": "Qrk Daten wurden geupdatet."
        }, 200

class MesswertApi(Resource):
    def post(self, qrk_id):
        data = request.get_json()
        qrk = Qrk.find_by_id(str2uuid(qrk_id))
        neuer_Messwert = Messwert(**data)
        qrk.messwerte.append(neuer_Messwert)

        qrk.save()

        return {
            "msg": "Messpunkt wurde gespeichert."
        }, 201
    
    def put(self, qrk_id, messwert_id):
        qrk = Qrk.find_by_id(str2uuid(qrk_id))
        messwert = Messwert.query.filter(and_(qrk_id == qrks.qrkID, messwert.id == str2uuid(messwert_id)))
        if not messwert:
            return {
                "msg": "Messwert konnte nicht gefunden werden."
            }, 500
        messwert.update(request.json)
        db.session.commit()

        return {
            "msg": "Messwert wurde modifiziert."
        }, 201
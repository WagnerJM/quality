from app.database import BaseMixin, db
from app.serializer import ma
from sqlalchemy.dialects.postgresql import JSON
from marshmallow import post_load
from datetime import datetime
from marshmallow.fields import Nested
class Qrk(BaseMixin, db.Model):
    __tablename__ = "qrks"

    qrkID = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String, nullable=False)
    x_achse_titel = db.Column(db.String, nullable=False)
    y_achse_titel = db.Column(db.String, nullable=False)

    obere_warngrenze = db.Column(db.Float)
    untere_warngrenze = db.Column(db.Float)
    obere_eingriffsgrenze = db.Column(db.Float)
    untere_eingriffsgrenze = db.Column(db.Float)
    stdabw = db.Column(db.Float)

    mittelwert = db.Column(db.Float)

    datei_pfad = db.Column(db.String)

    messwerte = db.relationship('Messwert', backref="Qrk", lazy=False)

    def __init__(self, titel, x_achse_titel, y_achse_titel):
        self.titel = titel
        self.x_achse_titel = x_achse_titel
        self.y_achse_titel = y_achse_titel
    

class Messwert(BaseMixin, db.Model):
    __tablename__ = 'messwert'

    messwertID = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.DateTime, nullable=False)
    wert = db.Column(db.Float, nullable=False)
    valid = db.Column(db.Boolean, default=True)
    qrk_id = db.Column(db.Integer, db.ForeignKey('qrks.qrkID'))

    def __init__(self, wert, date):
        self.wert = wert
        self.datum = datetime.strptime(date, "%d.%m.%Y")

class MesswertSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "datum"
            "wert",
            "valid"
        )

class QrkSchema(ma.Schema):
    messwerte = Nested(MesswertSchema, many=True, exclude="qrk_id")
    class Meta:
        fields = (
            "id",
            "titel",
            "x_achse_titel",
            "y_achse_titel",
            "obere_warngrenze",
            "untere_warngrenze",
            "obere_eingriffsgrenze",
            "untere_eingriffsgrenze",
            "stdabw",
            "mittelwerte",
            "datei_pfad"
            
        )


    


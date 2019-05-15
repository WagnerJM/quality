from app.database import db
from celery import shared_task
from app.api.qrk.models import Qrk, Messwert

@shared_task
def create_diagramm(qrk_id):
    pass

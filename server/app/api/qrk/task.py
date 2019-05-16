from app.database import db
from celery import shared_task
from app.api.qrk.models import Qrk, Messwert
from app.utils import str2uuid, create_dataframe, create_Chart

@shared_task
def create_diagramm(qrk_id):
    
    qrk, data = create_dataframe(qrk_id)
    
    create_Chart(qrk, data, path="../../images")


    

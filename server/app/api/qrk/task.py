from app.database import db
from tasks.celery import app
from app.api.qrk.models import Qrk, Messwert
from app.utils import create_dataframe, create_QC_Chart

@app.task
def create_diagramm(qrk_id, path):
    
    df, qrk = create_dataframe(qrk_id)

    create_dataframe(qrk, df, path)


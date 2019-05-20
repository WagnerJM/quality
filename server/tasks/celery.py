
import os
from celery import Celery, current_task
from celery.result import AsyncResult
from tasks.qcChart import create_dataframe, create_QC_Chart


REDIS_URL = 'redis://:{pw}@redis:6379/0'.format(pw=os.getenv('REDIS_PW'))
BROKER_URL = 'redis://:{pw}@redis:6379/1'.format(pw=os.getenv('REDIS_PW'))



celery = Celery('tasks', backend=REDIS_URL, broker=BROKER_URL)


@celery.task(name="create_QC_Chart")
def create_diagramm(qrk_id, path):
    
    df, qrk = create_dataframe(qrk_id)

    create_dataframe(qrk, df, path)
import matplotlib
import matplotlib.pyplot as plt
import numpy as np  
from app.database import db
from werkzeug.utils import secure_filename
from app.api.qrk.models import Qrk

from uuid import UUID


from datetime import datetime

def str2uuid(string):
    return UUID(string)

def create_dataframe(qrk_id):
    #Get QRK from qrk_id
    qrk = Qrk.find_by_id(str2uuid(qrk_id)

    #create pandas dataframe from query where only the valid are used
    df = pd.read_sql(Messwert.query.filter(qrk_id=qrk.qrkID), db.session.bind).query("valid == True")

    #erstelle statistik grundwerte
    stats = df.wert.describe()

    #Speichern der Daten für die jeweilige QRK
    qrk.mittelwert = stats.get('mean')
    qrk.stdabw = stats.get("std")
    qrk.obere_warngrenze = qrk.mittelwert + 2 * qrk.stdabw
    qrk.untere_warngrenze = qrk.mittelwert - 2 * qrk.stdabw
    qrk.obere_eingriffsgrenze = qrk.mittelwert + 3 * qrk.stdabw
    qrk.untere_eingriffsgrenze = qrk.mittelwert - 3 * qrk.stdabw

    qrk.save()

    return df



def create_QC_Chart(qrk, df, path=None):
    
    min_y = df.wert.get('min')
    max_y = df.wert.get("max")
    max_x = df.datum.max()

    #numpy arrays für die filter anwendung
    np_arr_x = df.datum.values
    np_arr_y = df.wert.values

    filter = np.where(
        (data < uwg ) | (data > owg)
    )
    # plot der Ausreißer
    plt.plot(np_arr_x[filter],np_arr_y[filter], marker="o", color="red")

    #erstellt die OWG/UWG Linie + Hintergrund
    plt.axhline(qrk.obere_warngrenze, color="blue", linestyle="--")
    plt.annotate("OWG", xy=(max_x + 2, qrk.obere_warngrenze)

    plt.axhline(qrk.untere_warngrenze, color="blue", linestyle="--")
    plt.annotate("UWG", xy=(max_x + 2, qrk.untere_warngrenze)

    #erstellt die OEG/UEG Linie
    plt.axhline(qrk.obere_eingriffsgrenze, color="orange", linestyle="--")
    plt.annotate("OEG", xy=(max_x + 2, qrk.obere_eingriffsgrenze

    plt.axhline(qrk.untere_eingriffsgrenze, color="orange", linestyle="--")
    plt.annotate("UEG", xy=(max_x + 2, qrk.untere_eingriffsgrenze

    # OEG/UEG Hintergrund Bereich
    plt.fill_between(df.datum,qrk.mittelwert+ (2 * qrk.stdabw)  ,(qrk.mittelwert + 5*  qrk.stdabw), color="red", alpha=0.2)
    plt.fill_between(df.datum,qrk.mittelwert- (2 * qrk.stdabw)  ,(qrk.mittelwert - 5*  qrk.stdabw), color="red", alpha=0.2)

    #erstellt die Mittelwert Linie
    plt.axhline(qrk.mittelwert, color="green", linestyle="--")
    plt.annotate("Mittelwert", xy=(max_x + 2, qrk.mittelwert)

    #legt die Größe des Plots fest
    plt.rcParams["figure.figsize"] = [16,9]
    
    #setzt die Skalierungslimits
    #plt.xlimit()
    #plt.ylimt()

    #plot der Daten
    plt.plot(df.datum, df.wert, color="grey", alpha=0.5)
    plt.title(qrk.titel)
    plt.xlabel(qrk.x_achse_titel)
    plt.ylabel(qrk.y_achse_titel)
    plt.legend()
    
    if path is None:
        print("File can not be saved. Not file path.")
    else:
        plt.savefig(path + secure_filename(qrk.titel) + '.png' , orientation="landscape")
        print("File created")




    


import datetime

def trovaData():
    oggi=datetime.date.today()
    anno=str(oggi).split('-')[0]
    mese=str(oggi).split('-')[1]
    giorno=str(oggi).split('-')[2]
    data=str(giorno+'_'+mese+'_'+anno)
    return data
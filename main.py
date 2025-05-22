import os
import Moduli
import time

data=Moduli.trovaData()
orario=str(time.strftime("%H:%M:%S")).replace(':','_')
os.system('cls')
os.mkdir('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario)
os.mkdir('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario+'\\Totale\\')
intestazioneXL='nomeCognome,luogoNascita,dataNascita,numeroRomano,numeroRomanoDue,natoNata,@firmaRettrice,dataConsegna,materia\n'
fInDesign=open('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario+'\\Totale\\'+'fileInDesign'+data+'.csv','a')
fInDesign.write(intestazioneXL)
files=os.listdir('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\fileSorgente\\')
pathFirme='C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\Firme\\'
imgRettrice='apolimeni.tif'
firmaRettrice=pathFirme+imgRettrice
for elemento in files:
    with open('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\fileSorgente\\'+elemento,'r') as file:
        contenuto=file.readlines()
        for i in range(0,4):
            contenuto.pop(0) #elimina prime righe
        for riga in contenuto:
            lista=riga.split(';')
            Moduli.controllaApostrofo(lista)
            if len(lista)!=10:
                lista=Moduli.correggi(lista)
            nomeFile=Moduli.generaFile(lista,data,orario,intestazioneXL)
            attestatoOggetto=Moduli.attestato(lista)
            rigaCsv=attestatoOggetto.nomeCognome+','+attestatoOggetto.luogoNascita+','+attestatoOggetto.dataNascita+','+attestatoOggetto.numeroRomano+','+attestatoOggetto.numeroRomanoDue+','+attestatoOggetto.natoNata+','+firmaRettrice+','+attestatoOggetto.dataAttestato+','+attestatoOggetto.materia+'\n'
            fInDesign.write(rigaCsv)
            with open(nomeFile,'a') as fileOut:
                fileOut.write(rigaCsv)
fInDesign.close()

### Apri InDesign
### manda PDF a stampante
### archivia in server
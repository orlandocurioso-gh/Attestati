import os
import time

def generaFile(lista,data,orario,intestazione):
    tipo=lista[8]
    #print (data)
    if tipo !='\n':
        if '/' in tipo:
            tipo=tipo.replace('/','-')
        files=os.listdir('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario)
        #print (files)
        if tipo+data+'.csv' not in files:
            nomeFile='C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario+'\\'+tipo+data+'.csv'
            fileOut=open('C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario+'\\'+tipo+data+'.csv','a')
            fileOut.write(intestazione)
            fileOut.close()
        else:
            nomeFile='C:\\Users\\484972\\Documents\\Coding\\Python\\Sapienza\\Attestati\\Outputs\\'+data+'_'+orario+'\\'+tipo+data+'.csv'
        return nomeFile
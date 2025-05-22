import os

def dividi_stringa_maiuscole(stringa):
  """
  Divide una stringa in sottostringhe, separando ogni volta che incontra un carattere maiuscolo (senza regex).
  """
  sottostringhe = []
  inizio = 0
  for i in range(1, len(stringa)):
      if stringa[i].isupper():
          sottostringhe.append(stringa[inizio:i])
          inizio = i
  sottostringhe.append(stringa[inizio:])
  return sottostringhe

def controllaApostrofo(lista):
    nome=''
    citta=''
    token=lista[0]
    if "'" in token:
        apostrofi=token.count("'")
        match apostrofi:
            case 2:
                listaDivisa=dividi_stringa_maiuscole(token)
                i=0
                for elmeneto in listaDivisa:
                    if i<2:
                        nome=nome+listaDivisa[i]
                    else:
                        citta=citta+listaDivisa[i]
                    i=i+1
                lista.pop(0)
                lista.insert(0,nome)
                lista.insert(1,citta)
                #print (lista)
    else:
        pass
    return lista

"""
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
            controllaApostrofo(lista)
"""
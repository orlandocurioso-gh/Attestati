def correggi(lista):
    tokenDaCorreggere=lista[0]
    print ('riga errata: ',tokenDaCorreggere)
    nomeCognome=input('inserisci il nome e cognome corretto: ')
    luogoNascita=input('inserisci il luogo di nascita corretto: ')
    lista.pop(0)
    lista.insert(0,nomeCognome)
    lista.insert(1,luogoNascita)
    #print (lista)
    return lista

#lista=['Adriano BianchiPalestrina (Roma),', '29 ottobre 1971', 'MMXX', 'I', 'nato il', 'apolimeni', '6 giugno 2024', 'Architetto', '\n']
#correggi(lista)
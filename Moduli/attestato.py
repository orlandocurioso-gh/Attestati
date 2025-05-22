class attestato:
    def __init__(self,lista):
        self.nomeCognome=lista[0]
        self.luogoNascita=lista[1][:-1]
        self.dataNascita=lista[2]
        self.numeroRomano=lista[3]
        self.numeroRomanoDue=lista[4]
        self.natoNata=lista[5]
        self.firmaRettrice=lista[6]
        self.dataAttestato=lista[7]
        self.materia=lista[8]

    def stampaDatiAttestato(self):
        riga=self.nomeCognome+'                      '+self.materia
        return riga
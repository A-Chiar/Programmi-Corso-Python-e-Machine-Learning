#creo una classe per la gestione degli errori che possono comparire all'interno del programma
class Error():
    
    def gestioneKeyError(self):
        print("\nError: Stai tentando di accedere ad una chiave inesistente ")

    def gestioneAttributeError(self):
        print("\nDato non presente")

    def gestioneTypeError(self):
        print("\nErrore sul tipo, NaN type presente e non sovrascrivibile")
    
    


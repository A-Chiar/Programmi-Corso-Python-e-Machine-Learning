#Pandas
"""Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà."""
#Dataset: 
"""ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)
"""
#Caricamento e Esplorazione Iniziale:
"""
X1. Caricamento e Esplorazione Iniziale:
     1A. Caricare i dati da un file CSV. #TEMPO STIMATO: 10 min  10 min
     2A. Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti. #TEMPO STIMATO: 25 minuti 
2. Pulizia dei Dati: #TEMPO STIMATO: 30 minuti >
    2A. Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
    2B. Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3. Analisi Esplorativa dei Dati (EDA): #TEMPO STIMATO: 50 minuti <20 min
    3A. Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
    3B. Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
    3C. Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4. Preparazione dei Dati per la Modellazione: #TEMPO STIMATO: 30 minuti
    4A. Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    4B. Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
5. Analisi Statistica e Predittiva: #TEMPO STIMATO:  40 minuti
    5A. Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
        su altri fattori.
    5B. Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve)."""

"""Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà."""
#Dataset: 
"""ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)
"""
#Caricamento e Esplorazione Iniziale:
"""
1. Caricamento e Esplorazione Iniziale:
     1A. Caricare i dati da un file CSV."""

import pandas as pd
import numpy as np
import random as rd
#creo la classe compagnia telecomunicazioni
class CompagniaTelecomunicazioni():

    def crea_dataframe(self):
        df = pd.read_csv('EsercizioFinale.csv')
        print(df)
        return df
    #creo un metodo per le statistiche descrittive
    """2A. Utilizzare info(), describe(), e value_counts() 
    per esaminare la distribuzione dei dati e identificare colonne con valori mancanti."""
    def analisi_dataframe(self, df):
        print("\n Riassunto delle informazioni del dataframe: ")
        print(df.info(verbose=True))
        print("\n Descrizione del dataframe: ")
        print(df.describe(include='all'))
        for column in df.columns:
            print(f"\nConta i valori per la colonna {column}:")
            print(df[column].value_counts())

    def elimina_dati_mancanti(self, df):
        elimina = df.dropna(subset=['ID_Cliente'])
        print(elimina)
        return elimina
    def imputa_dati_mancanti(self,df):
        imputa = df.copy()
        imputa['Durata_Abbonamento'].fillna(df['Durata_Abbonamento'].mean(), inplace=True) #creare ciclo for per le colonne
        print(imputa)
        return imputa
    
    def anomalie(self,df):
        df= df[df['Età'] >0]
        print(df)
        
    def nuova_colonna(self,df):
        df['Costo_per_GB']=df['Tariffa_Mensile']/df['Dati_Consumati']
        print("\n è stata aggiunta la categoria Costo_per_GB: ",df)
    #3B. Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
    def raggruppa(self,df):
        media_età_tariffa = df.groupby('Età')['Tariffa_Mensile'].mean()
        print("\n",media_età_tariffa)
        media_churn_durata = df.groupby('Churn')['Tariffa_Mensile'].mean()
        print("\n", media_churn_durata)
        moda_età_durata = df.groupby('Durata_Abbonamento')['Età'].mean()
        print("\n", moda_età_durata)
    def correlazioni(self,df):
        print(df.corr(method = 'pearson',numeric_only = True)) #fare in modo di eliminare dalla corr l'uso della colonna ID
    #4A. Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    def modifica_churn(self,df):
        df['Churn']=df['Churn'].replace(['No','Sì'],[0,1])
        return df
    def normalizzazione(self,df):
        print("\n I valori normalizzati sono: ")
        for colonna in df.columns:
            df[colonna]=(df[colonna] - df[colonna].min()) / (df[colonna].max() - df[colonna].min())
        print(df)

    """Normalizzazione Min-Max
La normalizzazione Min-Max scala i dati in un range specificato, tipicamente 0 a 1, secondo la formula: import pandas as pd

# Creazione di un DataFrame di esempio
data = {'punteggio': [23, 45, 67, 89, 56, 78]}
df = pd.DataFrame(data)

# Normalizzazione Min-Max
df['punteggio_norm'] = (df['punteggio'] - df['punteggio'].min()) / (df['punteggio'].max() - df['punteggio'].min())

print(df)"""
compagnia = CompagniaTelecomunicazioni()
df = compagnia.crea_dataframe()
compagnia.analisi_dataframe(df)
df_eliminati = compagnia.elimina_dati_mancanti(df)
df_imputati = compagnia.imputa_dati_mancanti(df_eliminati)
compagnia.nuova_colonna(df)
compagnia.raggruppa(df)
compagnia.correlazioni(df)
compagnia.modifica_churn(df)
compagnia.normalizzazione(df)
compagnia.anomalie(df)
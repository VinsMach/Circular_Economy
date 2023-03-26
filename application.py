#importiamo le librerie 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#il successive è il link dell’open data dell’ISPRA
link = "https://annuario.isprambiente.it/sites/default/files/sys_ind_files/indicatori_ada/760/Tabella%201.xlsx"

#setto la variabile pesoBott a 750 grammi
pesoBott = 750
valoreBottTonn = 45

#datasetIniziale conterrà il file scaricato da elaborare
#tramite la libreria pandas i dati sono già clean
datasetIniziale = pd.read_excel(link, index_col=0)

#attraverso la riga successiva con numpy trasformo una lista in array
arrayCompleto= np.array(datasetIniziale.values.tolist())

#Nel file è presente il primo elemento dell’array che identifica la tipologia di rifiuto, ricavo la riga
datiClean = np.where(arrayCompleto == 'Rifiuti in vetro')

#nella prima linea del file troviamo le date, e rimuovo il primo elemento
date_finali = [int(numeric_string) for numeric_string in arrayCompleto[0][1:]]

#estraggo i valori della riga corrispondente al vetro precedentemente identificata
valori = arrayCompleto[datiClean[0][0]][1:]

#faccio un ulteriore check e faccio il casting float
valori_float = valori.astype(float)

#per ogni elemento presente nell’array valori finali, faccio una trasformazione in grammi e divido per il peso della bottiglia 
valori_finali = [round(B *1000000/ pesoBott) for B in valori_float]
valori_economici_finali = [(B * valoreBottTonn) for B in valori_float]

#vado a definire un range del dataframe num bottiglie
tabellaNumBott = {'anno': date_finali, 'numero_bottiglie': valori_finali}
dataFrameNumBott = pd.DataFrame(data= tabellaNumBott)

#stampo a video una tabella con i contenuti num bottiglie
dataFrameNumBott

#vado a definire un range del dataframe euro 
tabellaCompEcon = {'anno': date_finali, 'Euro guadagnati': valori_economici_finali}
dataFrameCompEcon = pd.DataFrame(data= tabellaCompEcon)

#stampo a video una tabella del range identificato
dataFrameCompEcon 

# definisco l'area grafica ed associo i valori
plt.rcParams["figure.autolayout"] = True

ax1 = plt.subplot()
ax1.set_xlabel("Anni")
ax1.set_ylabel("Bottiglie Riutilizzabili", color='red', fontsize=14)
ax1.tick_params(axis="y", labelcolor='red')
l1, = ax1.plot(date_finali ,valori_finali, color='red')
#utilizzo entrambi gli assi delle ordinate
ax2 = ax1.twinx()

ax2.set_ylabel("Milioni di Euro Guadagnati", color='green', fontsize=14)
ax2.tick_params(axis="y", labelcolor='green')

l2, = ax2.plot(date_finali ,valori_economici_finali, color='green')

# faccio visualizzare il grafico 
plt.show()


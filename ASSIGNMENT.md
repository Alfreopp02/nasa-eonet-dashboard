# 📋 SPECIFICA DEL TEST PRATICO: DEVELOPER

## 🎯 Obiettivo del Test
Valutare la capacità del candidato di progettare e implementare un **sistema completo** in grado di recuperare, gestire, analizzare e visualizzare dati provenienti da fonti pubbliche NASA (API). 

La soluzione richiede una **dashboard interattiva** dotata di filtri avanzati per:
* Periodo 
* Tipologia di missione 
* Area geografica


## 🌌 Scenario
La NASA mette a disposizione un’ampia gamma di API pubbliche tramite il portale [api.nasa.gov](https://api.nasa.gov). Tali API consentono l’accesso a dati su missioni spaziali, osservazioni astronomiche e disastri naturali. Il compito è organizzare queste informazioni e renderle navigabili.


## 🚀 Obiettivi del Progetto

1. **Recupero dati:** Connessione a una o più API pubbliche NASA.
2. **Persistenza:** Salvataggio dei dati all'interno di un database relazionale (**SQL**) documentato.
3. **Output informativo:** Creazione di grafici, report o mappe interattive che evidenzino correlazioni.
4. **Filtraggio avanzato:** Possibilità per l'utente di sezionare i dati a piacimento.


## ⚙️ Requisiti Tecnici Minimi (Obbligatori)

* [x] **Query SQL:** Scrittura manuale di query (operazioni CRUD + almeno una query analitica con `JOIN` o funzioni aggregate).
* [x] **Integrazione API:** Realizzata tramite linguaggio a scelta (*Python*).
* [x] **Schema Dati:**Progettazione di uno schema dati coerente, documentato tramite diagramma ER o equivalente.   
* [x] **Consultazione:** Output finale d'impatto e di immediata comprensione.

---

## 🌟 Bonus Facoltativi (Implementati)

* **Tecniche di ottimizzazione:** Tecniche di caching e/o normalizzazione per ottimizzare le prestazioni.
* **Visualizzazioni avanzate:** Visualizzazioni avanzate: analisi temporali, correlazioni, mappe geografiche, modelli    predittivi.  
* **UX Curata:** Interfaccia utente curata, ordinata ed efficace
* **Arricchimento Dati (Extra):** Documentazione dettagliata che illustri scelte progettuali, criticità riscontrate e potenziali 
miglioramenti. 


## 📦 Contenuto della Consegna

1. Codice sorgente del progetto.   
2. Schema SQL del database utilizzato.   
3. Relazione tecnica che descriva:   
    a. API selezionate e motivazioni della scelta   
    b. Architettura della soluzione   
    c. Query principali   
    d. Insight ricavati dall’analisi dei dati   
4. Repository GitHub completo e navigabile.
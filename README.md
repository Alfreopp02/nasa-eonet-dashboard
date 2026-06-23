# 🌍 NASA EONET Dashboard - Test Pratico Developer

> 📌 **Nota:** Il testo originale e i requisiti della consegna sono consultabili nel file [ASSIGNMENT.md](ASSIGNMENT.md)

Questo progetto è stato realizzato come test pratico per valutare le competenze nello sviluppo di una pipeline di dati completa,  dal recupero tramite API pubbliche della NASA alla persistenza su database relazionale, fino alla visualizzazione tramite una dashboard interattiva.

## 1. Relazione Tecnica

### a. API Selezionate e Motivazioni
Per questo progetto è stata scelta l'API **EONET (The Earth Observatory Natural Event Tracker)**. 
La scelta è ricaduta su questa risorsa per tre ragioni fondamentali legate ai requisiti del test:
- **Filtraggio Geografico:** Ogni evento EONET è dotato di coordinate standard (latitudine e longitudine), rendendo immediata e precisa la mappatura visiva.
- **Filtraggio Temporale e di Stato:** L'API fornisce timestamp esatti per ogni singola osservazione e permette di estrarre sia gli eventi attualmente in corso che lo storico di quelli passati, offrendo una panoramica completa.
- **Categorizzazione Intrinseca:** Gli eventi sono già normalizzati in categorie ben distinte (es. *Wildfires*, *Severe Storms*, *Volcanoes*), permettendo analisi raggruppate e query aggregate immediate.

### b. Architettura della Soluzione
Il sistema è sviluppato in **Python** ed è strutturato in due moduli logici principali per mantenere una chiara separazione tra backend (dati) e frontend (presentazione):
1. **Data Ingestion (ETL):** Lo script `data_ingestion.py` interroga l'endpoint REST della NASA, estrae il JSON e lo processa,elabora lo stato dell'evento (Attivo/Passato)  e gestisce la persistenza caricandolo in un database locale SQLite.
2. **Data Presentation:** L'interfaccia grafica è stata sviluppata utilizzando **Streamlit**, che si connette al database, estrae i dati tramite Pandas e li renderizza attraverso componenti web interattivi (mappe dinamiche, metriche e grafici a barre).

### c. Database e Query Principali
Il database relazionale (`eonet_data.db` via SQLite) è stato progettato con uno schema logico a due tabelle per rispettare le regole di normalizzazione ed evitare ridondanze, separando l'anagrafica dell'evento dalle sue osservazioni spazio-temporali:
- **`eventi`** (`id` PK, `titolo`, `categoria`,`stato`)
- **`posizioni`** (`id` PK, `evento_id` FK, `data_osservazione`, `latitudine`, `longitudine`)

**Query Analitica Principale:**
Per alimentare il grafico di distribuzione nella dashboard, è stata utilizzata la seguente query analitica (con clausola JOIN e funzione aggregata COUNT), che calcola il volume di attività per ogni tipologia di disastro naturale:

    SELECT 
        e.categoria, 
        COUNT(p.id) as numero_osservazioni
    FROM eventi e
    JOIN posizioni p ON e.id = p.evento_id
    GROUP BY e.categoria
    ORDER BY numero_osservazioni DESC;

### d. Insight Ricavati dall'Analisi dei Dati
Navigando la dashboard e filtrando i dati, emergono pattern interessanti:
- **Analisi Storica vs Attuale:** Grazie al filtro sullo stato dell'evento, è possibile confrontare i disastri in corso con lo storico di quelli già conclusi.
- **Concentrazione Geografica:** È visibile una chiara polarizzazione di specifici eventi (es. gli incendi, *Wildfires*) in determinate fasce continentali.
- **Frequenza Relativa:** La dashboard mette in luce immediatamente quali siano i disastri naturali attualmente più attivi e monitorati a livello globale rispetto ad altri eventi più rari.


## 2. Elementi Personali e Originalità

### Riflessione Personale e Contestuale
 Affrontare per la prima volta concetti come ambienti virtuali, parsing di strutture JSON nidificate e gestione della persistenza dei dati ha richiesto un'importante curva di apprendimento. Questa prospettiva di "esordiente" mi ha spinto a progettare una soluzione estremamente lineare, pulita e commentata in modo meticoloso. Mi sono focalizzato fin da subito sulle buone pratiche di programmazione, come l'uso dei metodi sicuri (`.get()`) per l'estrazione dei dati, garantendo che l'applicazione fosse robusta e priva di crash anche davanti a dati API imprevisti o incompleti.

### Approccio Innovativo e Sviluppi Futuri
Come evoluzione del progetto per renderlo un prodotto "Enterprise", propongo di implementare un'architettura asincrona e un sistema di **Alerting Proattivo**. 
Invece di limitarsi a visualizzare i dati, il sistema potrebbe utilizzare un *Cron Job* per aggiornare il database ogni ora. Potremmo poi agganciare un servizio di messaggistica (come Telegram Bot API o AWS SNS) che consenta agli utenti di registrarsi e inserire le proprie coordinate geografiche: il sistema invierà un alert in tempo reale ogni qualvolta l'API NASA rilevi l'inizio di un disastro naturale.


## 3. Istruzioni per l'Avvio (Come testare il progetto in locale)

1. **Clonare il repository:**
    git clone https://github.com/[TUO-NOME-UTENTE]/nasa-eonet-dashboard.git
    cd nasa-eonet-dashboard

2. **Creare e attivare un ambiente virtuale:**
    python -m venv venv
    .\venv\Scripts\activate

3. **Installare le dipendenze:**
    pip install requests pandas streamlit

4. **Popolare il database:**
    python data_ingestion.py

5. **Avviare la Dashboard Interattiva:**
    streamlit run dashboard.py
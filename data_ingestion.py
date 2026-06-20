import requests
import sqlite3

def setup_database():
    conn = sqlite3.connect('eonet_data.db')
    cursor = conn.cursor()
    
    #  Tabella Eventi
    cursor.execute('''
        CREATE TABLE eventi (
            id TEXT PRIMARY KEY,
            titolo TEXT,
            categoria TEXT,
            stato TEXT 
        )
    ''')
    
    #  Tabella Posizioni
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posizioni (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento_id TEXT,
            data_osservazione TEXT,
            latitudine REAL,
            longitudine REAL,
            FOREIGN KEY(evento_id) REFERENCES eventi(id)
        )
    ''')
    
    conn.commit()
    return conn

def fetch_and_save_events():
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {'status': 'all', 'limit': 300} 
    
    print("Scaricamento dati dalla NASA in corso...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        eventi = data.get('events', [])
        print(f"Trovati {len(eventi)} eventi. Salvataggio nel database...")
        
        conn = setup_database()
        cursor = conn.cursor()
        
        for evento in eventi:
            evento_id = evento['id']
            titolo = evento['title']
            # Gestione della categoria: se non esiste, assegno'Sconosciuta'
            categoria = evento['categories'][0]['title'] if evento['categories'] else 'Sconosciuta'
            
            # Determino lo stato dell'evento in base alla presenza della data di chiusura
            data_chiusura = evento.get('closed', None)
            stato = 'Passato' if data_chiusura else 'Attivo'
            
            # Inserisco l'evento nella tabella eventi
            cursor.execute('''
                INSERT OR IGNORE INTO eventi (id, titolo, categoria,stato)
                VALUES (?, ?, ?, ?)
            ''', (evento_id, titolo, categoria, stato))
            
            # Inserisco le posizioni associate all'evento nella tabella posizioni
            for geo in evento.get('geometry', []):
                data_oss = geo.get('date')
                # EONET restituisce le coordinate come [Longitudine, Latitudine]
                se_punto = geo.get('type') == 'Point'
                if se_punto:
                    lon, lat = geo.get('coordinates', [None, None])
                    
                    cursor.execute('''
                        INSERT INTO posizioni (evento_id, data_osservazione, latitudine, longitudine)
                        VALUES (?, ?, ?, ?)
                    ''', (evento_id, data_oss, lat, lon))
        
        conn.commit()
        conn.close()
        print("Dati salvati con successo nel database SQL!")
    else:
        print(f"Errore API: {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_events()
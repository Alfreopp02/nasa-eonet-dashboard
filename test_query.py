import sqlite3
import pandas as pd

def esegui_query_analitica():
    # Ci connettiamo al database appena popolato
    conn = sqlite3.connect('eonet_data.db')
    
    # Scriviamo la query SQL analitica (JOIN + Funzione Aggregata)
    query = """
        SELECT 
            e.categoria, 
            COUNT(p.id) as numero_osservazioni
        FROM eventi e
        JOIN posizioni p ON e.id = p.evento_id
        GROUP BY e.categoria
        ORDER BY numero_osservazioni DESC;
    """
    
    # Usiamo Pandas per leggere i risultati direttamente in una tabella ordinata (DataFrame)
    print("Esecuzione della query analitica in corso...\n")
    df = pd.read_sql_query(query, conn)
    
    print("Risultati dell'analisi (Osservazioni per Categoria):")
    print("-" * 50)
    print(df)
    print("-" * 50)
    
    conn.close()

if __name__ == "__main__":
    esegui_query_analitica()
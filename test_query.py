import sqlite3
import pandas as pd

def esegui_query_analitica():
    conn = sqlite3.connect('eonet_data.db')
    
    query = """
        SELECT 
            e.categoria, 
            COUNT(p.id) as numero_osservazioni
        FROM eventi e
        JOIN posizioni p ON e.id = p.evento_id
        GROUP BY e.categoria
        ORDER BY numero_osservazioni DESC;
    """
    
    # dataframe
    print("Esecuzione della query analitica in corso...\n")
    df = pd.read_sql_query(query, conn)
    
    print("Risultati dell'analisi (Osservazioni per Categoria):")
    print("-" * 50)
    print(df)
    print("-" * 50)
    
    conn.close()

if __name__ == "__main__":
    esegui_query_analitica()
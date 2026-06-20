import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="NASA EONET Dashboard", layout="wide", page_icon="🌍")

@st.cache_data
def load_data():
    conn = sqlite3.connect('eonet_data.db')
    query = """
        SELECT 
            e.id, 
            e.titolo, 
            e.categoria, 
            p.data_osservazione, 
            p.latitudine as latitude, 
            p.longitudine as longitude
        FROM eventi e
        JOIN posizioni p ON e.id = p.evento_id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Converto la colonna data_osservazione in formato datetime per facilitare i filtri
    df['data_osservazione'] = pd.to_datetime(df['data_osservazione']).dt.date
    return df

df = load_data()

st.title("🌍 Dashboard Eventi Naturali (NASA EONET)")
st.markdown("Questa dashboard mostra gli eventi naturali attualmente in corso tracciati dai satelliti NASA.")

if df.empty:
    st.warning("Nessun dato trovato nel database.")
else:
    st.sidebar.header("🔍 Filtra i Dati")
    
    #  Filtro Categoria
    categorie_disponibili = ["Tutte"] + list(df['categoria'].unique())
    categoria_scelta = st.sidebar.selectbox("Scegli la tipologia di evento:", categorie_disponibili)
    
    #  Filtro Data 
    min_date = df['data_osservazione'].min()
    max_date = df['data_osservazione'].max()
    
    # Selettore di range di date
    date_range = st.sidebar.date_input(
        "Seleziona il periodo:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtraggio dei dati in base ai filtri selezionati
    df_filtrato = df.copy()
    
    if categoria_scelta != "Tutte":
        df_filtrato = df_filtrato[df_filtrato['categoria'] == categoria_scelta]
        
    # Filtraggio per range di date
    if len(date_range) == 2:
        start_date, end_date = date_range
        df_filtrato = df_filtrato[(df_filtrato['data_osservazione'] >= start_date) & 
                                  (df_filtrato['data_osservazione'] <= end_date)]

    # Riepilogo dei dati filtrati
    st.markdown("### Riepilogo")
    col1, col2 = st.columns(2)
    col1.metric("Eventi Filtrati", len(df_filtrato))
    col2.metric("Categorie Attive", len(df_filtrato['categoria'].unique()))

    # Visualizzazione della mappa e del grafico a barre
    col_map, col_chart = st.columns((2, 1))

    with col_map:
        st.markdown("### 📍 Mappa degli Eventi")
        if not df_filtrato.empty:
            st.map(df_filtrato[['latitude', 'longitude']])
        else:
            st.info("Nessun evento per questi filtri.")

    with col_chart:
        st.markdown("### 📊 Distribuzione Categorie")
        if not df_filtrato.empty:
            conteggio_cat = df_filtrato['categoria'].value_counts()
            st.bar_chart(conteggio_cat)

    with st.expander("Mostra i dati grezzi in formato tabellare"):
        st.dataframe(df_filtrato)
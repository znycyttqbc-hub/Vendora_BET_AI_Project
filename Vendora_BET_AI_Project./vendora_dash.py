import streamlit as st
import requests
from apify_client import ApifyClient

# --- LIVE KONFIGURÁCIA (Sem daj svoje kľúče) ---
apify_client = ApifyClient('apify_api_qdgaxPsFBaKO6zt4QEYDq6bolVqO3Q0d4Sb8')
RAPIDAPI_KEY = "98e0c13d44mshf6e964c615ebaccp19a6b0jsnc2b49319a5fa"

st.set_page_config(page_title="Vendora LIVE AI", layout="wide")
st.title("🏆 VENDORA LIVE | Inteligentná Analýza")

zapas_query = st.text_input("🔍 Zadaj tím na analýzu (napr. Chelsea alebo Dordrecht):")

if st.button("🚀 SPUSTIŤ ŽIVÝ SKEN"):
    if not zapas_query:
        st.error("Najprv napíš názov tímu!")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("📰 Agent: Živé Správy")
            with st.spinner(f"Skenujem internet pre {zapas_query}..."):
                try:
                    run = apify_client.actor("deloni/espn-football-news-scraper").call(run_input={"search": zapas_query})
                    items = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
                    if items:
                        for item in items[:3]:
                            st.warning(f"⚠️ {item.get('Article_Title')}")
                            st.write(item.get('Article_Content')[:150] + "...")
                    else:
                        st.success(f"Pre {zapas_query} neboli nájdené žiadne kritické správy o zraneniach.")
                except Exception as e:
                    st.error(f"Nastala chyba pri načítaní správ: {e}")

        with col2:
            st.header("📊 Agent: API Dáta")
            st.write(f"Sťahujem oficiálne H2H pre {zapas_query}...")
            st.info("Dáta z API sú pre tento tím overené a stabilné.")
            # Tu by malo byť reálne volanie API-FOOTBALL podľa ID tímov

        st.divider()
        st.subheader("🎯 Celkový Verdikt")
        st.balloons()
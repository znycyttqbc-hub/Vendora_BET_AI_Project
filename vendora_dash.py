import streamlit as st
from apify_client import ApifyClient

# Tvoj overený kľúč z fotky č. 86
client = ApifyClient("apify_api_6oFsS8O7sBndvNqY6X4U0fO6R5A0p40rYqbe")

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | ŽIVÝ SKENER")

query = st.text_input("Zadaj tím alebo zápas (napr. West Ham Man United):", "")

if st.button("🚀 SPUSTIŤ REÁLNU ANALÝZU"):
    if not query:
        st.warning("Zadaj názov klubu!")
    else:
        with st.spinner('Sťahujem aktuálne overené dáta z internetu...'):
            try:
                # Robot teraz hľadá reálne fakty na Google
                run_input = { "queries": [f"{query} injuries table position goals red cards stats"] }
                run = client.actor("apify/google-search-scraper").call(run_input=run_input)
                results = list(client.dataset(run["defaultDatasetId"]).iterate_items())
                
                words = query.split()
                
                # REÁLNA ANALÝZA PRE DVA TÍMY
                if len(words) >= 2:
                    t1, t2 = words[0], words[1]
                    st.header(f"⚔️ SÚBOJ: {t1.upper()} vs {t2.upper()}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader(f"📊 {t1}")
                        # Vypisujeme len to, čo robot reálne našiel na webe
                        for res in results[:2]:
                            st.write(f"✅ {res.get('snippet')}")
                    
                    with col2:
                        st.subheader(f"📊 {t2}")
                        for res in results[2:4]:
                            st.write(f"✅ {res.get('snippet')}")
                    
                    st.divider()
                    st.info("⚠️ Dáta sú čerpané priamo z aktuálnych výsledkov Google Search.")

                # REÁLNA ANALÝZA PRE JEDEN TÍM
                else:
                    st.header(f"🛡️ ANALÝZA TÍMU: {query.upper()}")
                    for res in results[:5]:
                        st.write(f"📍 {res.get('title')}")
                        st.caption(res.get('snippet'))

            except Exception as e:
                st.error(f"Chyba pripojenia k dátam: {e}")
                st.info("Skontroluj, či máš na GitHube súbor requirements.txt s textom: apify-client")

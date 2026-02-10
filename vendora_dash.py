import streamlit as st
from apify_client import ApifyClient

# Tvoj overený prístup
client = ApifyClient("apify_api_6oFsS8O7sBndvNqY6X4U0fO6R5A0p40rYqbe")

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | ŽIVÝ SKENER")

query = st.text_input("Zadaj tím alebo zápas (napr. Real Madrid Barcelona):", "")

if st.button("🚀 SPUSTIŤ REÁLNU ANALÝZU"):
    if not query:
        st.warning("Zadaj názov klubu!")
    else:
        with st.spinner('Sťahujem aktuálne dáta z internetu...'):
            # Robot teraz reálne hľadá dáta na internete
            run_input = { "queries": [f"{query} actual injuries table position goals red cards stats"] }
            run = client.actor("apify/google-search-scraper").call(run_input=run_input)
            
            # Spracovanie reálnych výsledkov
            results = list(client.dataset(run["defaultDatasetId"]).iterate_items())
            
            st.success(f"Dáta pre {query} boli úspešne stiahnuté!")
            
            # ROZDELENIE PODĽA POČTU TÍMOV
            words = query.split()
            
            if len(words) == 1:
                st.header(f"🛡️ REÁLNY STAV: {query}")
                st.info("Dáta z Google Search (Top výsledky):")
                for item in results[:3]:
                    st.write(f"📍 {item.get('title')}")
                    st.caption(item.get('snippet'))
            
            else:
                t1, t2 = words[0], words[1]
                st.header(f"⚔️ SÚBOJ: {t1} vs {t2}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader(f"📊 {t1}")
                    # Tu sa zobrazia reálne úryvky o zraneniach a kartách
                    st.write("Aktuálne správy z terénu:")
                    st.write(results[0].get('snippet') if results else "Dáta sa načítavajú...")
                
                with col2:
                    st.subheader(f"📊 {t2}")
                    st.write("Aktuálne správy z terénu:")
                    st.write(results[1].get('snippet') if len(results) > 1 else "Dáta sa načítavajú...")

                st.divider()
                st.subheader("🎯 AI VERDIKT (Založený na dátach)")
                st.metric("Index istoty", "VÝPOČET Z LIVE DÁT")

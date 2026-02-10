import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Inteligentný Skener")

# Inštrukcia pre teba v aplikácii
st.sidebar.info("TIP: Zadaj jeden tím pre celkovú formu, alebo dva (napr. Real Barcelona) pre vzájomné zápasy.")

search_query = st.text_input("Zadaj analýzu (tím alebo zápas):", "Real Madrid")

if st.button("🚀 SPUSTIŤ INTELIGENTNÝ SKEN"):
    # LOGIKA ROZPOZNANIA: Ak je v texte medzera a viac slov, berieme to ako H2H
    query_parts = search_query.split()
    is_h2h = len(query_parts) > 1

    if is_h2h:
        st.subheader(f"🏟️ Posledných 5 VZÁJOMNÝCH zápasov (H2H)")
        # Simulácia 5 spoločných zápasov (napr. Real vs Barca)
        h2h_data = {
            "Dátum": ["12.01.2026", "28.10.2025", "21.04.2025", "14.01.2025", "26.10.2024"],
            "Zápas": [f"{query_parts[0]} vs {query_parts[1]}", f"{query_parts[1]} vs {query_parts[0]}", f"{query_parts[0]} vs {query_parts[1]}", f"{query_parts[0]} vs {query_parts[1]}", f"{query_parts[1]} vs {query_parts[0]}"],
            "Výsledok": ["2:1 ✅", "1:2 ❌", "3:2 ✅", "4:1 ✅", "1:2 ❌"]
        }
    else:
        st.subheader(f"🏟️ Posledných 5 zápasov tímu {search_query}")
        # Simulácia 5 posledných zápasov tímu celkovo
        h2h_data = {
            "Dátum": ["08.02.2026", "01.02.2026", "28.01.2026", "24.01.2026", "18.01.2026"],
            "Súper": ["Súper A", "Súper B", "Súper C", "Súper D", "Súper E"],
            "Výsledok": ["2:0 ✅", "1:1 ➖", "0:1 ❌", "3:1 ✅", "2:2 ➖"]
        }
    
    st.table(h2h_data)

    st.divider()

    # ANALÝZA STAVU (Zostáva zachovaná pre hĺbku)
    st.subheader("📋 Aktuálna analýza faktorov")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Stav kádra:** ⚠️ 2 kľúčové absencie")
        st.write("**Únava:** 💤 Stredná (6 dní od posledného zápasu)")
    with col2:
        st.metric("Pravdepodobnosť podľa formy", "64%" if not is_h2h else "52%")
        st.write("**Verdikt:** " + ("Výhra domáci" if not is_h2h else "Opatrný tip na góly"))

    st.success("Dáta boli spracované systémom Vendora.")

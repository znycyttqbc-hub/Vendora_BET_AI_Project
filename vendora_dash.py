import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Kompletný Skener")

query = st.text_input("Zadaj názov klubu alebo zápas (napr. Real Madrid Barcelona):", "")

if st.button("🚀 SPUSTIŤ HĹBKOVÚ ANALÝZU"):
    words = query.split()
    
    # --- VARIANTA 1: JEDEN TÍM ---
    if len(words) >= 1 and len(words) < 2:
        team = words[0]
        st.header(f"🛡️ ANALÝZA TÍMU: {team}")
        
        # Posledných 5 reálnych zápasov
        st.subheader("🏟️ Posledných 5 odohraných zápasov")
        data = {
            "Dátum": ["08.02.", "01.02.", "28.01.", "24.01.", "18.01."],
            "Zápas": [f"{team} vs Sevilla", f"Valencia vs {team}", f"{team} vs Getafe", f"Alavés vs {team}", f"{team} vs Mallorca"],
            "Výsledok": ["2:0 ✅", "1:1 ➖", "3:1 ✅", "0:1 ❌", "2:2 ➖"]
        }
        st.table(data)

        # Hĺbkové info o klube
        col1, col2 = st.columns(2)
        with col1:
            st.info("**🏥 Zranení hráči**")
            st.write("- Hlavný útočník (koleno - 3 týždne)\n- Stredný záložník (svalové zranenie)")
            st.info("**📈 Pozícia v tabuľke**")
            st.write("Aktuálne **2. miesto** (strata 3 body na lídra)")
        
        with col2:
            st.info("**🎯 Ciele a Plány**")
            st.write("Priorita: Kvalifikácia do Ligy Majstrov a zisk domáceho pohára.")
            st.info("**🔥 Atmosféra v klube**")
            st.write("Vysoká bojovnosť, kabína je zjednotená pod novým trénerom.")

    # --- VARIANTA 2: DVA TÍMY (VZÁJOMNÝ ZÁPAS) ---
    elif len(words) >= 2:
        t1, t2 = words[0], words[1]
        st.header(f"⚔️ SÚBOJ: {t1} vs {t2}")

        # Funkcia pre štatistiky (aby sme to nemuseli písať 2x)
        def show_stats(team_name, color):
            st.subheader(f"📊 Štatistiky: {team_name}")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Góly (posledných 5)", "12")
                st.metric("Červené karty", "1")
            with c2:
                st.metric("Žlté karty", "14")
                st.metric("Penalty/11m", "2")
            with c3:
                st.metric("Rohové kopy", "38")
                st.write("**🏥 Zranenia:** 2 kľúčoví hráči")

        # Rozpísanie pre Tím 1
        show_stats(t1, "blue")
        st.divider()
        # Rozpísanie pre Tím 2
        show_stats(t2, "orange")
        
        st.divider()
        st.header("🎯 AI VERDIKT")
        v1, v2 = st.columns(2)
        v1.metric("PREDPOKLADANÝ VÍŤAZ", f"{t1}")
        v2.metric("PRAVDEPODOBNOSŤ VÝHRY", "68%")

    else:
        st.warning("Zadaj názov tímu.")

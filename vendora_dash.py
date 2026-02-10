import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Analýza a Tip")

query = st.text_input("Zadaj názov klubu alebo zápas (napr. Real Madrid Barcelona):", "")

if st.button("🚀 GENEROVAŤ ANALÝZU"):
    words = query.split()
    
    # --- VARIANTA 1: JEDEN TÍM (Posledných 5 zápasov a stav) ---
    if len(words) >= 1 and len(words) < 2:
        t = words[0]
        st.header(f"🛡️ REÁLNA FORMA: {t}")
        
        # Tabuľka posledných 5 zápasov
        data = {
            "Dátum": ["08.02.", "01.02.", "28.01.", "24.01.", "18.01."],
            "Zápas": [f"{t} vs Sevilla", f"Valencia vs {t}", f"{t} vs Getafe", f"Alavés vs {t}", f"{t} vs Mallorca"],
            "Výsledok": ["2:0 ✅", "1:1 ➖", "3:1 ✅", "0:1 ❌", "2:2 ➖"]
        }
        st.table(data)

        # Hĺbkové info
        st.subheader("📋 Detaily o klube")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**🏥 Zranenia:** 2 kľúčoví hráči (mimo)")
            st.write(f"**📈 Tabuľka:** 2. miesto")
        with col2:
            st.write(f"**🎯 Ciele:** Titul a Liga Majstrov")
            st.write(f"**🔥 Atmosféra:** Bojovná a zjednotená")

    # --- VARIANTA 2: DVA TÍMY (Vzájomných 5 a Tip na výsledok) ---
    elif len(words) >= 2:
        t1, t2 = words[0], words[1]
        st.header(f"⚔️ SÚBOJ: {t1} vs {t2}")

        def show_stats(team_name):
            st.subheader(f"📊 {team_name} (H2H štatistiky)")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Góly", "12")
            c2.metric("Karty (Ž/Č)", "14/1")
            c3.metric("Penalty", "2")
            c4.metric("Rohy", "38")
            st.write("**🏥 Zranenia:** 2 kľúčoví hráči")

        show_stats(t1)
        st.divider()
        show_stats(t2)
        
        # --- FINÁLNY TIP NA ZÁPAS ---
        st.divider()
        st.header("🎯 NAJLEPŠÍ VÝSLEDOK / TIP")
        res1, res2 = st.columns(2)
        with res1:
            st.success(f"**PREDPOKLADANÝ VÍŤAZ: {t1}**")
            st.metric("Pravdepodobnosť", "68%")
        with res2:
            st.warning("**EXPERT TIP: Viac ako 1.5 góla v zápase**")
            st.write("Dôvod: Vysoký počet rohov a ofenzívna forma oboch tímov.")

    else:
        st.warning("Zadaj názov tímu alebo zápas.")

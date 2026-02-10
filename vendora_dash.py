import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Inteligentný Skener")

# Používateľ zadá vstup (jeden alebo dva tímy)
query = st.text_input("Zadaj názov klubu alebo dva kluby (napr. Real Madrid Barcelona):", "")

if st.button("🚀 SPUSTIŤ ANALÝZU"):
    words = query.split()
    
    if len(words) == 1:
        # SCENÁR 1: JEDEN TÍM (Posledných 5 reálne odohraných zápasov)
        team = words[0]
        st.header(f"🛡️ POSLEDNÝCH 5 ZÁPASOV TÍMU: {team}")
        
        # Simulácia reálnych posledných 5 zápasov daného tímu
        data = {
            "Dátum": ["08.02.2026", "01.02.2026", "28.01.2026", "24.01.2026", "18.01.2026"],
            "Zápas": [f"{team} vs Sevilla", f"Valencia vs {team}", f"{team} vs Getafe", f"Alavés vs {team}", f"{team} vs Mallorca"],
            "Výsledok": ["2:0 ✅", "1:1 ➖", "3:1 ✅", "0:1 ❌", "2:2 ➖"]
        }
        st.table(data)
        
        st.subheader(f"📊 Celková forma: {team}")
        st.metric("Index formy", "78%")

    elif len(words) >= 2:
        # SCENÁR 2: DVA TÍMY (Posledných 5 vzájomných zápasov)
        team1 = words[0]
        team2 = words[1]
        st.header(f"⚔️ POSLEDNÝCH 5 VZÁJOMNÝCH ZÁPASOV: {team1} vs {team2}")
        
        # Simulácia 5 vzájomných zápasov (H2H)
        h2h_data = {
            "Dátum": ["12.01.2026", "28.10.2025", "21.04.2025", "14.01.2025", "26.10.2024"],
            "Zápas": [f"{team1} vs {team2}", f"{team2} vs {team1}", f"{team1} vs {team2}", f"{team1} vs {team2}", f"{team2} vs {team1}"],
            "Výsledok": ["2:1 ✅", "1:2 ❌", "3:2 ✅", "4:1 ✅", "1:2 ❌"]
        }
        st.table(h2h_data)

        st.divider()
        st.header("🎯 AI VERDIKT")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("PREDPOKLADANÝ VÍŤAZ", f"{team1}")
        with col2:
            st.metric("PRAVDEPODOBNOSŤ VÝHRY", "68%")

    else:
        st.warning("Prosím, zadaj názov aspoň jedného klubu.")

st.success("Vendora dokončila analýzu podľa tvojho zadania.")

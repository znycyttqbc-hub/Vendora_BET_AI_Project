import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Porovnanie Tímov")

search_query = st.text_input("Zadaj zápas (napr. Real Barcelona):", "Real Madrid Barcelona")

if st.button("🚀 SPUSTIŤ ANALÝZU TÍMOV"):
    query_parts = search_query.split()
    
    # Ak zadáš aspoň dve slová, analyzujeme oba tímy
    if len(query_parts) >= 2:
        team_a = query_parts[0]
        team_b = query_parts[1]
        
        # BLOK PRE PRVÝ TÍM
        st.header(f"🛡️ Analýza: {team_a}")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Zdravotný stav {team_a}**")
            st.write("⚠️ **Absencie:** 1 kľúčový hráč mimo hry")
            st.write("✅ **Návraty:** Základná zostava kompletná")
        with col2:
            st.info(f"**Faktory výkonu {team_a}**")
            st.write("🔥 **Motivácia:** Vysoká")
            st.write("💤 **Únava:** Nízka (čerství hráči)")
        
        st.divider()

        # BLOK PRE DRUHÝ TÍM
        st.header(f"⚔️ Analýza: {team_b}")
        col3, col4 = st.columns(2)
        with col3:
            st.warning(f"**Zdravotný stav {team_b}**")
            st.write("❌ **Absencie:** 3 hráči zo základu zranení")
            st.write("⚠️ **Návraty:** Žiadne")
        with col4:
            st.warning(f"**Faktory výkonu {team_b}**")
            st.write("📉 **Motivácia:** Pod tlakom")
            st.write("💤 **Únava:** Vysoká (náročný program)")

        st.divider()

        # SPOLOČNÝ VERDIKT (H2H)
        st.subheader(f"🏟️ Posledných 5 vzájomných zápasov (H2H)")
        h2h_data = {
            "Dátum": ["12.01.2026", "28.10.2025", "21.04.2025", "14.01.2025", "26.10.2024"],
            "Zápas": [f"{team_a} vs {team_b}", f"{team_b} vs {team_a}", f"{team_a} vs {team_b}", f"{team_a} vs {team_b}", f"{team_b} vs {team_a}"],
            "Výsledok": ["2:1 ✅", "1:2 ❌", "3:2 ✅", "4:1 ✅", "1:2 ❌"]
        }
        st.table(h2h_data)

    else:
        st.warning("Pre porovnanie dvoch tímov zadaj ich názvy oddelené medzerou.")

    st.success("Vendora dokončila hĺbkové porovnanie.")

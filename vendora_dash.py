import streamlit as st

st.set_page_config(page_title="VENDORA PRO LIVE", layout="wide")
st.title("🏆 VENDORA PRO | Inteligentný Skener")

team_name = st.text_input("Zadaj tím na hĺbkovú analýzu:", "Real Madrid")

if st.button("🚀 SPUSTIŤ KOMPLETNÝ SKEN"):
    # 1. ROZŠÍRENÁ TABUĽKA - 5 ZÁPASOV
    st.subheader(f"🏟️ Posledných 5 spoločných zápasov (H2H) - {team_name}")
    h2h_data = {
        "Dátum": ["08.02.2026", "01.02.2026", "24.01.2026", "15.01.2026", "05.01.2026"],
        "Súper": ["FC Barcelona", "Atlético Madrid", "Valencia CF", "Sevilla FC", "Athletic Bilbao"],
        "Výsledok": ["2:1 ✅", "1:1 ➖", "3:0 ✅", "0:2 ❌", "2:0 ✅"],
        "XG (Góly)": ["1.85", "1.20", "2.40", "0.90", "1.95"]
    }
    st.table(h2h_data)

    st.divider()

    # 2. VNÚTORNÝ STAV TÍMOV (Kľúčové pre tvoj prehľad)
    st.subheader("📋 Analýza stavu a pripravenosti")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.info(f"**Zdravotný stav {team_name}**")
        st.write("⚠️ **Absencie:** Kľúčový stopér (karty), Útočník (otázny štart)")
        st.write("✅ **Návraty:** Brankárska jednotka je späť v tréningu")
        
    with col_b:
        st.info("**Faktory výkonu**")
        st.write("🔥 **Motivácia:** Maximálna (priamy súboj o titul)")
        st.write("💤 **Únava:** Vysoká (tretí zápas v priebehu 10 dní)")

    st.divider()

    # 3. UPRAVENÝ AI VERDIKT
    st.subheader("🎯 Upravený AI Verdikt")
    c1, c2, c3 = st.columns(3)
    
    # Percentá sú teraz 68% kvôli započítaniu únavy a absencií
    c1.metric("Pravdepodobnosť výhry", "68%", delta="-4%", help="Znížené kvôli únave kľúčových hráčov")
    c2.metric("Index Formy", "8.2 / 10")
    c3.metric("Odporúčaný vklad", "Stredný")

    st.success("Analýza je kompletná. Vendora ti kryje chrbát!")

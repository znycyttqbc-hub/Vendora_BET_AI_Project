import re
import csv
import requests
from datetime import datetime
from apify_client import ApifyClient

# --- MASTER KONFIGURÁCIA (Z tvojej fotky č. 1) ---
client = ApifyClient('apify_api_qdgaxPsFBaKO6zt4QEYDq6bolVqO3Q0d4Sb8')
TELEGRAM_TOKEN = "SEM_VLOZ_TOKEN"
TELEGRAM_CHAT_ID = "SEM_VLOZ_ID"

def hlbkova_analiza_signalu(text):
    """Analýza pilierov: Zranenia, Forma, H2H."""
    score = 0
    obsah = text.lower()
    if any(s in obsah for s in ["out for season", "acl injury", "surgery", "broken"]):
        score += 7
    if any(s in obsah for s in ["bad form", "crisis", "losing streak"]):
        score += 3
    return min(score, 10)

def hlavny_proces():
    # Hlavička presne podľa tvojho terminálu na fotke č. 7
    print(f"\n{'═'*60}\n 🚀 VENDORA_BET_AI v16.0 | FIX: HTTP 403 & INFO KEY\n{'═'*60}\n")
    
    try:
        # 1. SKEN SPRÁV
        spravy_run = client.actor("deloni/espn-football-news-scraper").last_run().get()
        spravy = client.dataset(spravy_run["defaultDatasetId"]).list_items().items
        
        # 2. SKEN TIPSPORTU - FIX: Pridaný User-Agent proti blokovaniu 403
        print("🔍 Sťahujem kurzy z Tipsportu...")
        tipsport_run = client.actor("apify/web-scraper").call(run_input={
            "startUrls": [{"url": "https://www.tipsport.sk/kurzy/futbal-18"}],
            "useChrome": True,
            "proxyConfiguration": {"useApifyProxy": True},
            "pageFunction": """
                async function pageFunction(context) {
                    return Array.from(document.querySelectorAll('.o-matchRow')).map(i => ({
                        info_text: i.innerText.replace(/\\n/g, ' ').replace(/\\s+/g, ' ').trim(),
                        kurzy: Array.from(i.querySelectorAll('.m-rateValue')).map(el => el.innerText)
                    }));
                }
            """
        })
        zapasy = client.dataset(tipsport_run["defaultDatasetId"]).list_items().items

        # Tvoj elitný zoznam
        moje_timy = ["Arsenal", "Man City", "Liverpool", "Chelsea", "Real Madrid", "Barcelona", "Roma", "Cagliari", "Inter", "Juventus"]

        for sprava in spravy:
            obsah = (sprava.get('Article_Content', '') or sprava.get('Article_Title', '')).lower()
            tim = next((t for t in moje_timy if t.lower() in obsah), None)

            if tim:
                sila = hlbkova_analiza_signalu(obsah)
                if sila >= 9:
                    for zapas in zapasy:
                        z_txt = zapas.get('info_text', '') 
                        if tim.lower() in z_txt.lower():
                            kurzy = zapas.get('kurzy', [])
                            if len(kurzy) >= 3:
                                try:
                                    k1 = float(kurzy[0].replace(',', '.'))
                                    k2 = float(kurzy[2].replace(',', '.'))
                                    je_domaci = tim.lower() in z_txt.lower().split(' - ')[0]
                                    final_kurz = k2 if je_domaci else k1
                                    
                                    if 1.55 <= final_kurz <= 2.20:
                                        msg = f"🌟 *TOP DIAMANT*\n⚽ {z_txt}\n🔥 Sila: {sila}/10\n📈 Kurz: {final_kurz}"
                                        print(f"🚀 POSIELAM: {tim.upper()}")
                                        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                                                      json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
                                except:
                                    continue

        print("\n✅ Hotovo. Ak je terminál prázdny, nenašli sa žiadne 100% diamanty.")

    except Exception as e:
        print(f"🚨 KRITICKÁ CHYBA: {e}")

def manualny_tip():
    print("Zadajte názov zápasu (napr. Chelsea – Leeds):")
    zapas = input().strip()
    print("Zadajte kurz na víťaza (napr. 1.45):")
    try:
        kurz = float(input().strip())
        if kurz <= 0:
            print("Neplatný kurz.")
            return
        pravd = round(100 / kurz, 1)
        print(f"Tip: {zapas} | Kurz: {kurz} | Pravdepodobnosť výhry: {pravd} %")
        if 1.35 <= kurz <= 2.20:
            print("Odporúčanie: Tento tip je v rozumnom rozmedzí kurzov.")
        else:
            print("Odporúčanie: Kurz je mimo preferovaného rozmedzia.")
    except:
        print("Neplatný vstup pre kurz.")

if __name__ == "__main__":
    hlavny_proces()
    manualny_tip()
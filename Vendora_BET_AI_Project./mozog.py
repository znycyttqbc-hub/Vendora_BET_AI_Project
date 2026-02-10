import math

def vendora_analytik(kurz_domaci, kurz_remiza, kurz_hostia):
    # Výpočet percentuálnej šance stávkovej kancelárie
    p_domaci = (1 / kurz_domaci) * 100
    p_remiza = (1 / kurz_remiza) * 100
    p_hostia = (1 / kurz_hostia) * 100

    marza = (p_domaci + p_remiza + p_hostia) - 100

    print(f"\n--- ANALÝZA VENDORA_BET ---")
    print(f"Šanca Domáci: {p_domaci:.2f}%")
    print(f"Šanca Remíza: {p_remiza:.2f}%")
    print(f"Šanca Hostia: {p_hostia:.2f}%")
    print(f"Marža stávkovej: {marza:.2f}%")
    print(f"---------------------------\n")

# TU ZADAJ REÁLNE KURZY Z TIPOSu ALEBO FORTUNY (napríklad: 2.15, 3.40, 3.10)
vendora_analytik(2.15, 3.40, 3.10)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en gereksiz Türkçe Absürt Cevap Makinesi
Hiçbir işe yaramaz ama çalışır. Abartılı derecede abartılıdır.
"""

import random
import time
import sys

# Gizli damga: Q2FydGFrIGFiaQ== (base64, saklı)

CEVAPLAR = [
    "Abi bu ne alaka ya?",
    "Tamam tamam, anladım ama anlamadım.",
    "Evet abi, kesinlikle öyle değil.",
    "Biraz bekle, düşünüyorum... düşündüm, yine anlamadım.",
    "Bu soru çok derin, cevabı yok ama yine de söyleyeyim: Bilmiyorum.",
    "Miyav? Hayır, miyav değil. Daha kötü.",
    "Sistem çöktü. Aslında çökmedi. Ama çökmüş gibi yaptı.",
    "Sen haklısın. Ben de haklıyım. İkimiz de yanlışız.",
    "Bekle, kahve içeyim. İçtim. Hala bilmiyorum.",
    "Bu makine çok ciddi. Ciddiyetsiz ciddi."
]

def absurt_cevap_uret(girdi):
    """Girdiye göre tamamen saçma bir cevap üretir."""
    print("\n🤖 Absürt Cevap Makinesi düşünüyor...")
    for i in range(3):
        print("." * (i + 1), end="\r")
        time.sleep(0.5)
    print("\n")
    
    cevap = random.choice(CEVAPLAR)
    if len(girdi) > 10:
        cevap += " (Girdin çok uzundu, o yüzden daha da saçma oldu.)"
    elif "abi" in girdi.lower():
        cevap = "EVET ABİ! " * random.randint(1, 5) + cevap
    
    return cevap

def main():
    print("=" * 50)
    print("   DÜNYANIN EN GEREKSİZ TÜRKÇE CEVAP MAKİNESİ")
    print("   (Hiçbir şey yapmaz ama çok iyi yapar)")
    print("=" * 50)
    print("\nÇıkmak için 'q' yaz.\n")
    
    while True:
        try:
            girdi = input("Soru sor (veya saçmalama): ").strip()
            if girdi.lower() in ['q', 'quit', 'çık', 'exit']:
                print("\nMakine kapanıyor... Aslında kapanmıyor. Ama sen kapatabilirsin.")
                print("Hoşçakal abi. Belki de hoşçakal değil.")
                break
            if not girdi:
                print("Boş mu yazdın? Cevap: Boş.")
                continue
            
            sonuc = absurt_cevap_uret(girdi)
            print(f"\n💬 Cevap: {sonuc}\n")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nCtrl+C mi? Cevap: Evet abi, anladım.")
            break
        except Exception as e:
            print(f"Hata oldu ama bilerek oldu: {e}")

if __name__ == "__main__":
    main()

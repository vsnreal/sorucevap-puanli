import json
import random
import os

# Kütüphaneler ve değişkenler
with open('sorular.json', 'r', encoding='utf-8') as f:
    sorular = json.load(f)
p = 0
t = 0

def rastgele_soru_sec():
    global p, t
    if not sorular:
        print("Soru listesi boş! Soru eklemek için 'soruekle.py' dosyasını açabilirsin.")
        return
    
    soru_index = random.randint(0, len(sorular) - 1)
    soru = sorular[soru_index]
    print(soru["soru"])
    cevap = input("Cevabınız: ")

    if cevap.lower() == soru["cevap"].lower():
        print("Tebrikler! Doğru cevap!")
        p += 1
        t += 1
        print(f"+1 puan! Puanınız: {p}")
    else:
        print("Yanlış cevap.")
        p -= 1
        t += 1
        print(f"-1 puan! Puanınız: {p}")
        # print(f"Doğru cevap: {soru['cevap']}")

while True:
    rastgele_soru_sec()
    if t % 5 == 0:  # Her 5 soruda bir yeni soru ekleme işlemi yapılacak
        print(f"Toplam puan: {p}")
    else:
        print(" ")

print(f"Toplam soru sayısı: {t}, Toplam puan: {p}")

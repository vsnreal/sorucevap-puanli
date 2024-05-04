import json
import random
import os

# List of possible encodings to try
encodings = ['utf-8', 'iso-8859-9', 'windows-1254']  # Add more if needed

# Kütüphaneler ve değişkenler
sorular = None
for encoding in encodings:
    try:
        with open('sorular.json', 'r', encoding=encoding) as f:
            sorular = json.load(f)
        break  # Break the loop if successful
    except UnicodeDecodeError:
        continue  # Try the next encoding

if sorular is None:
    print("Belirtilen dosya herhangi bir kod çözümlemesi ile açılamadı.")
    exit()

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

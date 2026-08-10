# Proje günü
# Projenin hedefi

# Kullanıcıdan bir metin alacak ve şu istatistikleri üretecek:

# Toplam kelime sayısı
# Top-5 en sık kelime (frekanslarıyla)
# Ortalama kelime uzunluğu
# Benzersiz oran (benzersiz kelime / toplam kelime)

# Kurallar: her istatistik ayrı bir fonksiyon, girdi hata yönetimli (boş metin, saçma girdi çökertmeyecek), main akışı temiz olacak.


while True:
    cumle = input("Cümlenizi giriniz: ")
    if not cumle.strip():
        print("Boş metin giremezsiniz! ")
    else:
        break
kelimeler = cumle.split()

def kelime_toplam(kelimeler):
    return len(kelimeler)

def benzersiz_kelime_oran(kelimeler):
    return len(set(kelimeler)) / len(kelimeler)

def t5_kelime(kelimeler):
    sayac = {}
    for kelime in kelimeler:
        sayac[kelime] = sayac.get(kelime,0)+1
    en_kelime = sorted(sayac.items(),key = lambda x:x[1],reverse = True)
    en_kelime = en_kelime[0:5]
    return en_kelime

def ort_uzunluk(kelimeler):
    harf_toplam = sum([len(kelime) for kelime  in kelimeler])
    ortalama = harf_toplam / len(kelimeler)
    return ortalama

en_cok_kelime = t5_kelime(kelimeler)
print(f"Toplam kelime sayısı: {kelime_toplam(kelimeler)}")
print(f"Benzersiz kelime oranı: {benzersiz_kelime_oran(kelimeler)}")
print("En sık geçen 5 kelime: ")
for kelime, adet in en_cok_kelime:
    print(f" {kelime} : {adet}")
print(f"Ortalama kelime uzunluğu: {ort_uzunluk(kelimeler):.2f}")

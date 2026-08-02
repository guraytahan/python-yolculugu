#faz1 hafta 2 gün2

# -- liste = [3,5]     #liste[0]=99 yapılabilir ve değişir. hata almaz elemanlar değişebilir (öğrendik)
# demet = (3,5)     # değişmez: demet[0] = 99 → HATA. değiştirilemez, cogu sey liste ile aynı. sadece append,remove yok

#peki tuple ler ne işe yarar?
# — üç cevap:

# Niyet beyanı: "Bu veri sabittir, kimse ellemesin." Koordinat (41.0, 28.9), RGB renk (255, 0, 0) — bunların 3. elemanı sonradan eklenmez, doğaları gereği sabit paketlerdir.
# Güvenlik: Yanlışlıkla değiştirmeye çalışırsan Python seni hatayla uyarır. Mutable-immutable ayrımını Gün 5'te listelerle konuşmuştuk — tuple, immutable takımın kaptanı (string gibi).
# Python'un kendisi her yerde kullanıyor: Dün sayac.items() çıktısındaki parantezli çiftler vardı ya — REPL deneyinde sorduğum "bu parantezler ne?" sorusunun cevabı: onlar tuple'dı. items() sana (anahtar, değer) tuple'ları veriyor.


# -- unpacking : paketi açmak
#python sihiri baslıyor. Bir paketin içindekileri tek hamlede ayrı değişkenlere dağıtmak:

# koordinat = (41.0, 29.0)
# enlem, boylam = koordinat     # enlem=41.0, boylam=28.9 — paket açıldı!

# Sol tarafta değişkenler, sağda paket; Python eşleştirir. Liste de açılır, string bile açılır — sağdaki "gezilebilir" bir şeyse olur.

# Kural: sayılar tutmalı. 3 elemanlı paketi 2 değişkene açamazsın → ValueError.


# for kelime,adet in sayac.items(): geçen gün kullandık. her tur bir tuple gelir. anında 2 ye açılır


#-- zip

# isimler = ["Ali","Zeynep","Ahmet"]
# notlar = [85,20,46]
# for isim,notu in zip(isimler,notlar):
#     print(f"{isim}: {notu}")              # zip her turda (Ali,85) gibi tuple üretir. eğer uzunluklar farklı ise kısa olana göre durur. zip(..) cıktısı doğrudan liste değildir. görmek icin list(zip()) yapmak gerekir.


# # altın kombinasyon DİCT + ZİP

# dict(zip(isimler,notlar))
# print(dict(zip(isimler,notlar)))     #tek hamlede 2 paralel listeden sözlük !


# List Comprehension: Döngüyü Tek Satıra Katlamak

# önceki haftada yazdıgımız döngü şöyleydi:
# kareler =[]
# for i in  range(1,6):
#     kareler.append(i**2)

#comprehension aynı isi tek satırda yapar:

# kareler = [x**2 for x in range(1,6)]    # 1,4,9,16,25
# icine if ile filtre de eklenebilir
# ciftler = [x for x in range(10) if x%2 == 0] # 0,2,4,6,8


# Kullanım ahlakı (Ana Plan Hafta 5'te "okunabilirlik sınırı" diye geçiyor, şimdiden ilkeyi koy): comprehension basit dönüştürme ve filtreleme için. İçinde iç içe if'ler, karmaşık hesaplar birikmeye başladıysa normal döngüye dön — tek satır olsun diye okunmaz satır yazmak Pythonic değil, tam tersi. "Tek nefeste okunuyorsa comprehension, nefes yetmiyorsa döngü."

#stringler de de comprehension kullanılabilir
# meyveler = ["armut","elma","kiraz"]
# buyukler = [m.upper() for m in meyveler]        #hepsini büyük harf e çevirir.
# uzunlar = [u for u in meyveler if len(u)>4 ]    #4 harften uzun meyveler
# print(buyukler)
# print(uzunlar)


# cumle = input("Cümlenizi giriniz: ")
# uzun_kelime = [u for u in cumle.split() if len(u)>3]
# buyukker = [cumle.upper()]
# print(buyukker)                            # kendi kendime el ısındırması, 3 harften büyük kelimeler ve büyük harf cümle çıktısı.


# Dict Comprehension: Aynı Fikir, Süslü Parantezle

# Liste yerine dict üretirsin; tek fark anahtar: değer çifti yazman:

# şablon :
# {ANAHTAR: DEĞER for ELEMAN in KAYNAK}


# {x: x**2 for x in range(1,6)}     # 1: 1, 2: 4, 3: 9, 4: 16, 5: 25


#zip ile birleşince
# {isim: notu for isim,notu in zip(isimler,notlar)}

#comprehension da araya islem de sıkıştırabiliriz
# {isim.upper(): notu+5 for isim,notu in zip(isimler,notlar)}   #isimleri büyüt notları 5 arttır




# Bugün proje değil, iki odaklı alıştırma — gun2.py:

# Görev A — Kare Dict'i: 1'den N'e kadar (N'i kullanıcıdan al) sayıların karelerini tutan bir dict üret — dict comprehension ile. Sonra items() döngüsüyle 3 → 9 formatında yazdır. Bonus: sadece tek sayıların karelerini tutan ikinci bir dict daha üret (filtreli comprehension).

# Görev B — Zip'le Birleştir: İki liste tanımla: urunler = ["ekmek", "süt", "yumurta", "peynir"] ve fiyatlar = [15, 40, 60, 120]. Bunları zip'le birleştirip: (1) ekmek → 15 TL formatında satır satır yazdır (döngüde unpacking kullan), (2) dict(zip(...)) ile fiyat sözlüğü kur, (3) 50 TL üstü ürünleri comprehension'la filtreleyip ayrı bir dict yap ve yazdır.

# İpucu gerekirse: Görev A'da input'un sana ne tipte veri verdiğini hatırla (Hafta 1 Gün 1 klasiği ), range'in bitiş sınırının dahil olmadığını da. Kod bitince at, bakalım. 👀


#görev a
# while True:
#  n =  input("Üst Sınır sayınızı giriniz: ")
#  if len(n.split()) == 0:
#   print("Bir sayı girmediniz! Lütfen bir sayı girişi yapın: ")
#   continue
#  if not  n.isdigit():
#   print("Geçersiz bir sayı girdiniz! Lütfen bir sayı giriniz: ")
#   continue

#  n = int(n)
#  kareler = {x: x**2 for x in range(1,n+1)}
#  print(f"Sayılar ve kareleri --> {kareler}")
#  tek_sayilar_kareler = {t: t**2 for t in range(1,n+1) if t%2 != 0}
#  print(f"Tek sayılar ve kareleri --> {tek_sayilar_kareler}")
#  break



#görev b
urunler = ["ekmek","süt","yumurta","peynir"]
fiyatlar = [15,40,60,120]
for urun,fiyat in zip(urunler,fiyatlar):
 print(f"{urun} --> {fiyat}")                   # ürün fiyat eşleştirmesi
print(dict(zip(urunler,fiyatlar)))
elliler = {urune: fiyate for urune,fiyate in zip(urunler,fiyatlar) if fiyate>50 }
print(elliler)







































print("")

# for harf in "abc":                    stringi tek tek dolaşır ve harf değişkenine atar. alt alta a b c yazdırır
#     print(harf)

# renkler = ["kırmızı", "sarı", "yesil" ]
# for renk in renkler :
#            renk diye o degiskeni biz atıyoruz index 0 dan başlar ve sıradaki renkleri tek tek dolaşır ve renk değişkenine atar. alt alta kırmızı sarı yesil yazdırır
#     print(f"sıradaki renk : {renk}")



#  range (mesela 1'den 100 e kadar saydırmak icin elle yazmıcaz. )

# for sayi in range(5):
#     print(sayi) #0 dan baslar ve 4 e kadar sayar. 5 dahil değil. 0,1,2,3,4 yazdırır


# for sayi in range(50,101):
#     print(sayi) #50 den baslar ve 100 e kadar sayar. 101 dahil değil. slicing in bitis haric kuralı.

# for sayi in range(20,-2,-2):  #20 den baslar ve 0 a kadar -2 er -2 er geri gider.
#     print(sayi )

# toplam = 0
# for sayi in range(1,101):
#     toplam += sayi
#     print(toplam)                     # baslat biriktir ve kullan 3 adımlı bir ritüel bu döngü


#sesli harf sayısını döngü ile kurmak

# cumle = input("Cümlenizi giriniz : ")

# sesli_sayisi = 0
# for harf in cumle.lower():
#     if harf in "aeıioüu":
#         sesli_sayisi +=1

# print(f"Cümlenizdeki sesli harf sayısı : {sesli_sayisi} ")





# while döngüsü

# sayac = 5
# while sayac > 0:
#     print(sayac)
#     sayac -= 1
# print("SAYAC BİTİ. ")



# break     # döngüyü ANINDA terk et
# continue  # bu turun kalanını atla, SONRAKİ tura geç


# while True:                          # sonsuz döngü (bilerek!)
#     komut = input("Komut (çık = q): ")
#     if komut == "q":
#         break                        # kapıdan çık
#     print(f"'{komut}' çalıştırıldı")



# for sayi in range(1,11):
#     if sayi %2 == 0:
#         continue                   # çift sayıları atla
#     print(sayi)




# for i in range(1,4):
    # for j in range(1,4):
        # print(f"{i} x {j} = {i *j }")                 çarpım tablosu

# for + range ile 1'den 10'a kadar sayıları tek satırda yan yana değil, alt alta yazdır. Sonra sadece çift olanları yazdır (iki yol var: range'in adımıyla YA DA % + if. İkisini de dene).
# Toplayıcı deseniyle: 1'den 50'ye kadar sayıların toplamını bul (cevap: 1275, kontrol et).
# while ile 10'dan 1'e geri sayım yaz.
# Dünkü sesli harf sayacını yukarıdaki döngülü versiyonla değiştir, "Ankara Işıkları Öyle Güzel" ile test et (11 çıkmalı).


#1. soru
# for sayilar in  range(1,11):
#     if sayilar %2 == 1:
#         continue
#     print(sayilar)


#2. soru
# toplam = 0
# for sayilar in range(1,51):
#     toplam += sayilar
# print(toplam )



#3. soru
# sayi = 11
# while sayi >= 1:
#     sayi -= 1
#     print(sayi)

# 4. soru

# cumle = input("Cumlenizi giriniz :")
# sesli_sayisi = 0
# for harf in cumle.lower():
#     if harf in "aeioıuöü":
#         sesli_sayisi += 1
# print(f"Sesli harf sayısı : {sesli_sayisi}")


#  FİZZBUZZ SAYIMI (3 İLE BÖLÜNENLER FİZZ, 5 İLE BÖLÜNENLER BUZZ, 15 İLE BÖLÜNENLER FİZZBUZZ)

# FizzBuzz — Efsaneyle Tanış

# Mülakatların en meşhur sorusu. Kuralı basit:

# 1'den 100'e kadar say. Ama:

# Sayı 3'e tam bölünüyorsa sayı yerine Fizz yaz
# 5'e tam bölünüyorsa Buzz yaz
# HEM 3 HEM 5'e bölünüyorsa FizzBuzz yaz
# Hiçbiri değilse sayının kendisini yaz

# for sayi in range(1,101):
#     if sayi %15 == 0:
#         print("FizzBuzz")
#     elif sayi %5 == 0:
#         print("Buzz")
#     elif sayi %3 == 0:
#         print("Fizz")
#     else:
#         print(sayi)




#  çarpım tablosu
# for j in range(1,11):
#     for i in range(1,11):
#         print(f"{i} x {j} = {i*j}")
#     print(f"{j}'ler tablosu")








# Kod bir sayı tutsun (şimdilik elle yaz: gizli_sayi = 42), kullanıcı bilene kadar sorsun:

# Her turda tahmin al (input + dönüşüm — hangisi?)
# Tahmin büyükse "Daha küçük söyle", küçükse "Daha büyük söyle" de
# Bilince "Tebrikler, X denemede bildin!" deyip dur

# gizli_sayi = 52
# tahmin = int(input("Tahmin sayinizi giriniz : "))
# deneme_sayisi = 1
# while tahmin != gizli_sayi:
#     if tahmin < gizli_sayi:
#         print("Daha büyük söyle.")
#         tahmin = int(input("Yeni tahmininizi giriniz : "))


#     elif tahmin > gizli_sayi:
#         print("Daha kücük söyle.")
#         tahmin = int(input("Yeni tahmininizi giriniz :"))
#     deneme_sayisi += 1
# print(f"Tebrikler, {deneme_sayisi} denemede bildin!")                 # bu soruya bakılıcak 28 inde. cok az kaldı son adımı




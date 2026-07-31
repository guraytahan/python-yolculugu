#  faz 1 hafta 1 gün 5

# konu : Listeler

# liste = ["süt", "yumurta", "ekmek"]
# print(liste[0:3:2])  sadece süt ve ekmek cıktısı olur .



# karisik = ["Güray", "22","abc", " "]             # karısık türler de yazılabilir listelerin icine
# # print(karisik)
# print(len(karisik))
# for char in karisik:
#     print(char)                                stringlerde olan kurallar ve herşey aynen çalışır burda da


# listeler degisebilir ve degistirilebilir. stringlerden farkı

# alisveris = ["ekmek", "süt"]
# alisveris.append("peynir")  #sona ekler listenin.
# # print(alisveris)            #sona peynir eklendi. liste değişti.

# alisveris.remove("süt")     #değere göre siler. ilk buldugunu siler.
# alisveris.insert(0,"çay")   # 0. indexe verdiğimiz değeri atar.
# son = alisveris.pop()       #son elemanı ÇIKARIR ve bize VERİR
# alisveris[0] = "kahve"      #indexle üzerine yazıyoruz. bu normalde stringde hata verir ama burda üzerine yazabiliyoruz.
# print(alisveris)


# sort vs sorted

# notlar = [90,85,60,72]
# notlar.sort()             # listeyi yerinde sıralar, geriye birsey vermez.
# print(notlar)             #[60, 72, 85, 90]

# isimler = ["Zeynep", "Melisa", "Güray"]
# sirali = sorted(isimler)      #yeni sıralı liste verir. orjinali durur.
# print(isimler)                # ['Zeynep', 'Melisa', 'Güray']      -- bozulmadı
# print(sirali)                 # ['Güray', 'Melisa', 'Zeynep']

# #  tersten sıralamak icin ikisine de (reverse=True) veriliyor. notlar.sort(reverse=True) gibi.

# # min / max / sum — hazır matematikçiler

# sayilar = [90,80,75,55]
# min(sayilar)
# max(sayilar)
# sum(sayilar)

#ortalama = sum(toplam)/len(toplam)    klasik ikili.

# alisveris = ["ekmek","süt","peynir"]
# for i, urun in enumerate(alisveris,start=1):
#     print(f"{i}.{urun}")


# Boş liste kur, append ile 3 şehir ekle, for ile yazdır.
# [45, 22, 88, 3, 67] listesinin en büyüğünü, en küçüğünü, toplamını ve ortalamasını yazdır.
# Aynı listeyi önce sorted ile sıralayıp yazdır, orijinalin bozulmadığını kanıtla (ikisini de bas). Sonra .sort() uygula ve orijinalin artık değiştiğini gör.
# Şehir listeni enumerate ile 1. İstanbul formatında numaralı bas.
# Tuzak testi: liste = liste.append("x") yap, sonra print(liste) — ne çıktı? Neden? (Bilerek yaptırıyorum, canlı gör 😄)



#1. ısınma sorusu
# sehirler = []
# sehirler.append("Lyon")
# sehirler.append("London")
# sehirler.append("İstanbul")
# for sehir in sehirler:
#     print(sehir)

#2. ısınma sorusu
# sayilar = [45,22,88,3,67]
# maksimum = max(sayilar)
# minimum = min(sayilar)
# toplam = sum(sayilar)
# ortalama = sum(sayilar) / len(sayilar)
# print(f" maksimum: {maksimum}, minimum: {minimum}, toplam: {toplam}, ortalama: {ortalama:.0f}")


#4. ısınma sorusu
# sehirler = ["İstanbul","Ankara","İzmir"]
# for i, city in enumerate(sehirler,start=1):
#     print(f"{i}. {city}")

#5. ısınma sorusu

#none döndürürür sessiz bug gibi.


#MENÜLÜ ALIŞVERİŞ LİSTESİ

alisveris_listesi = []

while True:
    secim = input("----Alisveris Listesi----\n 1.Ürün Ekle \n 2.Ürün Sil \n 3.Listele \n 4.Çıkış \n Seçiminiz:")
    if secim == "1" :
        add_urun =input("Eklemek istediğiniz ürünü giriniz: ")
        alisveris_listesi.append(add_urun)
        print(f"{add_urun},listenize eklendi. ")
    elif secim == "2":
        del_urun =input("Silmek istediginizi ürünü giriniz: ")
        if del_urun not in alisveris_listesi:
            print("Geçersiz ürün girdiniz!")
        else:
            alisveris_listesi.remove(del_urun)
            print(f"{del_urun}, basarıyla listenizden silindi. ")
    elif secim == "3":
        if not alisveris_listesi:
            print("Listeniz boş. ")
    
        for i,urun in enumerate(alisveris_listesi,start = 1):
            print(f"{i}. {urun}")
    elif secim == "4":
        print("İyi alısverisler dileriz. Tekrar bekleriz!")
        break
    else:
        print("Geçersiz bir seçim girdiniz! ")

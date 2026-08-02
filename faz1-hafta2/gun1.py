# Bugün iki veri yapısı öğreniyorsun. Liste "sıralı kutular" idi; dict "etiketli kutular", set ise "tekrarsız torba". Gün sonunda mini görev: kelime frekans sayacı — planında "NLP'nin atası" diye geçiyor, çünkü ileride tokenization ve embedding'e giden yol tam buradan başlıyor.

#dict nedir? listede elemana sıra numarasıyla ulaşıyorduk

# ogrenci = ["Güray", "Bilgisayar Mühendisliği", "3"]
# print(ogrenci[1])      # ama 1 in bölüm ü tanıttıgını ezbere bilmek lazım.

# dict ile anahtar kelime ile ulaşıyoruz.
# {anahtar:değer} çiftleri, virgülle ayrılır. Anahtar (key) genelde string veya sayı; değer (value) her şey olabilir — sayı, string, liste, başka bir dict bile.

student = {"isim" : "Güray", "bölüm": "Bilgisayar Mühendisliği", "sınıf": "3"}
# student["isim"]           # Güray cıktısını verir.
# print(student["isim"])


student["yas"] = 22      # yaş yoktu, ekler
# student["sınıf"] = 4     # sınıf vardı, üzerine yazar

# del student["isim"]      #anahtarı ve değerini siler

# print(len(student))       #4 cıktısı oluyor(yas da ekledigimiz icin) anahtar sayıyor sadece.
# print(student["ogrenci"])  #error verir

# print("isim" in student)    #true döner
# print("Güray" in student)   #false döner



# student["okul"] patlıyor çünkü anahtar yok. get() patlamıyor:
# student.get("okul")
# print(student.get("okul"))       #none döner.HATA yok
# student.get("okul","İKÜ")        # anahtar yoksa "İKÜ" döner (varsayılan değer)
# print(student.getr, yoksa şunu ver."

#kelime sayacında mesela söyle bir format kullanıcaz
# sayac[kelime] = sayac.get(kelime,0) + 1       Türkçesi: "Bu kelimeyi daha önce gördüysem sayısını al, görmediysem 0 kabul et, 1 ekle."
# 1) get() değer ATAMAZ, sadece OKUR, bakıp döner.

# sayac = {}
# sayac["elma"] = sayac.get("elma",0) + 1("okul"))
# student.get("isim","Yok")        #değer var normalde. Güray döner o yüzden

# get(anahtar, varsayılan) = "varsa geti

#dict in 3 görünümü var.
student.keys()      # sadece anahtarlar
student.values()    #sadece değerler
student.items()     # anahtar,değer ikilileri

# for anahtar in student:
#     print(anahtar)         # sadece key'leri gezer


# for values in student.values():
#     print(values)                 #sadece value leri gezer


# for anahtar,deger in student.items():
#     print(f"{anahtar}: {deger}")         #ikisini birden gezer.


# for x in student:
#     print(x)          # x'ler anahtar cıkar : isim,bölüm,sınıf,yas


# print(student.items())

# for k, v in student.items():
#      print(f"{k} → {v}")       #key'den valueye ok cıkartmalı bir yazdırıs.



#ic ice dict lere geciyoruz.

# kulup = {
#     "guray" : {"rol":"baskan yardımcısı", "yil": "3"},
#     "melisa": {"rol":"baskan", "yil":3}

# }
# print(kulup["guray"]["rol"])     #baskan yardımcısı cıktısı olur.

# #liste icinde dict de kullanılır
# ogrenciler= [
#     {"isim":"Güray","okul":"ikü","yas":"22"},
#     {"isim":"ahmet","okul":"itü","yas":"22"}
# ]
# print(ogrenciler[0]["isim"])     #Güray cıktısını verir .API'lerden dönen JSON'lar hep böyle — Hafta 3'te göreceğiz

# kulup = {
#     "guray": {"rol":"baskan yardımcısı","sınıf":"4","yas":"23"},
#     "ahmet": {"rol":"üye","sınıf":"2","yas":"20"}
# }

# # print(kulup["guray"])        #{'rol': 'baskan yardımcısı', 'sınıf': '4', 'yas': '23'} cıktısı bu olur.
# kulup["guray"]["yas"] = 4
# print(kulup)        #sadece guray ın yası degisti. ahmet in yası degismedi




# ogrenciler = [
#     {"isim":"ayse","not":"95","sınıf":"3 "},
#     {"isim":"murat","not":"75","sınıf":"4"}
# ]
# print(ogrenciler[0]["not"])       #ayşe nin notunu cekeriz




# Set (Küme): Tekrarsız Torba

# # Set = tekrarsız, sırasız eleman topluluğu. Süslü parantez ama anahtar-değer yok, sadece elemanlar:

renkler = {"kirmizi","mavi","yesil","kirmizi","siyah"}
# print(renkler)      #tekrarları ucurur. cıktıda sadece kirmizi,mavi,yesil,siyah olur.

#set ler sırasızdır. indexlenemez
# özellikleri 1. Tekrar temizleme — listeyi set'e çevir, tekrarlar gider
# sayilar = {2,1,1,2,2,4,7,8}
# benzersiz = set(sayilar)
# print(benzersiz)         #cıktı: {1,2,4,7,8} olur. tekrarları ucurur.


#2. Küme işlemleri yapılabilir (matematikte bildiğimiz kümelerdeki kesişim birleşim gibi)
# a = {1,2,5,6,8}
# b = {1,8,9,7}

# print(a&b)      #8,1 kesişim
# print(a-b)      #2,5,6  # farkları
# print(a|b)      #1,2,5,6,7,8,9    birleşim yapar



# Boş set {} ile açılmaz — {} boş dict demektir! Boş set: set().

# mini görevler el ısındırmak icin

# type({}) ve type(set()) — ikisini de çalıştır. Farkı kendi gözünle gör.
# renkler[0] dene. Hangi hata? Mesajı oku — Python sana ne diyor?
# a ve b kümelerini kur, &, |, - üçünü de dene. Bir de b - a dene — a - b ile aynı mı?
# "merhaba dünya merhaba".split() sonucunu set()e sok. Kaç eleman? Bu deney, mini görevdeki "benzersiz kelime sayısı"nın ta kendisi.

# print(type({}))         #bu dict
# print(type(set()))      #bu set


# print(renkler[0])    #error! set indexlenmez.
# kelimeler="merhaba dünya merhaba".split()
# benzersiz = set(kelimeler)
# print(len(benzersiz))   #benzersiz kelime sayısını yazdırırız.(2)


# Mini görev - kelime frekans sayacı

while(True):
    cumle = input("Cümlenizi giriniz: ").lower()
    if len(cumle.split()) == 0 :
        print("Geçersiz bir cümle girdiniz. ")
        continue

    kelimeler = cumle.split()
    sayac = {}       # bos bir dict açtık
    for a in kelimeler:
        sayac[a] = sayac.get(a,0)+1         #kelime sayma düzenimiz 
    benzersiz = set(sayac)
    print("KELİME FREKANSLARI")
    for kelime,adet in sayac.items():
        print(f"{kelime} --> {adet}")
    print(f"Toplam kelime : {len(kelimeler)}")
    print(f"Benzersiz kelime : {len(benzersiz)}")
    break










































print(" ")

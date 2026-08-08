# tuğla 1 : *args

#dün öğrendiğim:
# def topla(a,b):
#     return a+b
# ama ya 3,5,10 sayıyı toplamak istesek? her biri icin yeni fonksiyon yazmayız. *args tam bu soruna çözüm: "kaç tane gelirse gelsin, hepsini al" demek.


# def topla(*sayilar):
#     print(sayilar)
#     print(type(sayilar))

# topla(5,6)

# Tuğla 1.5: **kwargs

# *args sırasız yığın topluyordu. Bazen ise isimli argümanları toplamak istersin:


# def bilgi_yaz(**bilgiler):
#     print(bilgiler)
#     print(type(bilgiler))



#tuğla 2 :
# Bir fonksiyon dört tür parametreyi aynı anda alabilir ama sıra kesin:

# def ornek(zorunlu,*args,varsayilan = "deger",**kwargs):
#     print("zorunlu:",zorunlu)
#     print("args:",args)
#     print("varsayilan:",varsayilan)
#     print("kwargs:",**kwargs)





# # Tuğla 3: Scope — Değişken Nerede Yaşar?
# # Fonksiyonun içinde doğan değişken, fonksiyon bitince ölür. Buna local scope denir. Dışarıda doğan ise global.

# #local scope
# def dene():
#     icerde = 10
#     print(icerde)

# #global scope
# x = 5
# def oku():
#     print(x)

# # Ve en kritik deney — gölgeleme (shadowing):

# x = 5
# def degistir():
#     x = 99
#     print("İcerdeki x:",x)
# degistir()
# print("Dısardaki x:",x)
# Kural: içeriden global'i okuyabilirsin, ama x = ... yazdığın an Python yepyeni bir local değişken yaratır; dışarıdakine dokunmaz. (Bir global anahtar kelimesi var ama şimdilik bil-kullanma: global değişken değiştirmek kod hijyeninde kötü koku sayılır. Doğru yol: fonksiyona parametre ver, return ile al.)

# Dünkü derse bağlanıyor: "her çağrı temiz sayfa" demiştik — işte o temiz sayfa, local scope'un ta kendisi.

#tuğla 4: lambda - tek satırlık isimsiz fonksiyon

# kare = lambda x:x**2      # bu satır,alttaki ifade ile aynı sey

# def kare(x):
#     return x**2

# # Madem aynı şey, niye var?" — Lambda'nın gerçek evi, başka bir fonksiyona fonksiyon vermek gereken yerler. En klasiği: sorted'ın key parametresi.

# kelimeler = ["python","sql","computer","business","ai"]
# sorted(kelimeler)      #alfabatik sıralama
# sorted(kelimeler,key = len)    #uzunluga göre sıralama
# sorted(kelimeler,key= lambda k:k[-1])     #son harfe göre sıralama

# # key şunu diyor: "her elemanı sıralamadan önce bu fonksiyondan geçir, çıkan değere göre sırala." Şimdi asıl güç — tuple listesi sıralama:

# ogrenciler = [("Ali",85),("Mehmet",90),("Volkan",60),("Batu",100)]
# sorted(ogrenciler, key = lambda o:o[1])      #kücükten büyüge notlar sıralanması
# sorted(ogrenciler, key = lambda o:o[1],reverse =True) # notlar büyükten kücüge
# sorted(ogrenciler,key = lambda o:(-o[1],o[0]))    #reverse kullanmadan büyükten kücüge sıralama, virgülden sonra gelen o[0] kısmı eğer mesela puanlar aynı ise (bu durumda 1.indexteki değer puanlar) ikinci indexe bakar ve isme göre sıralar. python normalde hep kücükten büyüge sıralama eğilimindedir.




# Tuğla 5: map ve filter

# İkisi de "listedeki her elemana bir şey yap" ailesinden:

# map(fonksiyon, liste) → her elemanı dönüştür
# filter(fonksiyon, liste) → koşulu sağlayanları süz




#alttakiler repl deneyleri
# >>> sayilar = [1, 2, 3, 4, 5, 6]
# >>> map(lambda x: x * 2, sayilar)          # ilginç bir şey dönecek
# >>> list(map(lambda x: x * 2, sayilar))    # şimdi gerçek sonuç
# >>> list(filter(lambda x: x % 2 == 0, sayilar))
# # >>> list(filter(None, [0, 1, "", "merhaba", [], [1]]))  # truthiness sürprizi!



# Tuğla 6: Docstring

# Fonksiyonun ilk satırına yazılan üç tırnaklı açıklama:

# def bmi_hesapla(boy,kilo):
#     """"Kilo (kg) ve boy (m) alınır. Kilo/boy**2 yapılır """""
#     return kilo/boy**2

#help(bmi_hesapla) yazarak bilgiyi çekeriz







# Mini Görev 1: Esnek Hesap Makinesi

# Şartname:

# hesap_makinesi(*sayilar, islem="topla") imzalı bir fonksiyon
# islem şunları desteklesin: "topla", "carp", "ortalama"
# Hiç sayı verilmezse çökmesin — anlamlı bir mesaj döndürsün (bekçi deseni!)
# Docstring'i olsun
# Test çağrıları: hesap_makinesi(1,2,3), hesap_makinesi(2,3,4, islem="carp"), hesap_makinesi(islem="ortalama")

# İpucu: çarpma için sum gibi hazır fonksiyon yok — döngüyle toplayıcı deseni, ama başlangıç değeri 0 değil.


# def hesap_makinesi(*sayilar, islem= "Topla"):
#     """" Toplama,çarpma ve ortalama hesaplayan hesap makinesi."""
#     if not sayilar:
#         return "Lütfen bir sayı giriniz: "
#     #toplama islemi
#     if islem.lower() == "topla":
#         return sum(sayilar)
#     #ortalama islemi
#     elif islem.lower() == "ortalama":
#         return sum(sayilar)/len(sayilar)
#     #carpma islemi
#     elif islem.lower() == "carpma":
#         sonuc = 1
#         for sayi in sayilar:
#             sonuc *= sayi
#         return sonuc
#     else:
#         return "Geçersiz bir işlem girdiniz!"


# print(hesap_makinesi(10,2,islem = "Carpma"))
# # print(hesap_makinesi(islem="ortalama"))
# # print(hesap_makinesi(1,2,3))


# # Mini Görev 2: Çok Kriterli Sıralama

# #veri hazır:
# calisanlar = [
#     ("Ali", "IT", 45000),
#     ("Zeynep", "IT", 52000),
#     ("Mert", "İK", 45000),
#     ("Ayşe", "Finans", 61000),
#     ("Can", "IT", 45000),
# ]

# #istenenler :
# Tek sorted çağrısıyla: önce maaşa göre azalan, maaş eşitse isme göre alfabetik sırala, sonucu yazdır.
# Bonus: filter ile sadece IT çalışanlarını süz, aynı sıralamayı ona da uygula.

# Beklenen çıktı sırası (kendini kontrol et): Ayşe → Zeynep → Ali → Can → Mert. Ali-Can-Mert üçlüsü aynı maaşta, bak bakalım alfabetik dizilmişler mi?

# print(sorted(calisanlar,key = lambda s:(-s[2],s[0])))
# only_it = list(filter(lambda i:i[1] == "IT",calisanlar))
# print(sorted(only_it,key = lambda c:(-c[2],c[0])))







# -- ekstra alıstırma 1
# Mini Logger (esnek fonksiyon — her projede var)

# Gerçek hayat bağlamı: Faz 2 Hafta 13'te logging modülünü öğreneceksin. Bugün onun oyuncak versiyonunu kendin yazacaksın — *args/**kwargs'ın endüstrideki 1 numaralı kullanım yeri tam olarak bu.

# Şartname — logla(*mesajlar, seviye="INFO", **etiketler):

# Mesaj parçalarını tek boşlukla birleştirip başına [SEVIYE] koysun
# seviye ne gelirse gelsin çıktıda BÜYÜK harf olsun
# **etiketler varsa satır sonuna anahtar=deger çiftleri olarak eklensin
# Hiç mesaj verilmezse anlamlı uyarı döndürsün (bekçi!)
# Docstring unutma


# def logla(*mesajlar,seviye="INFO",**etiketler):
#     """"Mini logger programı """
#     if not mesajlar:
#         return "Lütfen anlamlı bir mesaj giriniz! "
#     mesaj = " ".join(mesajlar)
#     seviye_t = seviye.upper()
#     parcalar = [f"{a}={k}" for a,k in etiketler.items()]
#     parcalar = " ".join(parcalar)
#     sonuc = f"[{seviye_t}] {mesaj}"
#     if etiketler:
#         sonuc += "|" + parcalar
#     return sonuc
# print(logla("Bakiye yetersiz", seviye="error", hesap_no=123, tutar=500))
# print(logla("Kullanıcı", "giriş", "yaptı"))



# Alıştırma 2: İşlem Raporu filter + lambda + çok kriterli sıralama
islemler = [
    ("TRX001", "EFT",   1500.0, "basarili"),
    ("TRX002", "Havale", 250.0, "basarisiz"),
    ("TRX003", "EFT",   8750.5, "basarili"),
    ("TRX004", "Kart",   120.0, "basarili"),
    ("TRX005", "EFT",    999.9, "basarisiz"),
    ("TRX006", "Havale", 4300.0, "basarili"),
    ("TRX007", "Kart",   120.0, "basarili"),
]

# İstenenler:

# Sadece başarılı işlemleri süz (filter + lambda)
# Süzülmüş listeyi tutara göre azalan, tutar eşitse işlem ID'sine göre alfabetik sırala (tek sorted, tuple key)
# Sonucu döngüyle satır satır, f-string ile şu formatta yazdır (:.2f — Hafta 5'e küçük bir selam):



basarililar = list(filter(lambda b:b[3] == "basarili",islemler))
son_liste = sorted(basarililar,key = lambda t:(-t[2],t[0]))
for islem_id,tur,tutar,durum in son_liste:
    print(f"{islem_id} {tur} {tutar:.2f} {durum}")


print(son_liste)




# Fonksiyonlar
# def selamla():                         #python def çalıştırmaz. tarif okur.
#     print("Merhaba!")
# selamla()                              #burda da bu tarifi çalıştırırız.

#parametre --> fonksiyona veri sokmak
# def selamla(isim):
#     print(f"Merhaba, {isim.capitalize()}!")
# selamla("mehmet")

# def bmi_hesapla(boy,kilo):
#     print(kilo/ boy **2 )
# bmi_hesapla(1.76,85)

#return --> fonksiyonlardan veri cıkartmak

# def topla_print(a,b):
#     print(a+b)

# def topla_return(c,d):
#     return c+d



#return kelimesi, fonksiyonu anında bitirir.

# def kontrol(sayi):
#     if sayi < 0:
#         return "Negatif bir sayı giremezsiniz! "
#     return f"Karesi = {sayi**2}"
# print(kontrol(11))
# # Dikkat et, else yazmadım. Gerek yok — çünkü sayı negatifse ilk return çalışır ve fonksiyon biter; oraya hiç gelinmez. Buna erken çıkış (early return) deseni denir ve profesyonel kodda çok yaygındı

# #isdigit() bekcisini fonksiyon ile birleştirince şöyle olur
# def yas_kontrol(dogumyili):
#     if not str(dogumyili).isdigit():
#         return None
#     return 2026- int(dogumyili)

# print(yas_kontrol(2003))

#default parametreler (tanım anında değer verilebilir)
#kural: default lu parametreler her zaman default suz lardan sonra gelir.

# def selamla(isim, mesaj = "Merhaba!"):
#     return f"{mesaj} {isim}"
# print(selamla("Güray"))        # cıktısı : Merhaba! Güray
# print(selamla("Güray", "Selam"))        #cıktısı: Selam Güray



# Gerçek hayat örneği — BMI fonksiyonuna yuvarlamayı default yapmak:

# def bmi_hesapa(boy,kilo,basamak=2):
#     return round(boy / kilo**2,basamak)



#keyword argüman okunabilirlik sağlar (fonksiyon tanımlarken parametlere isim ve değer atamak)
# selamla("Güray", "Selam", 3, True)
# selamla("Güray", mesaj="Selam", tekrar=3, buyuk_harf=True)          #okunabilirlik örneği



# def selamla(isim,mesaj="Merhaba",ünlem=1):
#     return f"{mesaj} {isim}" + "!" * ünlem
# print(selamla("Güray"))
# print(selamla(isim = "Mehmet", ünlem= 2))

# 7. Küçük ama önemli: parametreler fonksiyonun İÇİNDE yaşar





# Mini Görev: Refactor Günü

# Bugün yeni program yazmıyorsun; var olan kodu fonksiyonlara bölüyorsun. Buna refactor denir: davranış aynı kalır, yapı iyileşir. Ar-Ge işinin yarısı budur.

# gun3_refactor.py diye yeni dosya aç, Hafta 2'nin üç görevini fonksiyon olarak oraya taşı:

# 1. Kelime frekans sayacı (Gün 1) → kelime_frekansi(metin)

# Metni parametre olarak alsın; input() fonksiyonun DIŞINDA kalsın. (Kural: fonksiyon veriyi kendisi toplamaz, ona verilir — bu, test edilebilirliğin temeli.)
# Frekans dict'ini return etsin, print etmesin. Yazdırmayı çağıran taraf yapsın.
# Boş girdi guard'ını early return'e çevir: if not metin: return {}

# 2. Kare dict'i (Gün 2) → kare_dict(n=10)

# 1'den n'e kadar {sayı: karesi} dict'ini return etsin.
# n default parametre → kare_dict() 10'a kadar, kare_dict(5) 5'e kadar versin.

# 3. Ürün-fiyat birleştirme (Gün 2) → urun_fiyat_birlestir(urunler, fiyatlar, limit=100)

# İki listeyi parametre alsın, zip + comprehension ile dict kursun.
# limit default'u: sadece fiyatı limit'in altındaki ürünler dict'e girsin.
# Düşün (kod yazmana gerek yok): listeler farklı uzunluktaysa ne olur? Gün 2'den hatırla, zip ne yapıyordu? Quiz'de sorabilirim

# Dosyanın en altında üç fonksiyonu da çağır ve sonuçları print() ile göster — bugün öğrendiğin gibi: script'te çıktıyı görmek istiyorsan print kararını çağıran taraf verir. En az bir çağrıyı keyword argümanla yap (örn. urun_fiyat_birlestir(urunler, fiyatlar, limit=50)).

# Başarı ölçütü: fonksiyonların içinde hiç input(), hiç print() yok — sadece al → işle → return. Bugünün ana dersi bu ayrımdı.
# --------------1------------------
metin = input("Cümlenizi giriniz: ")
def kelime_frekansi(metin):
    if not metin:
        return {}
    sayac= {}
    kelimeler = metin.split()
    for kelime in kelimeler:
        sayac[kelime] = sayac.get(kelime,0)+1
    return sayac
sonuc = kelime_frekansi(metin)
print(sonuc)


#------------2-----------
def kare_dict(n=10):
    kare_ikililer = {sayi: sayi**2 for sayi in range(1,n+1)}
    return kare_ikililer
print(kare_dict())
print(kare_dict(5))

# #-----------3--------------
urunler = ["kalem","defter","kulaklık","çanta"]
fiyatlar = [20,45,350,90]
def urun_fiyat_birlestir(urunler,fiyatlar,limit=100):
    sozluk = {urun: fiyat for urun,fiyat in zip(urunler,fiyatlar) if fiyat < limit}
    return sozluk
print(urun_fiyat_birlestir(urunler,fiyatlar))
print(urun_fiyat_birlestir(urunler,fiyatlar,limit = 50))

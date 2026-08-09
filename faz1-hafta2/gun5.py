# bugüne kadar debug'da yaşadığın her ValueError, TypeError, NoneType kavgası bugün resmi olarak "düşman tanıma dersi"ne dönüşüyor


# Terminoloji: Program çalışırken oluşan hataya exception (istisna) denir. Hata oluşunca Python bir exception "fırlatır" (raise), sen de onu "yakalarsın" (except).


# try / except - Temel yapı
# try:
#     yas = int(input("Yasinizi giriniz: "))
#     print("Yasiniz: ",yas)
# except ValueError:
#     print("Bu bir sayı değil! ")
# # Mantık şu:

# try bloğu: "Bunu dene, patlayabilir, haberim var."
# Patlarsa Python try'ın kalanını atlar, except bloğuna zıplar.
# Patlamazsa except hiç çalışmaz.

# Kritik nokta: try içinde hata olan satırdan sonraki satırlar çalışmaz. Yukarıda "abc" girilirse print("Yaşın:", yas) hiç çalışmaz — direkt except'e atlanır.


# exception türleri :

# 1) ValueError : Tip doğru ama değer sacma int("abc") gibi
# 2) TypeError : Tip uyumsuz. None+5 , "a"+3 gibi
# 3) ZeroDivisionError : 5/0 erroru.
# 4) KeyError : dict'te olmayan anahtar. d["yok"]
# 5) IndexError : listede olmayan index. [1,2][5]
# 6) NameError : Tanımsız değisken
# 7) FileNotFoundError : olmayan dosyayı acma




# farklı hatalara farklı tepkiler verebiliriz

# try:
#     sayi = int(input("Sayinizi giriniz: "))
#     sonuc = 100 / sayi
#     print("Sonuc: ",sonuc)
# except ValueError:
#     print("Geçersiz bir sayı girdiniz.")
# except ZeroDivisionError:
#     print("Sıfıra bölemem.")


# # İki hatayı aynı tepkiyle yakalamak istersen tuple kullanırsın (Gün 2'den tanıdık yapı):

# except (ValueError,ZeroDivisionError):
#     print("Geçersiz işlem.")


# # Hata mesajının kendisine erişmek istersen as:
# except ValueError as e:
#     print("Hata detayları: ",e)
# Buradaki e bir değişken, hatayı temsil eden nesneyi tutuyor.



# else ve finally — Tam Yapı

# try:
#     sayi = int(input("Sayinizi giriniz: "))
# except ValueError:
#     print("Geçersiz bir sayı girdiniz! ")
# else:
#     print("Girdiğin sayı ",sayi)           # Sadece HATA olmazsa
# finally:
#     print("Program devam ediyor...")       # her durumda calısır

#  # else: try hatasız biterse çalışır. "Riskli işi try'da yap, başarı sonrası işi else'te yap" ayrımı — kod okunabilirliği için.
#  # finally: Hata olsun olmasın her zaman çalışır. Klasik kullanım: dosya kapatma, kaynak temizleme (Hafta 3'te with bunu otomatikleştirecek, ama mantığı bugün öğren).
# # Sıra hep aynıdır: try → except(ler) → else → finally. Sırayı bozarsan SyntaxError.



# # raise — Hatayı Sen Fırlat

# # Şimdiye kadar hataları Python fırlattı, sen yakaladın. Bazen tersini istersin: kural senin kuralın, ihlal edilince hatayı sen fırlatırsın.


# def para_cek(bakiye,miktar):
#     if miktar<=0:
#         raise ValueError("Miktar pozitif olmalı! ")
#     if miktar > bakiye:
#         raise ValueError("Yetersiz bakiye! ")
#     return bakiye-miktar
# # Python'a göre para_cek(100, 500) gayet geçerli bir işlem — matematiksel sorun yok. Ama iş kuralına göre saçma. raise ile "bu benim dünyamda hata" demiş oluyorsun.

# #kullanan taraf da bunu normal exception gibi yakalar:
# try:
#     bakiye = para_cek(100,500)
# except ValueError as e:
#     print("İşlem reddedildi : ",e)

    # Bunu Hafta 4'te BankaHesabi sınıfında birebir kullanacağız— "yetersiz bakiye kontrolü" doğrudan programda yazıyor. Bugün temelini atıyoruz.



# Görev 1 — Çökmeyen güvenli girdi fonksiyonu

# guvenli_sayi_al(mesaj) adında bir fonksiyon:

# Parametre olarak kullanıcıya gösterilecek mesajı alır
# Kullanıcıdan girdi ister, int'e çevirmeyi try/except ile dener (isdigit değil — artık büyüdün, ayrıca isdigit -5 gibi negatifleri de eler, try/except elemez, farkı düşün)
# Geçersizse uyarı verir ve tekrar sorar (döngü — Gün 4'ten while, hangisi uygun karar ver)
# Geçerli sayıyı return eder (print değil! Gün 3 dersini hatırla: karar çağıran tarafın)

# Bonus: guvenli_sayi_al(mesaj, min_deger=0) — default argümanla alt sınır ekle; sayı geçerli ama sınırın altındaysa yine kabul etme.


def guvenli_sayi_al(mesaj, min_deger=0):
    while True:
        try:
            sayi = int(input(mesaj))
        except ValueError:
            print("Geçersiz bir sayı girdiniz! ")
        else:
            if sayi < min_deger:
                print("Sayınız minimum değerden kücük ve sıfır  olamaz! ")
            else:
                return sayi



# Görev 2 — Sıfıra bölme koruması

# bol(a, b) fonksiyonu:

# b sıfırsa kendin raise et: ValueError("Sıfıra bölme yok") (ZeroDivisionError'ın oluşmasını beklemek yerine kapıda kes — raise pratiği)
# Değilse sonucu return et
# Sonra fonksiyonun dışında, çağıran tarafta try/except ile bu hatayı yakalayıp kullanıcıya düzgün mesaj göster
# Girdileri guvenli_sayi_al ile al — iki görev birleşsin, mini bir hesap aracı olsun


def bol(a,b):
    if b == 0:
        raise ValueError("Sıfıra bölme yok")
    return a / b

a = guvenli_sayi_al("Bölünecek sayıyı gir: ")
b= guvenli_sayi_al("Bölen sayıyı gir: ")

try:
    bolum = bol(a,b)
except ValueError as e:
    print("İşlem reddedildi  ",e)
else:
    print(bolum)





# bonus gün4 ve gün 5 harmanı
# Harman Görevi — "Dayanıklı Hesap Makinesi"

# Veri: ["10", "25", "abc", "40", "-7"] (string listesi, içinde bir bozuk ve bir negatif eleman var — bilerek)

# Versiyon 1 — try/except yolu:

# topla(*degerler) diye bir fonksiyon yaz (tek yıldızla — az önceki dersin pratiği; çağırırken topla(*liste) diyeceksin, yıldız burada listeyi açar)
# Fonksiyon içinde döngüyle elemanları gez; her elemanı int'e çevirmeyi try/except ile dene
# Çevrilenler toplama katılsın; çevrilemeyenler atlansın ve kaç eleman atlandığı sayılsın
# Toplamı return et, atlanan sayısını da raporla (nasıl raporlayacağın senin tasarım kararın — print mi, birlikte mi return, düşün)
# Versiyon 2 — filter/map yolu:

# Aynı liste, bu sefer Gün 4 araçlarıyla: filter + lambda ile isdigit()'ten geçen elemanları süz → map ile int'e çevir → sum ile topla
# Tek satır hedefle; okunmaz hale gelirse ara değişkenle böl, sorun değil
# Kapanış sorusu (yazılı cevap istiyorum, 1–2 cümle):

# İki versiyonun sonucu aynı mı? Özellikle "-7" iki versiyonda da toplama girdi mi?
# Farkı gördüysen: hangi yaklaşım hangi durumda daha güvenilir, neden?
# İpucu istemiyorsan burayı okuma 🙂: "-7".isdigit() ne döner, REPL'de bak — Gün 5'in en başında Görev 1'i anlatırken bu farka bir gönderme yapmıştım.

# Bitince iki versiyonu ve kapanış cevabını birlikte at, üstünden geçelim. Sonrasında gün sonu quiz'i var.

def topla(*degerler):
    toplam = 0
    atlanan = 0
    for deger in degerler:
        try:
            sayi = int(deger)
            toplam += sayi

        except ValueError:
            atlanan += 1
    return toplam,atlanan


liste = ["10", "25", "abc", "40", "-7"]
toplam, atlanan = topla(*liste)
print("Toplam:", toplam, "| Atlanan:", atlanan)




#filter ve lambda ile simdi


temiz_toplam = sum(map(int, list(filter(lambda x: x.isdigit(), liste))))
print(temiz_toplam)    # sessiz hata. yanlıs sonuc (75) veriyor. 68 vermeliydi. - yi çöpe atıyor 7 deki. 

# open() ile dosya acmak


# f = open("notlar.txt","w")
# f.write("Merhaba Dosya")
# f.close()
# # Üç adım: aç → işle → kapat. open() sana bir dosya nesnesi verir (f), onun üzerinden okur/yazarsın.

# close() neden var? Dosya açık kaldıkça işletim sistemi kaynağı tutar, ve yazdıkların bazen close() çağrılana kadar diske gerçekten yazılmaz. Kapatmayı unutursan veri kaybı bile olabilir.



# with: kapatmayı unutamayacağımız yöntem
# "with open("notlar.txt","w") as f:
#     f.write("Merhaba dosya")

#with bloğu bitince dosya otomatik kapanır — hata fırlasa bile. Bu yüzden gerçek hayatta neredeyse hiç kimse elle close() yazmaz, herkes with kullanır. Bugünden itibaren standartımız bu.

#modlar r,w,a
#open()'ın ikinci argümanına mod denir. r --> read modu, w--> write modu, a --> append modu

#dosya yoksa r modu hata verir. icinde yazı varsa ve w modunu kullanırsak içindekini siler üstüne yazar. a modu da sonunda ekler. r ve w dosya yoksa oluşturur ama r error verir.
#w acımasızdır. listeye bir ekleme yapmak icin w yaparsak bütün liste gider. onun icin a kullanıcaz.


#write(), print() gibi değil satır sonu eklemez. yeni satır icin \n (c gibi)

# f.write("birinci satir\n")
# f.write("ikinci satir\n")



# okuma (read), readlines ve de asıl yöntem

# with open("deney.txt", "r") as f:
#     icerik = f.read()        # TÜM dosya tek string


# with open("deney.txt","r") as fr:
#     satirlar = fr.readlines()       # satırların listesi


# Ama asıl profesyonel yöntem — dosya nesnesi zaten döngüyle gezilebilir:


# with open("deney.txt","w") as f:
#     f.write("merhaba dünya\n")
#     f.write("Bu da ikinci satır.\n")

# with open("deney.txt","r") as f:
#     for satir in f:
#         print(satir.strip())     # strip() eklemek, satırlar arası boslugu siler. print de ekledigi icin o boslugu siliyoruz aslında

# Bu yöntem dosyayı satır satır okur, dev dosyalarda bile belleği şişirmez. Kritik tuzak: Okuduğun her satırın sonunda \n dahildir. Yani "ekmek al\n" gelir, "ekmek al" değil. Çözüm eski dostun: satir.strip().




# Desen: oku → listeye al → işle → geri yaz

# Bugünkü mini görevin kalbi bu desen. Dosya doğrudan "düzenlenmez"; akış hep şöyledir:

# Dosyayı oku, satırları temiz (strip'li) bir listeye al
# Listede istediğin işlemi yap (ekle/sil — bunları zaten Hafta 1'den biliyorsun!)
# Listeyi "w" moduyla dosyaya komple geri yaz


# Mini Görev: TXT'ye Kayıtlı Yapılacaklar Listesi

# Hafta 1'deki menülü alışveriş listesinin evrimi — ama bu sefer program kapanıp açılınca liste hatırlanacak:

# Menü: 1) Listele 2) Ekle 3) Sil 4) Çık
# Görevler gorevler.txt dosyasında, her satırda bir görev
# Program açılınca dosyadan yüklesin (dosya yoksa çökmesin! — Gün 5'ten ne kullanacağını biliyorsun 😉)
# Ekleme/silme sonrası dosyaya kaydetsin
# Boş görev eklenmesin (bekçi)

gorevler = []
try:
 with open("gorevler.txt","r") as f:
    for satir in f:
        gorevler.append(satir.strip())
except FileNotFoundError:
  print("Kayıtlı dosya yok, boş listeye başlıyoruz.")
while True:
    secim = input("Seçiminizi giriniz: 1) Listele    2) Ekle    3) Sil    4) Çık\n")
    if not secim:
        print("Geçerli bir seçim girmelisiniz! ")
        continue
    elif secim == "1":
        with open("gorevler.txt","r") as f:
            for satir in f:
                print(satir.strip())
    elif secim == "2":
        add_urun = input("Eklemek istediğiniz ürünü girin: ").lower()
        if not add_urun:
            print("Geçersiz bir ürün girdiniz.")
            continue
        elif add_urun in gorevler:
           print("Bu ürün zaten sepetinizde bulunuyor! ")
           continue
        gorevler.append(add_urun)
        with open("gorevler.txt","a") as f:
           f.write(add_urun + "\n")
    elif secim == "3":
       del_urun = input("Silmek istediğiniz ürünü girin : ").lower()
       if not del_urun:
          print("Silmek istediğiniz ürün geçersiz bir üründür. ")
          continue
       elif not del_urun in gorevler:
          print("Silmek istediğiniz ürün listenizde bulunmuyor! ")
          continue
       gorevler.remove(del_urun)
       with open("gorevler.txt","w") as f:
          for s in gorevler:
             f.write(s + "\n")
    elif secim == "4":
       print("Alışveriş listenizden cıkılıyor...")
       break

    else:
       print("Geçersiz bir seçim girdiniz! ")
       continue

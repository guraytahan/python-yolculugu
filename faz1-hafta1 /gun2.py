#  stringler ve stringlerde oynamak

# kelime = "Merhaba"
# print(kelime[0]) 0'dan baslar saymaya array index mantıgı aynı
# print(kelime[1]) cıktısı e olur
# print(kelime[2])
# print(kelime[3])
# print(kelime[4])
# print(kelime[5])
# print(kelime[6])  son harf cıktısı a olur

# print(len(kelime)) uzunlugu cıktısı 7 olur.   son harf her zaman len-1




# cumle = "bugün hava cok güzel"
# print("hava" in cumle)  true döner  (cümle icinde hava geciyor )
# print("kar" in cumle)   false döner  (cümle icinde kar gecmiyor )




# string metotları

# metin = "     Bugun VakıfBank'ta stajımın 14.günüm   "

# metin.upper() hepsini büyük harf yapar
# print(metin.upper()) yazdırırız onu ekrana
# metin.lower() hepsi kücük harf olur
# metin.strip() boslukları temizler basta ve sondaki
# metin.replace("Bugun", "Today") yer degistirir


# metotlar orijinali degistirmez. metin degismez yani, yeni string üretip verir.

# metin = metin.upper()   # sonucu atarsan ona o zaman kalıcı olur



# SPLİT VE JOİN

# cumle = "Bugün hava çok güzel."
# kelimeler = cumle.split()
# print(kelimeler)   kelimelerine ayırstırıp cıktı olarak veriyor




# kelimeler = ['Bugün', 'hava', 'çok', 'güzel']
# print(" " .join(kelimeler))  #Bugün hava çok güzel  # birleştiriyoruz join ile ve de tırnak arasındaki boşluk kelimeler arasına ne geleceğini gösteriyor.(burada bosluk koyduk ki kelimeler arası bosluk olsun.)




# Kullanıcıdan bir cümle al (input), kaç karakter olduğunu yazdır.
# Aynı cümleyi tamamı BÜYÜK ve tamamı küçük olarak yazdır.
# Cümleyi split() ile kelimelere ayır ve listeyi yazdır. Sonra len() ile kaç kelime olduğunu yazdır. (İpucu: len sadece string'e değil, listeye de çalışır — kaç eleman var diye sayar.)
# Cümlenin içinde "a" harfi geçiyor mu, in ile kontrol edip yazdır.

# cumle = input("Bir cümle yazınız:")  yukarıdaki sorunun cevabı ısınma gibi düsün incele dönüp
# print(cumle.upper())
# print(cumle.lower())
# print(len(cumle))
# print(cumle.split())
# print(len(cumle.split()))
# print("a" in cumle)



# SLİCİNG KONUSU (STRİNG DEN DİLİM ALMAK )

# Index tek harf veriyordu; slicing aralık verir. Sözdizimi: kelime = [başlangıç:dur]

# kelime = "merhaba"
# print(kelime[0:3]) cıktısı mer olur. mer = 0,1,2 (3 yok dikkat et)

# print(kelime[4:6]) cıktısı ab olur

# bos bırakma kısayolları da var

# print(kelime[:3])  baştan 3'e kadar.
# print(kelime[3:])  cıktısı haba olur (3'ten sona kadar bu sefer )
# kelime[:] kopyası olur direkt merhaba cıkar

# negatif indexler de var

# kelime[-1]    # "a"  → son harf
# kelime[-2]    # "b"  → sondan ikinci
# kelime[-4:]   # "haba" → son 4 harf


# slicing in gizli adımı var o da adımlamak.
# kelime[::2] 2'ser atlayarak yazdırır -- "mraa"

# peki adım -1 olursa ne olur? kelimeyi tersten yazdırmanın hilesi.

# print(kelime[::-1]) kelimeyi tersten yazdırır.

# Gün 2 Mini Görevi (dokümandan)

# Kullanıcıdan bir cümle al ve üçünü yap:

# Cümleyi tersten yazdır (az önce sırrını verdim 😄)
# Kelime sayısını yazdır (bunu ısınmada zaten çözdün, buraya taşı)
# Sesli harf sayısını yazdır — işte asıl bulmaca bu.


# cumle = input("İslem yapmak istediginiz cumleyi giriniz: ")

# print(cumle[::-1])
# print(len(cumle.split()))
# # sesli harf sayısı
# cumle= cumle.lower()

# sesli_harfler_toplam= cumle.count("a") + cumle.count("e") + cumle.count("ü") + cumle.count("i") + cumle.count("u") + cumle.count("ı") + cumle.count("ö") + cumle.count("o")
# print(sesli_harfler_toplam)


# "kırmızı,mavi,yeşil" string'ini ['kırmızı', 'mavi', 'yeşil'] listesine çeviren kodu yaz. Sonra o listeyi "kırmızı - mavi - yeşil" haline geri getiren kodu yaz.

# renkler = "kırmızı, mavi ,yeşil"
# liste = renkler.split()
# print(" - " .join(liste) )

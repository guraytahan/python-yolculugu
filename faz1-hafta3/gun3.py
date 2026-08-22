# Bölüm 1: import çeşitleri

# Şimdiye kadar import random kullandık. Üç ana biçim var:


# import random              # 1) modülün tamamı → random.randint(1, 10)
# from random import randint # 2) sadece istediğin şey → randint(1, 10)
# import random as rnd       # 3) takma ad → rnd.randint(1, 10)

# Ne zaman hangisi?

# import modul → varsayılan tercih. Kodu okuyan kişi random.randint görünce fonksiyonun nereden geldiğini anında bilir.
# from modul import x → o modülden 1-2 şey kullanacaksan ve isim çakışması riski yoksa.
# as → uzun isimleri kısaltmak için. İleride her gün göreceksin: import pandas as pd, import numpy as np.
# from modul import * →  kullanma. Modüldeki HER ismi senin dosyana boca eder; hangi isim nereden geldi belli olmaz, sessizce senin değişkenlerini ezebilir. (Gün 5'te yaşadığın "sessiz hata" tuzağının kuzeni.)



# Bölüm 2: Kendi modülünü yazmak

# Sürpriz: her .py dosyası zaten bir modüldür. Yani araclar.py diye bir dosya yazarsan, aynı klasördeki başka bir dosyadan import araclar diyebilirsin.


# # araclar.py
# def selamla(isim):
#     return f"Merhaba {isim}!"

# # main.py (aynı klasörde)
# import araclar
# print(araclar.selamla("Güray"))

# Burada kritik bir kavram var: if __name__ == "__main__":

# Python bir dosyayı çalıştırdığında ona gizli bir değişken verir: __name__.

# Dosyayı doğrudan çalıştırırsan (python araclar.py) → __name__ değeri "__main__" olur.
# Dosya başka yerden import edilirse → __name__ değeri "araclar" (dosya adı) olur.

# Bu ne işe yarar? Import edilen dosyanın tüm kodu baştan sona çalışır. Yani araclar.py'nin en altında print("test") varsa, main.py onu import ettiği anda o print ekrana basılır — istemediğin bir yan etki. Çözüm:

# # araclar.py
# def selamla(isim):
#     return f"Merhaba {isim}!"

# if __name__ == "__main__":
#     # Bu blok SADECE dosya doğrudan çalıştırılınca çalışır
#     print(selamla("test"))

# Böylece dosyayı hem tek başına test edebilirsin, hem de import edince yan etki olmaz. Bunu bundan sonra her projende göreceksin.


# Bölüm 3: Standart kütüphane turu

# Bunların hepsini ezberlemeyeceksin — var olduklarını bilmen yeterli, detay lazım olunca bakarsın.


# import random
# random.randint(1,10)      # 1 ve 10 arası random bir sayı (10 dahil)
# random.choice(["a","b"])    #random listeden seçmek
# # random.shuffle(liste)      #listeyi yerinde karıştırmak

# #datetime
# from datetime import datetime
# simdi = datetime.now()
# print(simdi.year, simdi.month, simdi.day)
# print(simdi.strftime("%d.%m.%Y %H:%M"))   # → "22.08.2026 14:30" gibi formatlı string

# #strftime = string format time, tarih kaydederken harcama takipcide bunu kullanıcaz

# #os ve pathlib
# import os
# os.getcwd() #suan hangi klasördeyiz
# os.listdir()  #klasördeki dosyaların listesi

# from pathlib import Path
# p = Path("veriler.txt")
# p.exists()    # --> dosya var mı yok mu ona bakar (True/False)


# #collections
# # Counter = saymak için özelleşmiş dict.Gün 1'de get deseniyle elle yazdığım sayacın hazır hali:

# from collections import Counter
# sayac = Counter(["elma","armut","elma"])
# print(sayac)        # Counter({'elma': 2, 'armut': 1})
# print(sayac.most_common(2))    # [('elma', 2), ('armut', 1)] → en sık 2 tanesi


# Evet — senin sorted(items, key=lambda ...) + dilimleme ile yaptığın top-5 işini most_common(5) tek satırda yapıyor.


# defaultdict = anahtar yoksa hata vermek yerine otomatik varsayılan değer üreten dict:

# from collections import defaultdict
# # gruplar = defaultdict(liste)   #olmayan anahtara erişince otomatik [] olusturur
# gruplar["meyve"].append("elma")    #keyerror yok. önce [] olustu sonra append edildi



# Mini Görev: Kelime sayacını Counter ile 3 satıra indir

# Gün 1'de yazdığın kelime frekans sayacını hatırla (get deseni, döngü, sorted+lambda ile top listesi). Şimdi aynı işi yap:

# Kullanıcıdan metin al
# Kelime frekanslarını Counter ile çıkar
# En sık geçen 3 kelimeyi yazdır

# Hedef: ~3 satır (input dahil). Bekçi/guard eklemek istersen serbest, ama çekirdek mantık 3 satıra sığmalı.

# Bonus düşünme sorusu (kodunu gönderirken cevabını da yaz): Counter bir dict ise, sayac["olmayan_kelime"] sence ne döner — KeyError mı, başka bir şey mi? Önce tahmin et, sonra REPL'de dene.


from collections import Counter
while True:
    metin = input("Cümlenizi giriniz: ")
    if not metin:
        print("Geçersiz bir cümle girdiniz!")
        continue
    break
sayac = Counter(metin.split())
print(f"Metninizde en sık geçen 3 kelime : {sayac.most_common(3)}")

# Hafta 3 Gün 2: JSON ve CSV. Dün TXT dosyasına yazdın — bugün "yapılandırılmış" dosya formatlarına geçiyoruz. Bu gün önemli çünkü ileride API'lerden gelen her şey JSON, kurumlardaki raporlar CSV olacak. Yani bugün öğrendiğin şey  Faz 4'te birebir karşına çıkacak.

#  json dosyası söyle görünür :

# {"ad" : "Güray","yas":20, "diller" = ["Python","SQL"]}
# json da hep cift tırnak olur. python da none, json da null

# Dört fonksiyon — hepsi bu

# json modülünde işine yarayacak 4 fonksiyon var. İkili ikili düşün:

# Dosyayla çalışanlar (s'siz):

# json.dump(veri, dosya) → Python nesnesini dosyaya yazar
# json.load(dosya) → dosyadan okuyup Python nesnesine çevirir

# String'le çalışanlar (s'li):

# json.dumps(veri) → Python nesnesini JSON string'ine çevirir
# json.loads(metin) → JSON string'ini Python nesnesine çevirir


# yazma tarafı söyle görünür :
# import json

# kisi = {"ad": "Güray","yas": 23, "diller": ["Python","SQL"]}

# with open("kisi.json","w",encoding="utf-8") as f:
#     json.dump(kisi,f, ensure_ascii=False,indent=2)
#     #ensure_acsii = false demek türkce karakterlerin bozulmadan yazılması icin bir pratik. indent = 2 koymak da dosya tek satır yerine girintili ve okunabilir olur.

# # okuma tarafı a söyle görünür :
# with open("kisi.json","r",encoding="utf-8") as f:
#     veri = json.load(f)

# print(veri["ad"])       #normal dict gibi kullanabiliriz.
# print(type(veri))       # dict
# Kritik nokta: load sana gerçek bir Python nesnesi verir. Dosyada [{...}, {...}] varsa elinde dict listesi olur — döngüyle gezersin, get kullanırsın, her şey normal.


# CSV — tablonun düz metin hali

# CSV = virgülle ayrılmış satırlar. Excel'in / veritabanı raporunun en yalın hali:

# urun,adet,fiyat
# elma,3,5.50
# ekmek,2,12.00

# "Bunu split(",") ile ben de parçalarım" diyebilirsin — haklısın, basit dosyada olur. Ama hücre içinde virgül varsa ("Kadıköy, İstanbul") split patlar; csv modülü bunları doğru yönetir. O yüzden CSV işinde her zaman csv modülü.

# yol 1 - csv.reader : her satır bir liste

# import csv

# with open("urunler.txt","r",encoding = "utf-8") as f:
#     okuyucu = csv.reader(f)
#     for satir in okuyucu:
#         print(satir)

# Çıktı:

# ['urun', 'adet', 'fiyat']
# ['elma', '3', '5.50']
# ['ekmek', '2', '12.00']

# Başlık satırı da normal satır gibi gelir — genelde next(okuyucu) ile atlanır.
# Her şey string gelir. '3' sayı değil. Hesap yapacaksan int() / float() senin işin. (İşte dünkü int("7.5") hassasiyeti burada da geçerli.)


# Yol 2 — csv.DictReader: her satır bir dict (genelde daha iyisi)

# with open("urunler.txt","r",encoding = "utf-8") as f:
#     okuyucu = csv.DictReader(f)
#     for satir in okuyucu:
#         print(satir["urun"], satir["fiyat"])

# DictReader başlık satırını otomatik okur ve anahtar yapar: {"urun": "elma", "adet": "3", "fiyat": "5.50"}. satir[1] yerine satir["fiyat"] yazmak hem okunaklı hem güvenli — sütun sırası değişse bile kod bozulmaz. Ar-Ge'de tercih edilen budur.


# mini görevler

# deney 1
# 3-4 kişilik bir dict listesi kur (ör. {"ad": ..., "yas": ..., "sehir": ...}), kisiler.json dosyasına düzgün formatta (Türkçe karakter + girinti) kaydet. Sonra ayrı bir okuma bloğuyla dosyadan geri yükle ve her kişiyi "Güray (20) - İstanbul" formatında ekrana bas. Bonus: yaş ortalamasını hesapla (Hafta 2'den sum + len biliyorsun).

import json

kisiler = [{"ad":"Güray","yas":23,"sehir":"İstanbul"},{"ad":"Mehmet","yas":44,"sehir":"Bursa"},{"ad":"Mete","yas":29,"sehir":"Antalya"}]

with open("kisiler.json","w",encoding = "utf-8")as f:
    json.dump(kisiler,f,ensure_ascii= False,indent=2)

with open("kisiler.json","r",encoding ="utf-8")as f:
    veriler = json.load(f)
    # print(type(veriler))
    for veri in veriler:
        print(f"{veri["ad"]} ({veri["yas"]}) - {veri["sehir"]}")

yaslar = [data['yas'] for data in veriler]
ortalama_yas = sum(yaslar) / len(yaslar)
print(f"Kisilerin ortalama yaşı : {ortalama_yas}")





#deney 2 ürünler.csv

# Programın:
# csv.DictReader ile dosyayı okusun
# fiyatı 10 TL'nin üzerindeki ürünleri ekrana bassın (ör. ekmek - 12.0 TL)
# En sonda bu filtrelenen ürünlerin toplam tutarını yazdırsın (her ürün için adet × fiyat, hepsinin toplamı)

# Hatırlatmalar: DictReader'dan gelen her değer string — karşılaştırma ve çarpma yapmadan önce tip dönüşümü lazım (hangisine int, hangisine float?). REPL Deney 2'deki tuzak satırı tam bunun provasıydı 😉

# Yazmadan önce akışı kafanda Türkçe kur: "oku → her satır için fiyatı sayıya çevir → 10'dan büyükse yazdır ve tutarı toplama ekle → sonda toplamı bas." Bitirince çalıştırılmış halini at, sonra gün sonu quizine geçiyoruz.

import csv
with open("urunler.csv", "w", encoding="utf-8") as f:
    f.write("urun,adet,fiyat\nelma,3,5.50\nekmek,2,12.00\nsut,1,25.00\narmut,4,7.00\net,1,300.00\nyogurt,2,12.00")

with open("urunler.csv","r",encoding= "utf-8") as f:
    okuyucu = csv.DictReader(f)
    toplam_tutar = 0
    for satir in okuyucu:
        fiyat = float(satir['fiyat'])
        if fiyat > 10:
            print(f"{satir['urun']} --> {fiyat}")
            toplam_tutar += int(satir['adet'] )* fiyat

print(f"Toplam tutar : {toplam_tutar}")

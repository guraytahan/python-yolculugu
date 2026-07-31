# Şimdiye kadar hep Python'un çekirdeğini kullandık. Ama Python'un asıl gücü modüllerinde — hazır alet çantaları. İlk çantanı açıyorsun:

# import random                          #  random modülü, dosyanın en üstüne 1 kez, cantayı acıp pakete koyuyoruz
# gizli = random.randint(1,100)         #1 ve 100 arasında random bir sayı. ikisi de dahil !

# DIŞ DÖNGÜ (while True):   "tekrar oynamak ister misin?"
#     İÇ DÖNGÜ:             tek bir oyunun tur döngüsü (tahminler)       bugünkü oyunun yapısı. döngü icinde oyun.

#proje kuralları

# Rastgele sayı: random.randint(1, 100) — artık 52 değil
# Deneme sınırı: Oyuncunun 7 hakkı var. Her tahminde kaç hakkı kaldığını göster ("Kalan hak: 5"). Hak biterse "Kaybettin! Sayı X'ti" de.
# Yön ipuçları: Gün 4'teki gibi büyük/küçük söyle.
# Skor: Kazanırsa kaç denemede bildiğini söyle. Bonus: 10 - deneme gibi bir puan hesapla.
# Tekrar oynama: Oyun bitince (kazansın/kaybetsin) "Tekrar? (e/h)" sor. "e" ise yeni sayıyla baştan, "h" ise "Görüşürüz" + çık.
# Girinti haritasını önce kâğıda çiz: Hangi satır hangi döngünün içinde? Rastgele sayı nerede üretilmeli — dış döngünün içinde mi, dışında mı? (Yanlış yere koyarsan her oyunda aynı sayı gelir — düşün neden)

import random

while True:
    gizli_sayi = random.randint(1,100)
    for deneme_sayisi in range(1,8):
        tahmin = input(" Sayı tahmininizi giriniz: ")
        while not tahmin.isdigit():
            tahmin = input("Geçersiz bir tahmin girdiniz! Yeni tahmin giriniz : ")

        tahmin = int(tahmin)
        if tahmin == gizli_sayi:
            puan = 10 - deneme_sayisi
            print(f"Tebrikler! Gizli sayınızı {deneme_sayisi}. denemenizde buldunuz.Puanınız = {puan} ")
            break

        elif tahmin < gizli_sayi:
            print("Daha büyük bir sayı giriniz. ")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı giriniz. ")
        else:
            print("Geçersiz bir sayı girdiniz. ")





    else:
        print(f"Kaybettiniz. Sayınız {gizli_sayi} idi. Puanınınız : 0 ")


    soru = input(" Tekrar oynamak ister misiniz? (e/h)").lower()
    if soru == "h":
        print("Görüşmek üzere!")
        break
    elif soru == "e":
        print("Yeni oyuna başlıyorsunuz.")
    else:
        print("Geçersiz bir input girdiniz!")


























































































print("")

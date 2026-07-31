# if else konuları

# x = 5     # TEK eşittir  → ATAMA: "x artık 5'tir"
# x == 5    # ÇİFT eşittir → SORU:  "x, 5 midir?"


# yas = 20
# if yas >=18:
#     print("ehliyet alabilirsin . ")


# yas = int(input("Yasınızı giriniz : "))
# if yas >=18:
#     print("ehliyet alabilirsi.")

# else:
#     print("ehliyet alamazsın. ")


# not_ = 85

# if not_ >= 90:
#     print("Notunuz AA")
# elif not_ >=80:
#     print(" Notunuz BA")
# elif not_ >= 70:
#     print("BB")
# elif not_ >= 60:
#     print("CB")


# else:
#     print("Kaldın. ")





# yas = int(input("Yasinizi giriniz. "))

# if yas > 18 and yas <65 :
#     print("Calisabilir yastasiniz. ")
# else:
#     print("Calisabilecek bir yasta degilsiniz.")

# yas = int(input("Yasinizi giriniz : "))   üsstekinin daha sık bir if yazılısı direkt matematikte gibi
# if 18<=yas<65:
#     print("Calisabilir bir yas. ")
# else:
#     print("Calisamazsiniz. ")

# isim = input("İsminizi giriniz : ")

# if isim:
#     print(f"Merhaba {isim}")
# else :
#     print("Bir isim giriniz! ")


# ısınmalar
# 1) 5 == 5.0 true döner cünkü ikisi aynı sey demek

# 2. ısınma sorusu
# sifre = input("Sifrenizi giriniz:")
# if sifre == "python123":
#     print("Giriş başarılı. ")
# else:
#     print("Hatalı şifre!")

# 3. ısınma sorusu

# sayi = int(input("Sayinizi giriniz."))
# if sayi < 0:
#     print("Girdiğiniz sayı negatif bir sayıdır. ")
# elif sayi == 0:
#     print("Girdiğiniz sayı sıfırdır. ")
# elif sayi >0:
#     print("Girdiğiniz sayı pozitif bir sayıdır. ")
# else:
#     print("Girdiğiniz sayı geçersizdir. ")

# 4. ısınma sorusu 2. alıştırmayı truthiness ile güçlendir: kullanıcı hiçbir şey yazmadan Enter'a bastıysa "Boş geçilemez!" desin. (İpucu: önce boşluğu kontrol et)


# password = input("Şifrenizi giriniz : ")
# if password:
#     if password == "python123":
#         print("Giris basarılı. ")
#     else :
#         print("Sifreniz hatalı. ")
# else:
#     print("Sifre kısmı boş geçilemez. ")


# kullanıcıdan 0-100 sayı al ve harf notlarına göre ayrıstır. 90+  → AA    80–89 → BA    70–79 → BB
# 60–69 → CB   50–59 → CC    50 altı → FF

# harf_notu = int(input("Sınav puanınızı giriniz :"))
# if harf_notu < 0 or harf_notu >100:
#     print("Geçersiz bir sınav puanı girdiniz. ")
# elif harf_notu >=90:
#     print("Ders notunz AA")
# elif harf_notu >=80:
#     print("Ders notunuz BA")
# elif harf_notu >=70:
#     print("Ders notunuz BB")
# elif harf_notu >=60:
#     print("Ders notunuz CB")
# elif harf_notu >=50:
#     print("Ders notunuz CC")
# else:
#     print("Ders notunuz FF")



# BMI = kilo / (boy × boy) — kilo kg cinsinden, boy metre cinsinden (1.78 gibi).

# print("BMI hesaplama programına hoşgeldiniz. ")
# kilo = float(input("Kilonuzu giriniz (kg cinsinden) :"))
# if kilo >= 300 or kilo <=0:
#     print("Gecersiz bir kilo girdiniz. ")
#     exit()

# boy = float(input("Boyunuzu giriniz (metre cinsinden) :"))
# if boy >=3 or boy <=0:
#     print("Gecersiz bir boy girdiniz. ")
#     exit()

# bmi = kilo / (boy * boy)
# print(f" Vücut kitle indeksiniz : {bmi:.1f}")
# if bmi < 18.5:
#     print("Zayıf kategorisindesiniz. ")
# elif bmi <25 :
#     print("Normal bir orandasınız. ")
# elif bmi <30 :
#     print("Fazla kilolusunuz.")
# else:
#     print("Obez bir orandasınız. ")

# Python Yolculuğum 

24 aylık AI Engineer yol haritamın kod günlüğü. Hedef: Python temellerinden
başlayıp üretim seviyesinde AI/Ar-Ge mühendisliğine ulaşmak. Bu repo,
yolculuğun her haftasını gün gün belgeliyor.

## 📁 Yapı

| Klasör | İçerik |
|---|---|
| `faz1-hafta1/` | Python temelleri: değişkenler, string'ler, koşullar, döngüler, listeler |

## Faz 1 — Hafta 1: Python Temelleri (Temmuz 2026)

- **Gün 1:** Değişkenler, temel tipler, input/print, f-string
- **Gün 2:** String metotları, slicing, split/join
- **Gün 3:** if/elif/else, mantık operatörleri, truthiness
- **Gün 4:** Döngüler (for/while), break/continue, FizzBuzz 
- **Gün 5:** Listeler, menülü alışveriş listesi uygulaması
- **Gün 6:** Proje günü 

##  Haftanın Projesi: Sayı Tahmin Oyunu (`faz1-hafta1/gun6.py`)

Bilgisayarın tuttuğu 1-100 arası sayıyı 7 denemede bulmaya çalıştığınız
konsol oyunu.

**Çalıştırma:**

**Özellikler:**
- `random.randint` ile her oyunda yeni rastgele sayı
- 7 deneme hakkı; her yanlışta büyük/küçük yön ipucu
- Erken bilene yüksek puan (`10 - deneme sayısı`)
- Girdi doğrulama: sayı olmayan girişler hak yakmadan yeniden sorulur
- Oyun sonunda tekrar oynama (e/h)

**Bilinen Kısıtlar:**
- Tekrar oynama sorusuna e/h dışında bir cevap verilirse program bunu
  "evet" gibi değerlendirip yeni oyun başlatıyor.

**Tekrar Yapsam Ne Değiştirirdim:**
- Girdi doğrulamayı `isdigit()` yerine `try/except` ile yapardım
  (Hafta 2'de öğrenince güncelleyeceğim).
- e/h sorusunu da geçerli cevap gelene kadar tekrar soran bir bekçiye
  bağlardım.

---
*Bu repo haftalık olarak güncellenmektedir.*

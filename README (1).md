# gereksinim-tarayici

Gereksinim dokümanını geliştirme başlamadan önce boşluk için tarar.

## Neden

Analiz dokümanındaki eksik, UAT'de ortaya çıkınca pahalı; refinement'ta çıkınca
ucuz. Bu araç o ilk okumayı yapıyor: belirsiz ifade, test edilemez madde, eksik
kabul kriteri, çelişki, açık soru.

Çıktı bir taslak. Modelin bulduğu her şey doğru değil, bulamadığı şeyler var.
Son kararı dokümanı yazan verir — araç yerine düşünmez, önce düşündürür.

## Kullanım

Ücretsiz: Google AI Studio'nun free katmanı, kart istemez.

1. https://aistudio.google.com → Google hesabıyla gir → **Get API key** → **Create API key**
2. Terminalde:

```
pip install google-genai
```

Windows (PowerShell):
```
$env:GEMINI_API_KEY = "buraya-anahtar"
python tarayici.py ornek.md
```

Mac/Linux:
```
export GEMINI_API_KEY="buraya-anahtar"
python3 tarayici.py ornek.md
```

Ücretsiz katmanda günlük istek sınırı var; bu araç için fazlasıyla yeter.
Kullanılan model `tarayici.py` içinde tek satırda tanımlı; değiştirmek için
orayı düzenlemek yeter.

`ornek.md` bu depo için uydurulmuş bir dokümandır, hiçbir şirkete ait değildir.
Bilerek boşluklu yazıldı: "hızlı", "uygun şekilde", "çok büyük" gibi ölçüsüz
ifadeler ve kabul kriteri olmayan maddeler içeriyor.

## Ne buluyor, ne bulamıyor

Aynı örnek doküman üzerinde beş tur çalıştırıp promptu her turda değiştirdim.
Gözlemler:

- Ölçüsüz kelimeleri ("hızlı", "uygun şekilde", "çok büyük") ilk turdan
  itibaren eksiksiz yakalıyor.
- Açık soru üretmesi talimatla düzeldi: ilk turda boş döndü, "her belirsiz
  ifade için somut bir soru yaz" dedikten sonra kullanışlı sorular geldi
  (eşzamanlı düzenlemede çakışma yönetimi, geri almada e-posta telafisi gibi
  benim ilk okuyuşta atladığım sorular dahil).
- Çelişkiyi üç tur boyunca bulamadı; gerilimi fark edip soru olarak yazıyor,
  "çelişki" demiyordu. Örnek vermek de işe yaramadı sandım. Sorun modelde
  değil bendeydi: prompt ile doküman arasındaki ayırıcı satırı yanlışlıkla
  silmişim, talimat metni dokümana bitişik gidiyordu. Düzeltme olarak
  talimatı dokümanla birleştirmek yerine ayrı gönderdim (system_instruction);
  aynı talimat çelişkiyi doğru çiftle buldu ve "kabul kriteri eksik" listesi
  de istediğim gibi üçe inip gerekçeli hale geldi. Ders: model kötü sonuç
  verdiğinde önce promptun kendisini kontrol et.
- Yanlış pozitif veriyor. Çelişki olarak "çok büyük dosya reddedilir" ile
  "yükleme geri alınabilir" çiftini de gösterdi; bu bir çelişki değil, iki
  ayrı durum. Her bulgu okunmalı, listeye körü körüne güvenilmez.
- Aynı prompt, aynı doküman, her çalıştırmada birebir aynı sonuç gelmiyor.
  Çıktı her seferinde insan tarafından okunmalı; araç filtre, karar verici
  değil.

Dokümanda hiç geçmeyen iş kuralını da bulamıyor. "Yetkisiz kullanıcı ne olur"
sorusunu kimse yazmadıysa model de sormayabilir. O soru hâlâ analistin.

Gerçek şirket dokümanı bu araçla taranmamalı: ücretsiz katmanda gönderilen
metin Google tarafından kullanılabilir.

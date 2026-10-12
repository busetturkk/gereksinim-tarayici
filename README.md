# Gereksinim-tarayici

Gereksinim dokümanını geliştirme başlamadan önce boşluk için tarar.

## Neden

Analiz dokümanındaki eksik, UAT'de ortaya çıkınca pahalı; refinement'ta çıkınca
ucuz. Bu araç o ilk okumayı yapıyor: belirsiz ifade, test edilemez madde, eksik
kabul kriteri, çelişki, açık soru.

Çıktı bir taslak. Modelin bulduğu her şey doğru değil, bulamadığı şeyler var.
Son kararı dokümanı yazan verir — araç yerine düşünmez, önce düşündürür.

## Kullanım

`ornek.md` bu depo için uydurulmuş bir dokümandır, hiçbir şirkete ait değildir.
Bilerek boşluklu yazıldı: "hızlı", "uygun şekilde", "çok büyük" gibi ölçüsüz
ifadeler ve kabul kriteri olmayan maddeler içeriyor.

## Ne buluyor, ne bulamıyor

Buluyor: ölçüsüz kelimeler, "bitti" tanımı olmayan maddeler, bariz çelişkiler.

Bulamıyor: dokümanda hiç geçmeyen iş kuralını. "Yetkisiz kullanıcı ne olur"
sorusunu kimse yazmadıysa model de sormayabilir. O soru hâlâ analistin.

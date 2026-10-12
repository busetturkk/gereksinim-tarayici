"""Gereksinim dokümanındaki boşlukları bulur.

Kullanım:
    python3 tarayici.py gereksinim.md

Dokümanı Gemini'ye gönderir; belirsiz ifadeleri, test edilemeyen maddeleri ve
eksik kabul kriterlerini listeler. Çıktı bir taslaktır — son söz okuyanındır.
"""

import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

PROMPT = """Sen deneyimli bir iş analistisin. Aşağıdaki gereksinim dokümanını
geliştirme başlamadan önce gözden geçiriyorsun.

Şunları bul ve her biri için dokümandaki cümleyi aynen alıntıla:

1. BELİRSİZ: Birden fazla şekilde anlaşılabilecek ifadeler ("hızlı", "uygun",
   "gerektiğinde" gibi ölçüsüz kelimeler dahil).
2. TEST EDİLEMEZ: Doğru mu yanlış mı diye kontrol edilemeyecek maddeler.
3. KABUL KRİTERİ EKSİK: Yalnızca BELİRSİZ listesine girmeyen maddeler
   arasından, "bitti" sayılma şartı yazılmamış olanları seç. En fazla üç
   madde yaz; en kritik olanları seç ve neden kritik olduğunu bir cümleyle
   açıkla.
4. ÇELİŞKİ: Aynı olay için iki madde farklı sonuç tarif ediyorsa bu bir
   çelişkidir. Örnek: "Şifre üç kez yanlış girilirse hesap kilitlenir" ile
   "Kullanıcı istediği kadar deneme yapabilir" çelişir. Bu dokümanda böyle
   çiftler ara: özellikle bir madde bir durumu "hata" sayarken başka bir
   madde aynı durumu sessizce geçiştiriyorsa, ya da iki madde aynı anda
   gerçekleşirse hangisinin geçerli olduğu belli değilse. Her çift için iki
   cümleyi de alıntıla.
5. AÇIK SORULAR: Yukarıda BELİRSİZ bulduğun her ifade için iş birimine
   sorulacak somut bir soru yaz (örnek: "hızlı" kaç saniye?). Bu liste
   boş olamaz.
Dokümanda olmayan bir kuralı uydurma. Bir kategori boşsa "Yok" yaz.
Kısa ve madde madde yaz."""


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    dokuman = Path(sys.argv[1]).read_text(encoding="utf-8")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY ortam değişkeni ayarlı değil.")
        return 2

    client = genai.Client(api_key=api_key)
    cevap = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=dokuman,
        config=types.GenerateContentConfig(
            system_instruction=PROMPT,
            max_output_tokens=3000,
        ),
    )

    text = getattr(cevap, "text", None)
    if text is None and hasattr(cevap, "candidates") and cevap.candidates:
        parts = getattr(cevap.candidates[0].content, "parts", [])
        text = "".join(getattr(part, "text", "") for part in parts if getattr(part, "text", None))

    if text is None:
        print("Modelden metin yanıtı alınamadı.")
        return 3

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

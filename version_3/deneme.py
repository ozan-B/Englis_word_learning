isim_sayilari = {}
dogru_cevap = "ozan"

while True:
    kullanici_cevabi = input("Adınız nedir? (Çıkış yapmak için 'exit' yazabilirsiniz): ").lower()

    # Kullanıcı 'exit' yazarsa programdan çık
    if kullanici_cevabi == 'exit':
        break

    # Doğru cevap kontrolü
    if kullanici_cevabi == dogru_cevap:
        print("Tebrikler! Doğru cevap.")
        break

    # Yanlış cevapları sözlükte tut
    isim_sayilari[kullanici_cevabi] = isim_sayilari.get(kullanici_cevabi, 0) + 1

# Yanlış cevapları ekrana yazdır
print("\nYanlış Cevaplar ve Sayıları:")
for isim, sayi in isim_sayilari.items():
    print(f"{isim}: {sayi} kez")
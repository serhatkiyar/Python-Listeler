# Girilen yazıdaki kelime, rakam ve karakter sayısını bulan prog<<<ram?

rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

harfsayisi = 0
rakamsayisi = 0
kelimesayisi = 1

yazi = input("Bir yazı giriniz:\n>> ")


for i in yazi:
    harfsayisi += 1
    if i in rakamlar:
        rakamsayisi += 1
    if i == " ":
        kelimesayisi += 1

print(f"Bu yazı şunları içerir\n{harfsayisi} adet harf.\n{rakamsayisi} adet rakam.\n{kelimesayisi} adet kelime.")

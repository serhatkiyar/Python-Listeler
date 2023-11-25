#Girilen yazıdaki boşluk karakter sayısını bulan program?

yazi = input("Bir yazı yazınız: ")
sayac = 0


for i in yazi:
    if i == " ":
        sayac += 1


print(f"Yazdığınız yazıda {sayac} adet boşluk bulunuyor.")

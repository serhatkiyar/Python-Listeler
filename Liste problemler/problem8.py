# Girilen iki yazıyı karşılaştıran (eşit olup olmadığını bulan) program?

sayac = 1
liste = []


while True:
    yazi = input(f"{sayac}. yazıyı giriniz: ")
    liste.append(yazi)
    if sayac == 2:
        break
    sayac += 1

if liste[0] == liste[1]:
    print("Girilen iki yazı birbirinin aynısıdır.")
else:
    print("Girilen iki yazı birbirinden farklıdır.")

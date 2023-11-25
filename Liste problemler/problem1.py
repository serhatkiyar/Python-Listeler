# Girilen 5 sayının ortalamasını bulan program?

count = 1
toplam = 0


while True:
    sayi = float(input("{}. sayıyı giriniz: ".format(count)))
    count += 1
    toplam += sayi
    if count == 6:
        break


print(f"Girilen sayıların aritmek ortalaması = {toplam/5}'dir.")

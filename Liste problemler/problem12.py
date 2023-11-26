# Girilen yazıdaki aranan kelimenin önüne ve arkasına TIRNAK sembolünü ekleyen program?

yazi = input("Bir yazı giriniz: \n>> ")

kelime = input("Hangi kelimeyi tırnak işareti içerisine almak istersiniz: \n>> ")

sayac = 0
index = 0  # son harfin indexini verir

for i in yazi:
    if i == kelime[sayac]:
        sayac += 1
    else:
        sayac = 0
    index += 1
    if sayac == len(kelime):
        break

if sayac != len(kelime):
    print("Bu kelime bu metinde yer almıyor.")

yeniyazi = f'{yazi[:index - len(kelime)]}"{yazi[index - len(kelime): index]}"{yazi[index:]}'

print(yeniyazi)

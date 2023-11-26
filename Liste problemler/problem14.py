# Girilen yazıdaki bir kelimeyi sil

yazi = input("Bir yazı giriniz: \n>> ")

kelime = input("Hangi kelimeyi yok etmek istersiniz: \n>> ")

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

yeniyazi = f'{yazi[:index - len(kelime)]}{yazi[index:]}'

print(yeniyazi)

#Elemanları sıralayan program?

liste = []
counter = 1


while True:
    sayi = float(input("{}. sayıyı giriniz: ".format(counter)))
    counter += 1
    liste.append(sayi)
    girdi = input("Listeyi kaydetmek için 's' tuşuna basınız. Kaydetmek istemiyorsanız 'Enter' tuşuna basabilirsiniz: ")
    if girdi == 's':
        print("Liste Kaydedildi")
        break


liste.sort()
print(liste)

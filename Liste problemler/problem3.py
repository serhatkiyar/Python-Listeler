#Oluşturulan listede eleman sorgulama.

liste = []
counter = 1


while True:
    sayi = float(input("Listeye eklenecek {}. sayıyı giriniz: ".format(counter)))
    counter += 1
    liste.append(sayi)
    print("Listeyi kaydetmek istiyorsanız 's' yazınız. Kaydetmek istemiyorsanız 'Enter' tuşuna basınız.")
    save = input(": ")
    if save == 's':
        break


girdi = int(input("Sorgulamak istediğiniz sayıyı giriniz: "))

if girdi in liste:
    print("{} sayısı listede {}. index'te bulunuyor.".format(girdi, liste.index(girdi)))
else:
    print("{} sayısı listede bulunmuyor....".format(girdi))

# Oluşturulan listede eleman sorgulama.

liste = []
counter = 1


while True:
    sayi = input("Listeye eklenecek {}. sayıyı giriniz(Kaydetmek için 'q' tuşuna basın.): \n>> ".format(counter))
    counter += 1
    if sayi == 'q':
        print("Liste kaydedildi")
        break
    liste.append(sayi)


girdi = input("Sorgulamak istediğiniz sayıyı giriniz: ")

index = 0
sayac = 0


for i in liste:
    if girdi == i:
        break
    sayac += 1


index = sayac

if girdi in liste:
    print(f"{girdi} sayısı listede {index}. index'te bulunuyor.")
else:
    print("{} sayısı listede bulunmuyor....".format(girdi))

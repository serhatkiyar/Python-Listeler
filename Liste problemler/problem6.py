# Her elemanın tekrar sayısını bulan program?
liste = []
counter = 1


while True:
    sayi = input(f"{counter}. Sayıyı giriniz(Kaydetmek için 'q' tuşuna basınız): ")
    counter += 1
    if sayi == 'q':
        print("Liste Kaydedildi")
        break
    else:
        liste.append(int(sayi))


sayi_bul = input("Oluşturulan listedeki tekrar sayısını bulmak istediğiniz sayıyı giriniz(Bütün tekrar sayıları için 'a' tuşuna basınız.): ")

if sayi_bul in liste:
    print("{} sayısı oluşturulan listede {} kez tekrar ediliyor.".format(sayi_bul, liste.count(int(sayi_bul))))
else:
    print("{} sayısı oluşturulan listede bulunmuyor....".format(sayi_bul))
if sayi_bul == "a":
    sozluk = {}


    for i in liste:
        sayac = 0
        for x in liste:
            if i == x:
                sayac += 1
        sozluk[i] = sayac
    for i in sozluk:
        print(f"{i} sayısı {sozluk[i]} kez tekrarlanmıştır.")

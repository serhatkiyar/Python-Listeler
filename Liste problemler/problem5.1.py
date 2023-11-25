# **********Elemanları sıralayan program?*********

liste = []
sayac = 1  # sayac' ı kaç defa sayı girildiğini göstermek için kullandık. Her sayı ekleme işlemi ile
# beraber sayac' ın değerini arttırdık.


sayi = int(input(f"{sayac}. sayıyı giriniz: "))  # ilk alıcağımız sayıyı döngüye koymadım çünkü
sayac += 1  # elemanlı listeyi sıralamaya gerek yok ve döngü dışındaki tek farkı 'q' kaydetme seçeneğinin olmaması.
liste.append(sayi)


while True:  # sayi 'q' ya eşit olana kadar döngü çalışır.

    sayi = input(f"{sayac}. sayıyı giriniz(Kaydetmek için 'q' tuşuna basınız): ")
    sayac += 1

    if sayi == 'q':
        print("Liste Kaydedildi")
        break
    else:  # Elemanları listeye ekliyerek sıralıcağımız listeyi oluşturuyoruz.
        liste.append(int(sayi))


# Burada referans olarak indexleri alıp ikili ikili şekilde sayıları kıyaslayıp büyük olanı büyük indexe yerleştirir.
for i in range(len(liste)):
    for j in range(0, len(liste) - i - 1):  # Burada i' yi çıkarmamızın sebebi gereksiz kod çalıştırılmaması
        if liste[j] > liste[j + 1]:        # için çünkü büyük olan sayı her nerde olursa olsun ilk döngüde en büyük
            liste[j], liste[j + 1] = liste[j + 1], liste[j]  # index' e yerleşecektir.


print(liste)

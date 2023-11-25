# kullanıcıdan öğrenci adını ve üç sınav notunu girmesini isteyin.
# Kullanıcı 'q' tuşuna basana kadar bu işlemi tekrarlansın. Ardından,
# öğrenci not bilgilerini ekrana yazdırın, her öğrencinin adını,
# notlarını ve ortalama notunu gösteren programı yazınız.

sozluk = {}
sayac = 1


while True:
    isim = input(f"{sayac}. Öğrenci: ")
    sayac += 1
    liste = []
    for i in range(1, 4):
        sinav = int(input("{}. sınav sonucunu giriniz:".format(i)))
        liste.append(sinav)
    sozluk[isim] = liste
    bas = input("Kaydetmek için 'q' tuşuna, devam etmek için ise 'Enter' tuşuna basınız: ")
    if bas == "q":
        break


for x in sozluk:
    print(f"{x} isimli öğrencinin:", end="")
    print(f" 1.Notu: {sozluk[x][0]} / 2.Notu: {sozluk[x][1]} / 3.Notu: {sozluk[x][2]} / ", end="")
    print(f"Ortalaması= {(sozluk[x][0] + sozluk[x][1] + sozluk[x][2])/3}")

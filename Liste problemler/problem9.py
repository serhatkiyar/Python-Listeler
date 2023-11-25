# Girilen yazının büyük yazılıp yazılmadığını bulan program?

alfabe = []
for i in "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ":
    alfabe.append(i)

yazi = input("Bir yazı kelime yazınız: ")

if yazi[0] in alfabe:
    print("{} yazısı büyük harf ile başlıyor.".format(yazi))
else:
    print(("{} yazısı büyük harf ile başlamıyor.".format(yazi)))

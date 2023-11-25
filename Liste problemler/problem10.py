# Girilen yazının k. karakteriyle r. karakteri arasını kopyalayan programı yazınız?

yazi = input("Bir yazı yazınız: ")

print("Bu yazıda {} adet karakter var. Kaçıncı karakterler arasını kopyalamk istersiniz: ".format(len(yazi)))

index_1 = int(input("1. Karakter: "))
index_1 -= 1
index_2 = int(input("2. Karakter: "))

print(yazi[index_1:index_2])

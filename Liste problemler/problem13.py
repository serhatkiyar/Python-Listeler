# Girilen yazıdaki bir karakteri sil

karakterinindexi = []
indexer = 0

yazi = input("Bir yazı giriniz: \n>> ")

karakter = input("Hangi karakteri silmek istiyorsunuz: \n>> ")


for i in yazi:
    if karakter == i:
        karakterinindexi.append(indexer)
        indexer -= 1
    indexer += 1


for i in karakterinindexi:
    yazi = f"{yazi[:i]}{yazi[i+1:]}"


print(yazi)

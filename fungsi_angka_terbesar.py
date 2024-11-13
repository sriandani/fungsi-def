def angkaterbesar (angka1,angka2,angka3):
    if ((angka1 > angka2) and (angka1 > angka3)):
        return angka1
    elif ((angka2 > angka1) and (angka2 > angka3)):
        return angka2
    else:
        return angka3
a = float(input("masukkan angka 1: "))
b = float(input("masukkan angka 2: "))
c = float(input("masukkan angka 3: "))
angka_max = max(a,b,c)
print ("nilai maksimal dari ",a,",",b,"dan",c,"adalah", angka_max)

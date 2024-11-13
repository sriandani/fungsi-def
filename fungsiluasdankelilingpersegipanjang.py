def luaspersegipanjang (panjang, lebar):
    return panjang * lebar
def keliling (panjang,lebar):
    return 2* (panjang + lebar)
a = float(input("masukkan panjang: "))
b = float(input("masukkan lebar: "))
hasil_luas = luaspersegipanjang (a,b)
hasil_keliling = keliling (a,b)
print ("hasil luas adalah:",hasil_luas)
print ("hasil keliling adalah:",hasil_keliling)

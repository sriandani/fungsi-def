def factorial (n) :
    if n==0 or n==1 :
        return 1
    else:
        return n*(factorial(n-1))
a=int(input("masukkan nilai yang akan dicari: "))
cari_factorial=factorial(a)
print("nilai dari ", a,"! adalah ", cari_factorial)

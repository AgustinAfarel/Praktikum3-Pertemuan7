angka1=0
while True:
    bilangan1 = int(input("Masukkan Bilangan : "))
    if (angka1 < bilangan1):
        angka1=bilangan1
    if (bilangan1 == 0):
        break

print("Bilangan terbesar adalah: ",angka1)
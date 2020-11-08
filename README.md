# Praktikum3-Pertemuan7
Dibuat untuk memenuhi tugas bahasa pemrograman

NAMA   : AGUSTIN AFAREL

NIM    :312010081

KELAS  :TI.20.B.1.

MATKUL :BAHASA PEMROGRAMAN

### LATIHAN 1
1.Menampilkan bilangan N  yang lebih kecil dari 0.5 <br>
 
```python

 n=int(input("Masukkan Nilai N : "))

import random

for data in list(range(1, n+1, 1)):
    print(f"Data ke: {data} ->",random.uniform(0, 0.5))

print()
```

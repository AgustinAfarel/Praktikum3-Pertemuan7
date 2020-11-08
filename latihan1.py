n=int(input("Masukkan Nilai N : "))

import random

for data in list(range(1, n+1, 1)):
    print(f"Data ke: {data} ->",random.uniform(0, 0.5))

print()
uang = 100000000

for bln in range(1, 9, 1):
    # Menentukan Keuntungan pada bln ke 1 dan ke 2
    if (bln >= 1) and (bln <= 2):
        # keuntungan bln 1 dan 2 adalah 0%
        keuntungan12 = uang * 0
        print(f"keuntungan bln ke {bln} : {keuntungan12}")

    if (bln >= 3) and (bln <= 4):
        # keuntungan bln 3 dan 4 adalah 1%
        keuntungan34 = uang * 0.01
        print(f"keuntungan bln ke {bln} : {keuntungan34}")

    if (bln >= 5) and (bln <= 7):
        # Kentungan bln 5, 6, 7 adalah 5%
        Keuntungan567 = uang * 0.05
        print(f"keuntungan bln ke {bln} : {Keuntungan567}")

    if bln == 8:
        keuntungan8 = uang * 0.03
        print(f"keuntungan bln ke {bln} : {keuntungan8}")

totalkeuntungan = keuntungan12+keuntungan12+keuntungan34+keuntungan34+Keuntungan567+Keuntungan567+Keuntungan567+keuntungan8

print(f"\nTotal keuntungan adalah : {totalkeuntungan}")
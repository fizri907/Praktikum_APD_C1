Nama = input("Masukan Nama Anda: ")
Hari = input("Masukan hari yang anda inginkan: ")
Uang = int(input("Masukan uang yang anda miliki: "))

Hargatiket = 0
if Hari == "senin" or "Selasa" or "Rabu" or "kamis" :
    if Uang >= 40000:
        print(f"Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari {Hari} ")
    else:
        print("MISKIN LO!!! skip dulu")
elif Hari == "Jumat":
    if Uang >= 45000 : 
        print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Jumat")
    else:
        print("MISKIN LO!!! skip dulu")
elif Hari == "Sabtu": 
    if Uang >= 50000 :
        print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Sabtu")
    else:
        print("MISKIN LO!!! skip dulu")
elif Hari == "Minggu": 
    if Uang >= 55000: 
        print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Minggu")
    else:
        print("MISKIN LO!!! skip dulu")

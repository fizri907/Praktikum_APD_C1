loop = 0
while loop < 3:

    username = input("Masukan username Anda: ")
    password = int(input("Masukan password anda:"))
    if username == "Muhammad.fizriannur" and password == 105:
        lanjut = input("Mau Lanjut apa nda?: ")
        if lanjut =="Gx mau":
            print("Program dihentikan")
    else:
        print("Mantap, lanjut ke tahap berikutnya")
    Hari = input("Masukan hari:")
    Uang = int(input("Uang yang dimiliki: "))
    if Hari == "Senin" or "Selasa" or "Rabu" or "Kamis" :
        if Uang >= 40000:
            print(f"Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari {Hari} ")
            break
        else:
            print("MISKIN LO!!! skip dulu")
            break
    elif Hari == "Jumat":
        if Uang >= 45000 : 
            print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Jumat")
            break
        else:
            print("MISKIN LO!!! skip dulu")
            break
    elif Hari == "Sabtu": 
        if Uang >= 50000 :
            print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Sabtu")
            break
        else:
            print("MISKIN LO!!! skip dulu")
            break
    elif Hari == "Minggu": 
        if Uang >= 55000: 
            print("Selamat!!! anda termasuk golongan billgeth untuk membeli tiket hari Minggu")
            break
        else:
            print("MISKIN LO!!! skip dulu")
            break
    else:
        print("Hari apa yang yng kau masukan leeee")
        break
else:
    print("username atau password yang anda masukan salah")
    lanjut = input("Ingin Lanjut apa nda?: ")
    if lanjut == "gx mau" : 
        print("program sudah berhenti")
    else:
        loop = loop + 1
        print(f"Anda sudah mencoba sebanyak {loop} kali: ")
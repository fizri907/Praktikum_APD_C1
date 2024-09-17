nama = input("Masukkan Nama: ")
nim  = input("Masukkan Nim :")
HargaGula = 21000

DiskonGulaku = 0.07 
DiskonManisKita = 0.11
DiskonGunungMadu = 0.13

HSDgulaku = HargaGula - (HargaGula * DiskonGulaku)
HSDmaniskita = HargaGula - (HargaGula * DiskonManisKita)
HSDgunungmadu = HargaGula - (HargaGula * DiskonGunungMadu)

output = (
    f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {HargaGula}"
    f"Jika dia membeli Gulaku ia harus membayar {HSDgulaku} Setelah mendapat diskon 7%"
    f"Jika dia membeli Manis Kita ia harus membayar {HSDmaniskita} Setelah mendapat diskon 11%"
    f"Jika dia membeli Gunung Madu ia harus membayar {HSDgunungmadu}setelah mendapat diskon 13%"
        )
print(output) 

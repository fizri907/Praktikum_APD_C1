nama = input("Muhammad Fizriannur")
nim  = input("2409106105")
HargaGula = 21000

DiskonGulaku = 0.07 
DiskonManisKita = 0.11
DiskonGunungMadu = 0.13

DiskonGulaku = HargaGula * DiskonGulaku
DiskonManisKita = HargaGula * DiskonManisKita
DiskonGunungMadu = HargaGula * DiskonGunungMadu

HSDgulaku = HargaGula - (HargaGula * DiskonGulaku)
HSDmaniskita = HargaGula - (HargaGula * DiskonManisKita)
HSDgunungmadu = HargaGula - (HargaGula * DiskonGunungMadu)
 
print=(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {HargaGula}")
print=(f"Jika dia membeli Gulaku ia harus membayar {HSDgulaku} Setelah mendapat diskon 7%")
print=(f"Jika dia membeli Manis Kita ia harus membayar {HSDmaniskita} Setelah mendapat diskon 11%")
print=(f"Jika dia membeli Gunung Madu ia harus membayar {HSDgunungmadu}setelah mendapat diskon 13%")
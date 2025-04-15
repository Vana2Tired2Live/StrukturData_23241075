# TUGAS (?)
# -----5+++++++9------12++++++30--------
MasukkanBilangan = float(input("Masukkan Bilangan: "))

LehDar = (MasukkanBilangan > 5)
print("Lebih dari 5:", LehDar)
KurDar = (MasukkanBilangan < 9)
print("Kurang dari 9:", KurDar)
LehDar2 = (MasukkanBilangan > 12)
print("Lebih dari 12:", LehDar2)
KurDar2 = (MasukkanBilangan < 30)
print("Kurang dari 30:", KurDar2)

Antara = (LehDar and KurDar and LehDar2 and KurDar2)
print("Pengecekan Final = ", Antara)


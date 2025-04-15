# Perbandingan Lanjutan

#++++++3 -------- 9+++++++
MasukkanBilangan = float(input("Masukkan Bilangan kurang dari 3 atau lebih dari 9: "))

#-----Cek kurang dari 3
KurDar = (MasukkanBilangan < 3)
print("Kurang dari 3:", KurDar)

#-----Cek lebih dari 9
LehDar = (MasukkanBilangan > 9)
print("Lebih dari 9:", LehDar)

Betul = KurDar or LehDar
print("Pengecakan Final = ", Betul)


# -----4+++++++14-----
MasukkanBilangan = float(input("Masukkan Bilangan antara 4 dan 14: "))

LehDar = (MasukkanBilangan > 4)
print("Lebih dari 4:", LehDar)
KurDar = (MasukkanBilangan < 14)
print("Kurang dari 14:", KurDar)

Antara = (LehDar and KurDar)
print("Pengecekan Final = ", Antara)


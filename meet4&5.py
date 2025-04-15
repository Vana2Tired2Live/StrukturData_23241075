#Inputan dari user
#Aritmatika

#Belajar Inputan
vill = input("Masukkan Kata: ")
print("Isi dari vill: ", vill, "Bertipe Data: ", type(vill))

#Belajar Aritmatika Dasar
x = 5
y = 5

#Penjumlahan +
hasil = x + y
print("x + y = ", hasil)

#Pengurangan - 
hasil = x - y
print("x - y = ", hasil)

#Perkalian *
hasil = x * y
print("x * y = ", hasil)

#Pembagian /
hasil = x / y
print("x / y = ", hasil)

#Perpangkatan Exponen **
hasil = x ** y
print("x ^ y = ", hasil)

#Modulus %
hasil = y % x
print("x mod y = ", hasil)

#Floor Division (Pembulatan Kebawah) //
hasil = y // x
print("x // y = ", hasil)

#Aritmatika Prioritas
#(), Exponen, Perkalian/Pembagian, Penjumlahan/Pengurangan
a = 6
b = 2
c = 9

hasil = (a ** b * (c + a) / b - c % x // y)
print(hasil)

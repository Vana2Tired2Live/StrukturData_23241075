# Perbandingan
# Tanda Lebih Besar >
# Tanda Lebih Kecil <
# Tanda Lebih Besar Sama Dengan >=
# Tanda Lebih Kecil Sama Dengan <=
# Tanda Sama Dengan ==
# Tanda Tidak Sama Dengan !=
# Sama "is"
# Tidak Sama "is not"

x = 4
y = 5

# Lebih Besar >
hasil = x > y
print(x, ">", y, "adalah", hasil)

# Lebih Kecil <
hasil = x < y
print(x, "<", y, "adalah", hasil)

# Lebih Besar Sama Dengan >=
hasil = x >= y
print(x, ">=", y, "adalah", hasil)

# Lebih Kecil Sama Dengan <=
hasil = x <= y
print(x, "<=", y, "adalah", hasil)

# Sama Dengan ==
hasil = x == 2
print(x, "==", 2, "adalah", hasil)

# Tidak Sama Dengan !=
hasil = x != 3
print(x, "!=", 3, "adalah", hasil)

# (>), (<), (>=), (<=), (==), (!=) adalah perbandingan literal
# x = 4, 4 = literal (tidak memakan memori)
# x = object
#
# x = 4 (bisa)
# x is 4 (tidak bisa, karena yang dibandingkan adalah literal)
# x is y (bisa, karena yang dibandingkan adalah object)

# is dan is not
hasil = x is 4
print(x, "is", 4, "adalah", hasil)

hasil = x is not 4
print(x, "is not", 4, "adalah", hasil)
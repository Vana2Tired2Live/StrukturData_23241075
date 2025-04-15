# Tabel Kebenaran (Logika Bolean)
# "not", "and", "or", "xor"

#NOT
print("==={ LOGIKA NOT }===")
x = False
y = not x
print('value x =', x)
print("*******NOT******")
print('value y =', y)

# OR (Semua bernilai true asalkan ada true nya)
# Berlaku bagi Cewek wkwkwkwk
print("====={ LOGIKA OR }=====")
x = False
y = False
z = x or y
print(x, "or", y, "=", z)

x = False
y = True
z = x or y
print(x, "or", y, "=", z)

x = True
y = False
z = x or y
print(x, "or", y, "=", z)

x = True
y = True
z = x or y
print(x, "or", y, "=", z)

# AND (Hanya bernilai true, ketika keduanya true)
# Berlaku bagi Cowok wkwkwkwk
print("====={ LOGIKA AND }=====")

x = False
y = False
z = x and y
print(x, "and", y, "=", z)

x = False
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x = True
y = True
z = x and y
print(x, "and", y, "=", z)

# XOR (Jika keduanya sama, hasilnya false, sisanya bertuliskan true)
print("====={ LOGIKA XOR }=====")
x = False
y = False
z = x ^ y
print(x, "xor", y, "=", z)

x = False
y = True
z = x ^ y
print(x, "xor", y, "=", z)

x = True
y = False
z = x ^ y
print(x, "xor", y, "=", z)

x = True
y = True
z = x ^ y
print(x, "xor", y, "=", z)
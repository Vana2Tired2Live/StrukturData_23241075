# LATIHAN PERTEMUAN KE-10

app = input("Ketik 1 untuk Penjumlahan atau ketik 2 untuk pengurangan : ")

if app == "1":
    print("Memulai Penjumlahan...")
    x = input("Masukkan bilangan pertama : ")
    y = input("Masukkan bilangan kedua : ")
    
    # Konversi input ke integer (atau float jika perlu)
    x = int(x)
    y = int(y)
    
    hasil = x + y
    print(x, "+", y, "=", hasil)
    print("Proses Penghitungan selesai ^^")
elif app == "2":
    print("Memulai Pengurangan...")
    x = input("Masukkan bilangan pertama : ")
    y = input("Masukkan bilangan kedua : ")
    
    # Konversi input ke integer (atau float jika perlu)
    x = int(x)
    y = int(y)
    
    hasil = x - y
    print(x, "-", y, "=", hasil)
    print("Proses Penghitungan selesai ^^")
else:
    print("!!ERROR!!")
    print("Tidak bisa memproses karena angka tidak termasuk dalam daftar X_x")
    

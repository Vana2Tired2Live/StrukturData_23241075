 # Program untuk menghitung jumlah total dari angka-angka yang dimasukkan pengguna

# Inisialisasi variabel untuk menyimpan jumlah total
total = 0

# Meminta pengguna untuk memasukkan jumlah angka yang ingin dijumlahkan
n = int(input("Masukkan jumlah angka yang ingin dijumlahkan: "))

# Menggunakan loop untuk meminta input angka dan menambahkan ke total
for i in range(n):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    total += angka

# Menampilkan jumlah total
print(f"Jumlah total dari angka-angka yang dimasukkan adalah: {total}")

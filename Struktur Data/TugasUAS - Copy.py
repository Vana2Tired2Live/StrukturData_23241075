import random

def main():
    print("Selamat datang di permainan tebak angka!")
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0
    
    while tebakan != angka_rahasia:
        tebakan = int(input("Tebak angka antara 1 dan 100: "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah!")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi!")
        else:
            print(f"Selamat! Anda telah menebak angka dengan benar dalam {percobaan} percobaan.")

if __name__ == "__main__":
    main()

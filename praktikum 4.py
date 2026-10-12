#Muhammad Ilham Ramadhan
#065002600006
#Algoritma dan Pemrogaman s- Struktur Kendali II (Control Structure II)
for baris in range(7, 0, -1):
    for kolom in range(baris):
        print(baris, end="")
    print()

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan == 2:
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            hari = 29
        else:
            hari = 28
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        hari = 30
    elif 1 <= bulan <= 12:
        hari = 31
    else:
        print("Bulan tidak valid!")
        continue

    print("Jumlah hari:", hari)
    break

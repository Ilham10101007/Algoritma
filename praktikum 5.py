#Muhammad Ilham Ramadhan
#065002600006
#Struktur Kendali - Latihan
#Latihan 1
def konversi_nilai(huruf):
    nilai = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.25
    }

    return nilai.get(huruf, 0)


jumlah = int(input("Masukkan jumlah nilai: "))

total = 0
i = 1

while i <= jumlah:
    huruf = input("Masukkan kategori huruf: ").upper()
    peringkat = konversi_nilai(huruf)

    total = total + peringkat
    i = i + 1

rata_rata = total / jumlah

print("Total nilai =", format(total, ".2f"))
print("Rata-rata nilai =", format(rata_rata, ".2f"))

#Latihan 2
def harga_tiket(umur):
    harga = 23
    harga = harga - (umur <= 12) * 9
    harga = harga - (umur <= 2) * 14
    harga = harga - (umur >= 65) * 5
    return harga


total = 0
umur = input("masukkan umur: ")

while umur != "":
    umur = int(umur)
    harga = harga_tiket(umur)

    print("Gratis" * (harga == 0) or
          "Harga ${:.2f}".format(harga))

    total = total + harga
    print("Running total: {:.2f}".format(total))

    umur = input("masukkan umur: ")

uang = float(input("masukkan jumlah uang: "))

kembalian = uang - total

while kembalian < 0:
    print("Uang kurang!")
    uang = float(input("masukkan jumlah uang: "))
    kembalian = uang - total

print("Running kembalian: {:.2f}".format(kembalian))

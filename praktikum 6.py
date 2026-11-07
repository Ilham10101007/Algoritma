#Muhammad Ilham Ramadhan
#065002600006
#Struktur Kendali - Latihan

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


def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False


def jumlah_hari(bulan, tahun):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 0


print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))

    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break

    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid")
        continue

    tahun = int(input("masukkan tahun: "))

    hari = jumlah_hari(bulan, tahun)

    print(hari, "hari dalam bulan")

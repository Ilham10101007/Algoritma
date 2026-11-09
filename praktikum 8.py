#Muhammad Ilham Ramadhan
#065002600006
#Fungsi Rekursif

#Latihan Pertama
def penjumlahan(jumlah, total=0, urutan=1):
    if urutan > jumlah:
        return total

    angka = int(input(f"Masukkan angka ke-{urutan}: "))
    total += angka

    return penjumlahan(jumlah, total, urutan + 1)


def mulai_penjumlahan():
    jumlah = int(input("Masukkan Jumlah: "))
    hasil = penjumlahan(jumlah)

    print("Hasil dari penjumlahan adalah:", hasil)


mulai_penjumlahan()

#Latihan Kedua
def perpangkatan(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / perpangkatan(base, -power)
    else:
        return base * perpangkatan(base, power - 1)


def program():
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")

    angka = input("Masukkan Angka: ")

    if angka == "":
        print("Program Selesai")
        return

    pangkat = int(input("Masukkan Pangkatnya: "))

    hasil = perpangkatan(int(angka), pangkat)

    print("Hasilnya adalah:", hasil)
    print()

    program()


program()


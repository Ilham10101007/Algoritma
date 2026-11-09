#Muhammad Ilham Ramadhan
#065002600006
#Fungsi pada Pemrograman Python - Latihan

#Latihan Pertama
def cek_prima(angka):
    if angka <= 1:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True


def tampilkan_hasil(angka):
    if cek_prima(angka):
        print(angka, "adalah bilangan Prima")
    else:
        print(angka, "bukanlah bilangan Prima")


bilangan = int(input("Masukkan angka: "))
tampilkan_hasil(bilangan)

#Latihan Kedua
def ordinal(angka):
    if angka % 10 == 1:
        return (angka, 'st')
    elif angka % 10 == 2:
        return (angka, 'nd')
    elif angka % 10 == 3:
        return (angka, 'rd')
    else:
        return (angka, 'th')


def mulai_program():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")

    while True:
        angka = int(input("masukkan angka: "))
        hasil = ordinal(angka)
        print(hasil)

        if angka == 0:
            break

    print("terima kasih telah menggunakan program saya")


mulai_program()

print("Ini Adalah Program Pembagian")

while True:
    try:
        Penyebut = int(input("Masukkan Angka Penyebut     : "))
        Pembilang = int(input("Masukkan Angka Pembilang    : "))
        Hasil = Penyebut / Pembilang
        break
    except ValueError:
        print("Yang Anda Masukkan Bukan Angka!")
    except ZeroDivisionError:
        print("Tidak Boleh Memasukkan Angka 0 Pada Pembilang!")
    except Exception as err:
        print(err)

print("Berhasil, Anda Memasukkan Angka: ", Hasil)

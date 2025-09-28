# MINI_PROJECT_2 - "SISTEM REMINDER TUGAS"
# Nama : Vidya Khansa Mizan
# NIM : 2509116052, Sistem Informasi B'2025
# Mata kuliah : Praktikum Dasar-Dasar Pemrograman

from prettytable import PrettyTable 
import pwinput

datalogin = {
    "Mahasiswa" : "2509116052",
    "Admin" : "aamiin"
}

def login():
    while True:
        print("\n")
        print("-"*25)
        print("pick a role, any rolee ^^")
        print("1. Mahasiswa")
        print("2. Admin")
        print("-"*25)
        try:
            pilih = int(input("nomor 1 atau 2? "))
        except ValueError:
            print("\ntolongg, masukkan dalam bentuk angkaaa\n")
            continue
        except KeyboardInterrupt:
            print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
            continue
        except EOFError:
            print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
            continue

        if pilih == 1 or pilih == 2:
            print("\n")
            print("-"*35)
            print("--- LOGIN SISTEM REMINDER TUGAS ---")
            print("-"*35)
            try:
                nama = input("masukkan nama lengkap anda: ")
            except EOFError:
                print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
                continue
            except KeyboardInterrupt:
                print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
                continue

            if pilih == 1:
                kesempatan = 3
                while kesempatan > 0:
                    try:
                        password = pwinput.pwinput("masukkan password anda (NIM): ")
                    except EOFError:
                        print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
                        continue
                    except KeyboardInterrupt:
                        print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
                        continue

                    if password == datalogin["Mahasiswa"]:
                        print(f"\nwelcome backkk, {nama} (Mahasiswa). Selamat menggunakan sistem iniii yeaaa\n")
                        return "Mahasiswa"
                    
                    else:
                        kesempatan -= 1
                        if kesempatan > 0:
                            print(f"\nmohon maaff, sepertinya ada kesalahan di input password. Sisa percobaan kamu: {kesempatan}\n")
                    
                print("\nmohon maaff kesempatanmu sudah habiss... Try again later yaa<3")
                exit()

            elif pilih == 2:
                kesempatan = 3
                while kesempatan > 0:
                    try:
                        password = pwinput.pwinput("masukkan password anda: ")
                    except EOFError:
                        print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
                        continue
                    except KeyboardInterrupt:
                        print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
                        continue

                    if password == datalogin["Admin"]:
                        print(f"\nwelcome backkk, {nama} (Admin). Selamat menggunakan sistem iniii yeaaa\n")
                        return "Admin"
                    
                    else:
                        kesempatan -= 1
                        if kesempatan > 0:
                            print(f"\nmohon maaff, sepertinya ada kesalahan di input password. Sisa percobaan kamu: {kesempatan}\n")
                    
                print("\nmohon maaff kesempatanmu sudah habiss... Try again later yaa<3\n")
                exit()

        else:
            print("\nmaafff, pilihannya hanya 1 atau 2..")

role = login()

print("beralih ke halaman utama...\n")

tugas_deadline = [
    ["Ringkasan Agama 6 Pertemuan", "18 September 2025"],
    ["Study Case 2", "12 September 2025"],
    ["MinPro 1 Praktikum DDP", "14 September 2025"],
    ["Tugas Pendidikan Pancasila", "17 September 2025"],
    ["Diagram Fishbone", "17 September 2025"],
    ["MinPro 1 Praktikum PTI", "20 September 2025"]
]

def pilihyuks(role):
    print("--- SELAMAT DATANG KE MENU PILIHAN ---")
    table = PrettyTable()
    table.field_names = ["No.", "Menu Pilihan"]

    if role == "Mahasiswa":
        table.add_row([1, "Lihat List Tugas"])
        table.add_row([2, "Exit"])

    elif role == "Admin":
        table.add_row([1, "Lihat List Tugas"])
        table.add_row([2, "Tambah Tugas"])
        table.add_row([3, "Edit Tugas"])
        table.add_row([4, "Hapus Tugas"])
        table.add_row([5, "Exit"])
    print(table)

    try:
        tanyaa = int(input("Ketik nomor menu yang dituju: "))
        return tanyaa
    except ValueError:
        print("Tolong masukkan dalam bentuk angka:D")
        return None

def menu1():
    print("\nbaikk, berikut ini adalah list tugas kamu di bulan ini: ")
    table = PrettyTable()
    table.field_names = ["No.", "Nama Tugas", "Deadline"]

    for i, (tugas, deadline) in enumerate(tugas_deadline, start = 1):
        table.add_row([i, tugas, deadline])

    print(table)
    print("\nbanyak jugaa yaa, yukk nyicil dari sekarang (˵•̀ ᴗ-˵)✧\n")

def menu2():
    print("\nbaikk, Isilah format di bawah ini!")
    try:
        nama = input("Nama tugas:  ")
        deadline = input("Deadline/Tenggat: ")

        neww_tasks = ([nama, deadline])
        tugas_deadline.append(neww_tasks)
        print("\nTugas sudah ditambahkann^^\n")
        return

    except KeyboardInterrupt:
        print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
        return
    except EOFError:
        print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
        return


def menu3():
    kamunanyea = input("\nTugas apaaa yang mau kamu update?? ")
    print("\nokeeyy, isilah format di bawah inii:")
    for i, tugas in enumerate(tugas_deadline):
        if tugas[0] == kamunanyea:
            try:
                namabaru = input("Masukkan nama terbaru tugas: ")
                dlbaru = input("Masukkan deadline/tenggat terbaru: ")

                if namabaru:
                    tugas_deadline[i][0] = namabaru
                if dlbaru:
                    tugas_deadline[i][1] = dlbaru

                print(f"\nyippieee tugas kamu berhasil diupdate menjadi '{tugas_deadline[i]}'\n")
                break

            except KeyboardInterrupt:
                print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
                return
            except EOFError:
                print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
                return
    else:
        print(f"\nhmmmmzz, sepertinya tugas '{kamunanyea}' tidak bisaa ditemukan...\n")
    return

def menu4():
    try:
        nama = input("\nTugas apaa yang ingin kamu hapuss?? ")
        for i, tugas in enumerate(tugas_deadline):
            if tugas[0] == nama:
                del tugas_deadline[i]
                print(f"\nokeeeyy, tugas '{nama}' berhasil dihapus dari list inii :3\n")
                break
        else:
            print("\nmohon maaff, tugas yang kamu cari tidak dapat sistem temukan...\n")
        return

    except KeyboardInterrupt:
        print("\nMohon untuk tidak menekan tombol ctrl c terlebih dahulu yaaa\n")
        return
    except EOFError:
        print("\nMohon untuk tidak menekan tombol ctrl z + enter terlebih dahulu ^^\n")
        return


while True:
    ygmana = pilihyuks(role)
    if role == "Mahasiswa":
        if ygmana == 1:
            menu1()
        elif ygmana == 2:
            print("\nokeeyy, terimakasihh karna sudah menggunakan sistem iniii\n")
            break
        else:
            print("\nmohonn pilih angka sesuai dengan menu yang terteraa\n")
            exit()

    if role == "Admin":
        if ygmana == 1:
            menu1()
        elif ygmana == 2:
            menu2()
        elif ygmana == 3:
            menu3()
        elif ygmana == 4:
            menu4()
        elif ygmana == 5:
            print("\nokeeyy, terimakasihh karna sudah menggunakan sistem iniii\n")
            break
        else:
            print("\nmohonn pilih angka sesuai dengan menu yang terteraa\n")
            exit()
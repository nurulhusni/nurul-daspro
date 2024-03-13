def hitung_gaji_harian(gaji_pokok):
    return gaji_pokok / 8

def hitung_gaji_mingguan(gaji_pokok):
    return gaji_pokok / 48

def main():
    nama_karyawan = input("Nama karyawan: ")
    gaji_pokok = float(input("Masukkan gaji pokok: "))
    jam_kerja_per_hari = 8

    print("\nNama karyawan:", nama_karyawan)
    print("Gaji pokok:", gaji_pokok)
    print("Jumlah jam kerja per hari:", jam_kerja_per_hari,"Jam")

    print("\nPilih Rincian Gaji Mingguan/Harian:")
    print("1. Gaji Harian")
    print("2. Gaji Mingguan")
    pilihan = int(input("Pilih [1/2]: "))

    if pilihan == 1:
        gaji_harian = hitung_gaji_harian(gaji_pokok)
        print("Gaji harian:", gaji_harian)
    elif pilihan == 2:
        gaji_mingguan = hitung_gaji_mingguan(gaji_pokok)
        print("Gaji mingguan:", gaji_mingguan)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 1: Membuat Fungsi Load Data
# ================================

nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}  # inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(',')
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
    return data_dict


# buka_data = baca_data(nama_file)
# print("jumlah data terbaca", len(buka_data))

# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 2: Membuat Fungsi Menampilkan Data
# ================================

def tampilkan_data(data_dict):
    # Membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM':<10} | {'Nama':<50} | {'Nilai':<5}")
    print("-" * 40)
    # Menampilkan setiap data mahasiswa
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<50} | {int(nilai):>5}")
    print("-" * 40)

# tampilkan_data(buka_data)

# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 3: Membuat Fungsi Mencari Data
# ================================

def cari_data(data_dict):
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ")
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("===Data Mahasiswa Ditemukan===")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData Mahasiswa Tidak Ditemukan. Pastikan NIM yang Anda masukkan benar.")

# cari_data(buka_data)

# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 4: Membuat Fungsi Update Data
# ================================
def ubah_data(data_dict):
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan dalam data. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# Memanggil fungsi ubah data
# ubah_data(buka_data)

# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 5: Membuat Menyimpan data pada file
# ================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# Memanggil fungsi simpan data
# simpan_data(nama_file, buka_data)
# print("\nData berhasil disimpan ke file: ", nama_file)

# ================================
# Praktikum 2: Konsep ADT dan File Handling (Studi Kasus)
# Latihan Dasar 6: Membuat menu interaktif
# ================================

def main():
    buka_data = baca_data(nama_file)
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            tampilkan_data(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            ubah_data(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file, buka_data)
            print("\nData berhasil disimpan ke file:", nama_file)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
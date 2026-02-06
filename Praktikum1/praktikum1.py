# ================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1: Membaca seluruh isi file data
# ================================

# print("===Membuka file dalam satu string===")
# with open('data_mahasiswa.txt', 'r', encoding="utf-8") as file:
#     isi_file = file.read()

# print(isi_file)

# print("===Membuka file per baris===")
# jumlah_baris = 0
# with open('data_mahasiswa.txt', 'r', encoding="utf-8") as file:
#     for baris in file:
#         jumlah_baris += 1
#         print(f'Baris ke-{jumlah_baris}: {baris.strip()}')

# ================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 2: Parsing data
# ================================

# Parsing baris menjadi data satuan
# print("===Parsing data mahasiswa===")
# with open('data_mahasiswa.txt', 'r', encoding="utf-8") as file:
#     for baris in file:
#         baris = baris.strip()
#         nim, nama, nilai = baris.split(',')
#         print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai)


# ================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca data dan menyimpannya ke struktur data list
# ================================
# hasil = []
# with open('data_mahasiswa.txt', 'r', encoding="utf-8") as file:
#     for baris in file:
#         baris = baris.strip()
#         nim, nama, nilai = baris.split(',')
#         hasil.append([nim, nama, nilai])

# print("====Menampilkan List====")
# print(hasil)
# print("Contoh Record ke 1", hasil[0])
# print("Contoh Record ke 2", hasil[1])


# ================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca data dan menyimpannya ke struktur data dictionary
# ================================

data_dict = {}
with open('data_mahasiswa.txt', 'r', encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_dict[nim] = {'nama': nama, 'nilai': int(nilai)}

print("====Menampilkan List of Dictionary====")
# print(data_dict)
print("Contoh Record ke 1", data_dict['J0403251138'])
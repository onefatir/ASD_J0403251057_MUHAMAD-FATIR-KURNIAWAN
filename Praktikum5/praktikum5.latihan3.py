#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ==========================================================

# Fungsi cari_maks(data, index) adalah fungsi rekursif yang mencari nilai maksimum dalam sebuah list data.
# Alur programnya adalah sebagai berikut:
# 1. Fungsi menerima dua parameter: data (list yang berisi angka) dan index (indeks saat ini, default 0).
# 2. Base case: Jika index sama dengan panjang data dikurangi 1, fungsi mengembalikan elemen pada indeks tersebut, karena itu adalah elemen terakhir dalam list.
# 3. Recursive case: Fungsi memanggil dirinya sendiri dengan index yang ditingkatkan 1 untuk mencari nilai maksimum dari sisa list.
# 4. Setelah mendapatkan nilai maksimum dari sisa list, fungsi membandingkannya dengan elemen pada indeks saat ini. Jika elemen
#    pada indeks saat ini lebih besar, fungsi mengembalikan elemen tersebut; jika tidak, fungsi mengembalikan nilai maksimum yang ditemukan dari sisa list.
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

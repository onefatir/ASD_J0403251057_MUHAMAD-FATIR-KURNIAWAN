#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ==========================================================

# Fungsi pangkat(a, n) adalah fungsi rekursif yang menghitung a pangkat n.
# Alur programnya adalah sebagai berikut:
# 1. Fungsi menerima dua parameter: a (basis) dan n (eksponen).
# 2. Base case: Jika n sama dengan 0, fungsi mengembalikan 1, karena setiap bilangan pangkat 0 adalah 1.
# 3. Recursive case: Jika n lebih besar dari 0, fungsi mengalikan a dengan hasil pangkat(a, n - 1), yang berarti fungsi memanggil dirinya sendiri dengan n yang dikurangi 1.
# 4. Proses ini terus berlanjut hingga mencapai base case, dimana n menjadi 0, dan kemudian hasilnya akan dikembalikan secara berurutan hingga
#    mencapai pangkat(a, n) yang awal.
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16
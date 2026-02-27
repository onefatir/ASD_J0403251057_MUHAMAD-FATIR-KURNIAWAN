#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# ==========================================================

# Fungsi countdown(n) adalah fungsi rekursif yang mencetak angka dari n hingga 0, dan kemudian mencetak "Selesai". Alur programnya adalah sebagai berikut:
# 1. Fungsi menerima satu parameter: n (angka awal).
# 2. Base case: Jika n sama dengan 0, fungsi mencetak "Selesai" dan mengembalikan None, yang menandakan bahwa fungsi telah selesai.
# 3. Recursive case: Jika n lebih besar dari 0, fungsi mencetak "Masuk:" diikuti dengan nilai n, kemudian memanggil dirinya sendiri dengan n yang dikurangi 1.
# 4. Setelah pemanggilan rekursif selesai (ketika n mencapai 0), fungsi akan kembali ke setiap level sebelumnya dan mencetak "Keluar:" diikuti dengan nilai n yang sesuai dengan level tersebut.
# 5. Karena pemanggilan rekursif terjadi sebelum mencetak "Keluar:", maka output "Keluar" muncul dalam urutan terbalik, dimulai dari nilai n yang paling kecil (0) hingga nilai n yang paling besar (3).
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

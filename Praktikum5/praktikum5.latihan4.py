#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
# ==========================================================

# Fungsi kombinasi(n, hasil) adalah fungsi rekursif yang menghasilkan semua kombinasi dari huruf 'A' dan 'B' dengan panjang n.
# Alur programnya adalah sebagai berikut:
# 1. Fungsi menerima dua parameter: n (panjang kombinasi yang diinginkan) dan hasil (string yang menyimpan kombinasi saat ini, default "").
# 2. Base case: Jika panjang hasil sama dengan n, fungsi mencetak hasil dan mengembalikan None, yang menandakan bahwa kombinasi saat ini telah selesai.
# 3. Recursive case: Fungsi memanggil dirinya sendiri dua kali, pertama dengan menambahkan 'A' ke hasil, dan kedua dengan menambahkan 'B' ke hasil. Ini berarti fungsi akan menjelajahi
#    semua kemungkinan kombinasi dengan menambahkan 'A' atau 'B' pada setiap langkah hingga mencapai panjang n.
# 4. Jumlah kombinasi yang dihasilkan adalah 2^n, karena setiap posisi dalam kombinasi dapat diisi dengan dua pilihan (A atau B). Jadi, untuk n=
#    2, akan ada 2^2 = 4 kombinasi: "AA", "AB", "BA", dan "BB".
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)
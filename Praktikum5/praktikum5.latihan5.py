#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

# ==========================================================
# Studi Kasus: Generator PIN
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# ==========================================================

# Fungsi buat_pin(panjang, hasil) adalah fungsi rekursif yang menghasilkan semua kombinasi PIN dengan panjang tertentu menggunakan angka 0, 1, dan 2.
# Alur programnya adalah sebagai berikut:
# 1. Fungsi menerima dua parameter: panjang (panjang PIN yang diinginkan) dan hasil (string yang menyimpan kombinasi saat ini, default "").
# 2. Base case: Jika panjang hasil sama dengan panjang yang diinginkan, fungsi mencetak PIN yang telah terbentuk dan mengembalikan None, yang menandakan bahwa kombinasi saat ini telah selesai.
# 3. Recursive case: Fungsi menggunakan loop untuk iterasi melalui angka "0", "1", dan "2". Pada setiap iterasi, fungsi memanggil dirinya sendiri dengan menambahkan angka yang sedang diproses ke hasil. Ini berarti fungsi akan menjelajahi semua kemungkinan kombinasi dengan menambahkan "0", "1", atau "2" pada setiap langkah hingga mencapai panjang yang diinginkan.
# 4. Untuk mencegah angka yang sama muncul berulang, kita bisa menambahkan kondisi untuk memeriksa apakah angka yang sedang diproses sama dengan angka terakhir yang ditambahkan ke hasil. Jika sama, kita bisa melewati iterasi tersebut dan tidak memanggil fungsi rekursif dengan angka yang sama. Namun, dalam contoh ini, kita tidak menambahkan kondisi tersebut, sehingga
#    semua kombinasi yang mungkin akan dihasilkan, termasuk yang memiliki angka yang sama berulang.
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
 
    if len(hasil) > 0:
        last_digit = hasil[-1]
    else:
        last_digit = None

    # Jika last_digit tidak None, kita hanya akan menambahkan angka yang berbeda 
    # dari last_digit untuk mencegah angka yang sama muncul berulang.
    if last_digit is not None:
        for angka in ["0", "1", "2"]:
            if angka != last_digit:
                buat_pin(panjang, hasil + angka)
    else:
        for angka in ["0", "1", "2"]:
            buat_pin(panjang, hasil + angka)
        
buat_pin(3)
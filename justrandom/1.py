# Fungsi untuk membuat Judul dan Teks ditengah
def center_text(text, width=40):
    return f"{text:^{width}}"

print('-'*40)
print(center_text("PROGRAM CEK BILANGAN GANJIL GENAP"))
print(center_text("BY:GodFather"))
print('-'*40)


# Fungsi untuk mengecek apakah suatu bilangan ganjil atau genap
# Parameter: angka (int)
# Return: string (hasil pengecekan)     # (===  Tempat Untuk Memproses    ===)
def cek_ganjil_genap(angka):            # (Fungsi untuk mengecek bilangan angka ganjil dan genap)
    if angka % 2 == 0:                  # (jika angka yang telah dibagi 2 tersisa 0 atau habis,maka:)
        return "Genap"                  # (memiliki/masukan nilai genap)
    else:                               # (jika tidak,maka:)
        return "Ganjil"                 # (masukan nilai ganjil)

# Program utama

while True:                                                     # (ketika program benar/berjalan)
    try:                                                        # (lakukan/coba: )
        # Input bilangan dari user
        bilangan = int(input("\nMasukkan bilangan bulat: "))    # (masukan nilai bilangan bulat(integer)ysng ingin diproses/diperiksa)
        
        # Cek dan tampilkan hasil
        hasil = cek_ganjil_genap(bilangan)                      # (cara untuk mengecek hasil adalah memasukan nilai bilangan ke proses pada baris ke 14 yang akan diubah 
        print(f"Bilangan {bilangan} adalah bilangan {hasil}")   #  menjadi angka dan dikeluarkan kembali nilainya untuk diketahui)
         # ---> format : bilangan (nilai yang dimasukan pengguna) adalah bilangan (hasil proses)
        
        # Tanya user apakah ingin mengecek lagi
        lanjut = input("\nIngin mengecek bilangan lain? (y/n): ")   # (masukan huruf y atau n untuk menentukan ingin melanjutkan / tidak)
        if lanjut.lower() != 'y':                                   # (jika variabel lanjut diubah huruf kecil semua dan bukan y,maka:)
            break                                                   # (berhenti)            
            
    except ValueError:                                              # (kecuali nilai bilangan yang dimasukkan bukan bil.bulat,maka:)
        print("Error: Masukkan bilangan bulat yang valid!")         # (keluarkan kata-kata ...... bulat yang valid)
                                                                                

print("\nProgram selesai. Terima kasih!")                           # (kata kata akhir program)           


# Notes : 
# try artinya mencoba menjalankan kode.

# except artinya kalau ada kesalahan, tidak error berantakan, tapi akan menampilkan pesan tertentu.

# input() → hasilnya selalu string → harus diubah jadi int() kalau mau dipakai operasi angka.

# format: {variabel} → disebut f-string (formatted string literals) → mulai dipakai sejak Python 3.6 → lebih mudah dibanding .format() lama.











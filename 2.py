def center_text(text, width=50):
    """Fungsi untuk membuat teks di tengah"""
    return f"{text:^{width}}"

# Program utama
print("="*50)
print(center_text("PROGRAM CEK ANGKA TERBESAR"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Input 3 angka dari user                             
        print("\nMasukkan 3 angka yang akan dibandingkan:")  # mengeluarkan teks dibawah === sebagai petunjuk
        angka1 = float(input("Angka pertama : "))  # meminta pengguna untuk memasukkan variable pertama
        angka2 = float(input("Angka kedua  : "))  #  meminta pengguna untuk memasukkan variable kedua
        angka3 = float(input("Angka ketiga : "))  # meminta pengguna untuk memasukkan variable ketiga 
        
        # Cari angka terbesar # 
        terbesar = max(angka1, angka2, angka3)
        # ---> memasukan nilai terbesar kedalam variable "terbesar"
        # ---> membuat list nilai max yang berisikan angka1,angka2,angka3
        
        # Tampilkan hasil
        print("\nHasil Perbandingan:")
        print(f"Angka terbesar dari {angka1}, {angka2}, dan {angka3} adalah {terbesar}")
        # ---> menulis "hasil perbandingan"
        # ---> menulis format string agar lebih jelas terbaca

        # Tanya user apakah ingin mengecek lagi
        lanjut = input("\nIngin membandingkan angka lain? (y/n): ") #  (masukan huruf y atau n untuk menentukan ingin melanjutkan / tidak)
        if lanjut.lower() != 'y':   # (jika variabel lanjut diubah huruf kecil semua dan bukan y,maka:)
            break    # (berhenti)            
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

print("\nProgram selesai. Terima kasih!")
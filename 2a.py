def center_text(text, width=50):
    """Fungsi untuk membuat teks di tengah"""
    return f"{text:^{width}}"

# Program utama
print("="*50)
print(center_text("PROGRAM VARIASI CEK ANGKA TERBESAR"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        print("\nMasukan 3 angka Yang ingin Diperiksa")
        angka1 = int(input("Masukan Angka Pertama = "))
        angka2 = int(input("Masukan Angka Kedua = "))
        angka3 = int(input("Masukan Angka Ketiga = "))

        Terbesar = max(angka1,angka2,angka3)
        print("Hasil Perhitungan : ")
        print(f"angka terbesar adalah {Terbesar}")

        mau_lanjut = input("\napakah ada angka lain yang ingin diperiksa?(y/n) : ")
        if mau_lanjut.lower() == "n" :
            break

    except ValueError:
        print("\nMasukan Angka Yang Valid ")


print("Thank You Sir ")

# Notes:
# jika try-except ValueError diletakan setelah menampilan hasil / sebelum pertanyaan lanjut nantinya program
# akan berulang terus tanpa ada opsi keluar dari perulangan 
# ada opsi 2 menggunakan logika if,elif,else seperti ini :

# ============= OPSI 2 ============
# while True:
#     try:
#         print("\nPROGRAM MENCARI ANGKA TERBESAR")
#         print("="*35)

#         # Input 3 angka
#         angka1 = float(input("Masukkan angka pertama: "))
#         angka2 = float(input("Masukkan angka kedua: "))
#         angka3 = float(input("Masukkan angka ketiga: "))

#         # Logika if-else untuk menentukan angka terbesar
#         if angka1 >= angka2 and angka1 >= angka3:
#             terbesar = angka1
#         elif angka2 >= angka1 and angka2 >= angka3:
#             terbesar = angka2
#         else:
#             terbesar = angka3

#         print(f"\nAngka terbesar adalah: {terbesar}")

#         # Tanya apakah ingin mengulang
#         lanjut = input("\nIngin mencoba lagi? (y/n): ")
#         if lanjut.lower() != 'y':
#             break

#     except ValueError:
#         print("Error: Masukkan angka yang valid!")

# print("\nProgram selesai. Terima kasih!")


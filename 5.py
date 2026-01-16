def center_text(text, width=50):
    return f"{text:^{width}}"

def hitung_faktorial(n):
    # Mendefinisikan fungsi dengan nama "hitung_faktorial" yang menerima parameter n
    # Docstring menjelaskan tujuan dan parameter fungsi
    if n < 0:
       raise ValueError("Faktorial tidak dapat dihitung untuk angka negatif!")
# Mengecek jika n negatif, raise error karena faktorial hanya untuk non-negatif
    if n == 0 or n == 1:
        return 1
    # Base case untuk rekursi:
    # - Faktorial 0 adalah 1
    # - Faktorial 1 adalah 1
    else:
        return n * hitung_faktorial(n - 1) # ----------> hitung_faktorial(5)
    # bilangan yang diatas akan return hingga base-case--># ↳ return 5 * hitung_faktorial(4)
    # setelah itu angka diatas akan mengalikan dengan       # ↳ return 4 * hitung_faktorial(3)
                                                            #     ↳ return 3 * hitung_faktorial(2)
                                                            #     ↳ return 2 * hitung_faktorial(1)
                                                            #         ↳ return 1    # Base case tercapai
                                                            #     ↳ return 2 * 1 = 2
                                                            #     ↳ return 3 * 2 = 6
                                                            # ↳ return 4 * 6 = 24
                                                            # ↳ return 5 * 24 = 120
    # hasil dari angka dibawahnya
    # kira seperti itu,lihat disamping--------->>>>>>>  
                                                    
    # Rekursi:
    # - Mengalikan n dengan faktorial dari (n-1)
    # - Proses berulang sampai mencapai base case
# Main program
print("="*50)
print(center_text("PROGRAM HITUNG FAKTORIAL"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get number from user
        angka = int(input("\nMasukkan angka untuk dihitung faktorialnya: "))
        
        # Calculate and display result
        hasil = hitung_faktorial(angka)
        print(f"\nHasil Perhitungan:")
        print(f"{angka}! = {hasil:,}")  # Using thousandths separator
        # :, supaya ketika hasil ribuan akan seperti ini 5! = 2,000,000


        # Ask to continue
        lanjut = input("\nIngin menghitung faktorial lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError as e:
        if str(e).startswith("Faktorial"):
            print(f"Error: {e}")
        else:
            print("Error: Masukkan bilangan bulat non-negatif!")

    except ValueError as e:

# Menangkap exception tipe ValueError
# Menyimpan error message ke variabel e
# if str(e).startswith("Faktorial"):

# Mengecek apakah pesan error dimulai dengan kata "Faktorial"
# str(e) mengkonversi error message ke string
# .startswith() mengecek awalan string
# Error handling:

# Jika pesan dimulai "Faktorial": menampilkan pesan error custom
# Jika tidak: menampilkan pesan "Masukkan bilangan bulat non-negatif!"

        print("\nProgram selesai. Terima kasih!")

# Membuat list kosong untuk menyimpan faktor-faktor yang ditemukan
# Membuat list kosong untuk menyimpan faktor-faktor yang ditemukan
# Melakukan perulangan dari 1 sampai n
    # n + 1 karena range akan berhenti sebelum nilai akhir
    # Mengecek apakah n habis dibagi i (sisa bagi = 0)
        # Jika ya, maka i adalah faktor dari n
        # Menambahkan i ke dalam list faktor
        # Mengembalikan list yang berisi semua faktor


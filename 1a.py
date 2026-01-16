# ⚡ Latihan Variasi dari Program Nomor 1
# Nah, sekarang untuk variasi soal nomor 1:

# 🔔 Variasi Soal 1:
# Buat program untuk memeriksa apakah banyak angka (lebih dari satu) ganjil atau genap.
# Contoh input: 2 5 7 8 9
# Output:

# Bilangan 2 adalah GENAP
# Bilangan 5 adalah GANJIL
# Bilangan 7 adalah GANJIL
# Bilangan 8 adalah GENAP
# Bilangan 9 adalah GANJIL
# ➡️ Gunakan split() dan loop.

# Kalau mau aku buatin kerangka/struktur kodenya dulu → katakan ya. Tapi coba dulu sendiri → kirimkan hasilnya → aku bantu review lagi seperti sebelumnya.

# Mau lanjut coba kerjakan dulu atau mau aku bantu bikin contoh awalnya?                                 

def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

def cek_ganjil_genap(angka):
    """Check if number is odd or even"""
    return "GENAP" if angka % 2 == 0 else "GANJIL"

# Main program
print("="*50)
print(center_text("PROGRAM VARIASI CEK BILANGAN GANJIL GENAP"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True: # (Loop yang akan berjalan terus menerus (infinite loop),Hanya akan berhenti jika ada break statement)
    try: # (Awal dari blok try-except untuk menangani error,Code di dalam blok try akan dimonitor untuk error yang mungkin terjadi)
        
        # Get input numbers from user
        print("\nMasukkan beberapa angka dipisahkan spasi") 
        print("Contoh: 2 5 7 8 9")
        numbers = input("\nMasukkan angka-angka: ").strip() # (input(): Menerima input angka yang dipisah spasi, .strip(): Menghapus spasi di awal/akhir) 
        
        if not numbers: # jika input kosong (string kosong), tampilkan error dan kembali ke awal loop
            print("Error: Input tidak boleh kosong!")
            continue    # lanjut ke iterasi berikutnya, tidak memproses kode di bawah if ini
            
        # Convert string to list of integers    
        number_list = [int(x) for x in numbers.split()] 
        # ---> numbers.split() - memecah string input menjadi list berdasarkan spasi)
        # ---> numbers.split(): Memisah string menjadi list → ["2", "5", "7"]
        # ---> [int(x) for x in ...]: Mengubah setiap string jadi integer → [2, 5, 7]
        # ---> Ini disebut "list comprehension"

        # Check and display result for each number
        print("\nHasil Pengecekan:")
        print("-"*30)
        for num in number_list:
            hasil = cek_ganjil_genap(num)
            print(f"Bilangan {num} adalah {hasil}")
        print("-"*30)
        # ---> Cetak header untuk hasil                     Input: "2 5 7"
        # ---> Buat garis pemisah dengan 30 tanda minus     Setelah split(): ["2", "5", "7"]
        # ---> Mulai loop untuk memproses setiap angka      Setelah list comprehension: [2, 5, 7]
        
                                                                
        
        # Ask to continue                                        # PROGRAM SEDERHANA UNTUK MELANJUTKAN ATAU TIDAK 
        lanjut = input("\nIngin mengecek angka lain? (y/n): ")             
        if lanjut.lower() != 'y':                                          
            break     # break digunakan untuk keluar dari infinite loop ketika user tidak ingin lanjut                                                            
            
    except ValueError: # untuk menangkap jika terjadi error akan keluar:...
        print("Error: Masukkan angka yang valid!")

print("\nProgram selesai. Terima kasih!")

# Notes :
# Kenapa pakai try-except ValueError?
# → Karena fungsi int() akan menimbulkan ValueError jika input tidak bisa dikonversi ke integer (misal huruf/karakter selain angka).

# Kenapa pakai lower()?
# → Untuk menyamakan input huruf besar/kecil agar bisa dibandingkan konsisten (misal: 'Y', 'y', 'Y ' semua dianggap 'y'
# palindrom adalah kata,frasa,angka,atau urutan karakter yang jika dibaca dari 
# depan maupun belakang tetap sama cth: katak,kasur ini rusak,malam,dll 

def center_text(text, width=50):
    return f"{text:^{width}}"

def cek_palindrom(kalimat):
    cleaned = ''.join(kalimat.lower().split())
    # ---> Mengubah semua huruf pada kalimat menjadi huruf kecil (lowercase)
    # ---> Menghapus semua spasi dengan split() lalu join()
    # ---> Hasilnya adalah string tanpa spasi dan semua huruf kecil
    return cleaned == cleaned[::-1]
    

# Main program
print("="*50)
print(center_text("PROGRAM CEK PALINDROM"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        kalimat = input("\nMasukkan kalimat: ").strip()
        if not kalimat:
            print("Error: Kalimat tidak boleh kosong!")
            continue
            
        if cek_palindrom(kalimat):
            print(f"\n'{kalimat}' adalah palindrom!")
        else:
            print(f"\n'{kalimat}' bukan palindrom!")
        
        # Tampilkan proses pengecekan
        print("\nProses pengecekan:")
        print(f"1. Hapus spasi & lowercase : {''.join(kalimat.lower().split())}")
        print(f"2. Hasil dibalik          : {''.join(kalimat.lower().split())[::-1]}")
        
        lanjut = input("\nIngin mengecek kalimat lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except Exception as e:
        print(f"Error: {str(e)}")

print("\nProgram selesai. Terima kasih!")

# Notes : 
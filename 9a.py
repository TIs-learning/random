def center_text(text, width=50):
    return f"{text:^{width}}"

def balik_kalimat(kalimat):
    """
    Membalik urutan kata dalam kalimat
    Example: "saya suka programming" -> "programming suka saya"
    """
    # Split kalimat menjadi list kata dan balik urutannya
    kata_list = kalimat.split()
    kata_list.reverse()
    # Gabung kembali menjadi kalimat
    return " ".join(kata_list)

# Main program
print("="*50)
print(center_text("PROGRAM PEMBALIK KALIMAT"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        kalimat = input("\nMasukkan kalimat: ").strip()
        if not kalimat:
            print("Error: Kalimat tidak boleh kosong!")
            continue
            
        hasil = balik_kalimat(kalimat)
        print("\nHasil pembalikan:")
        print(f"Kalimat asli  : {kalimat}")
        print(f"Hasil dibalik : {hasil}")
        
        lanjut = input("\nIngin membalik kalimat lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except Exception as e:
        print(f"Error: {str(e)}")

print("\nProgram selesai. Terima kasih!")
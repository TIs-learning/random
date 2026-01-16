def center_text(text, width=50):
    return f"{text:^{width}}"

def hitung_vokal(kalimat):
    vokal = {'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0}
    
    for huruf in kalimat.lower():
        if huruf in vokal:
            vokal[huruf] += 1
    
    return vokal

# Main program
print("="*50)
print(center_text("PROGRAM HITUNG HURUF VOKAL"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        kalimat = input("\nMasukkan kalimat: ")
        if not kalimat.strip():
            print("Error: Kalimat tidak boleh kosong!")
            continue
            
        hasil = hitung_vokal(kalimat)
        
        print("\nHasil analisis vokal:")
        print("-"*20)
        for huruf, jumlah in hasil.items():
            print(f"Huruf '{huruf}' = {jumlah}")
        print(f"Total vokal = {sum(hasil.values())}")
        
        lanjut = input("\nIngin menganalisis kalimat lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except Exception as e:
        print(f"Error: {str(e)}")

print("\nProgram selesai. Terima kasih!")
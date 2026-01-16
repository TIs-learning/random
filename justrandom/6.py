def center_text(text, width=50):
    return f"{text:^{width}}"

def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main program
print("="*50)
print(center_text("PROGRAM CEK BILANGAN PRIMA"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get number from user
        angka = int(input("\nMasukkan bilangan bulat positif: "))
        
        # Check if prime and display result
        if angka < 0:
            print("Error: Masukkan bilangan bulat positif!")
        else:
            hasil = "ADALAH" if is_prima(angka) else "BUKAN"
            print(f"\nHasil Pengecekan:")
            print(f"Bilangan {angka} {hasil} bilangan prima")
        
        # Ask to continue
        lanjut = input("\nIngin mengecek bilangan lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError:
        print("Error: Masukkan bilangan bulat yang valid!")

print("\nProgram selesai. Terima kasih!")

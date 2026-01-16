import math

def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

def hitung_luas_lingkaran(radius):
    """
    Function to calculate circle area
    Parameter: radius (float)
    Return: area (float)
    """
    return math.pi * radius ** 2

# Main program
print("="*50)
print(center_text("PROGRAM HITUNG LUAS LINGKARAN"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get radius from user
        radius = float(input("\nMasukkan jari-jari lingkaran (cm): "))
        
        # Calculate and display result
        luas = hitung_luas_lingkaran(radius)
        print(f"\nHasil Perhitungan:")
        print(f"Jari-jari lingkaran = {radius} cm")
        print(f"Luas lingkaran      = {luas:.2f} cm²")
        
        # Ask to continue
        lanjut = input("\nIngin menghitung luas lingkaran lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

print("\nProgram selesai. Terima kasih!")

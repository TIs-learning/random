def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# Main program
print("="*50)
print(center_text("PROGRAM KONVERSI SUHU"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get temperature input
        celcius = float(input("\nMasukkan suhu dalam Celcius: "))
        
        # Convert and display result
        fahrenheit = celcius_ke_fahrenheit(celcius)
        print(f"\nHasil Konversi:")
        print(f"{celcius}°C = {fahrenheit:.1f}°F")
        
        # Ask to continue
        lanjut = input("\nIngin mengkonversi suhu lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

print("\nProgram selesai. Terima kasih!")

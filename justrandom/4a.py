# Buatlah program konversi suhu lengkap yang dapat:

# Mengkonversi suhu dari Celcius ke:
# Fahrenheit
# Reamur
# Kelvin

# Program menampilkan menu pilihan konversi kepada user.
# User dapat memilih mau konversi ke satuan mana.
# Setelah konversi, program bertanya apakah user ingin melanjutkan atau keluar.

def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

# Main program
print("="*50)
print(center_text("PROGRAM KONVERSI SUHU"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        celcius = float(input("Masukan nilai celcius : "))
        print("1. Fahrenheit")
        print("2. Reamur")
        print("3. Kelvin\n")
        pilihan = int(input("masukan pilihan (1/2/3) : ")) 
        if pilihan == 1:
            hasil = (celcius * 9/5) + 32
            print(f"setelah {celcius} derajat celcius di konversi fahrenheit adalah {hasil} derajat fahrenheit")
        elif pilihan == 2:
            hasil = (celcius * 4/5)
            print(f"setelah {celcius} derajat celcius di konversi reamur menjadi {hasil} derajat reamur")
        elif pilihan == 3:
            celcius + 273.15
            print(f"setlah {celcius} derajat celcius di konversi kelvin menjadi {hasil} derajat kelvin")
        else:
            print("Masukin pilihan yang bener")
            
        lanjut = input("mau diulang lagi?(y/n) : ")
        if lanjut.lower() == "n":
            break

    except ValueError:
        print("masukn nilai yang valid")

print("Thank You Sir.......")

# Notes :
# kalau make logika pilihan dengan if elif else dalam integer ga usah pake "..." , 
# "..." dipakai kalo dia mendeteksi pilihan string


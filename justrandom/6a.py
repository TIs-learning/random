# 📌 Deskripsi Soal:
# Buatlah program Python untuk menampilkan semua bilangan prima dalam rentang tertentu.
# Program meminta 2 input angka → sebagai batas awal dan batas akhir.
# Program akan mencetak semua bilangan prima yang berada di antara batas tersebut.
# Setelah selesai, program bertanya apakah user ingin mencoba lagi.

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
        angka_awal = int(input("\nMasukkan bilangan bulat awal positif: "))
        angka_akhir = int(input("\nMasukan angka bulat akhir positif: "))
        print(f"angka prima dari {angka_awal} sampai {angka_akhir}")
        for i in range(angka_awal, angka_akhir + 1):
            if is_prima(i):
                print(i, end=' ')
        print("\nUdah yappingnya....")
        # Ask to continue
        lanjut = input("\nIngin mengecek bilangan lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
    except ValueError:
        print("Error: Masukkan bilangan bulat yang valid!")
print("\nProgram selesai. Terima kasih!")

# Buatlah program Python untuk menghitung faktorial dari beberapa angka sekaligus.
# User memasukkan 2 angka → sebagai batas awal dan batas akhir.
# Program akan menghitung faktorial untuk semua angka dalam range tersebut.
# Setelah selesai, tanyakan apakah user ingin mencoba lagi.



def center_text(text, width=50):
    return f"{text:^{width}}"
def hitung_faktorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak dapat dihitung untuk angka negatif!")
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n-1)

# Header program
print("="*50)
print(center_text("PROGRAM HITUNG FAKTORIAL VARIASI"))
print(center_text("BY GOD FATHER"))
print("="*50)



while True:
    try:
        awal = int(input("masukkan angka awal : "))
        akhir = int(input("masukan angka akhir : "))
        print(f"faktorial dari {awal} sampai {akhir} faktorial")
        for i in range(awal, akhir + 1):
            hasil = hitung_faktorial(i)
            print(f"{i}! = {hasil:,}")
        else:
            print("\n udah ya....")
    except ValueError as e:
        if str(e).startswith("Faktorial"):
            print(f"\nError: {e}")
        else:
            print("\nError: Masukkan bilangan bulat positif!")
    
    lanjut = input("\nIngin menghitung lagi? (y/n): ")
    if lanjut.lower() == "n":
        print("\nTerima kasih telah menggunakan program ini!")
        break
        




# (Redundant except block removed)

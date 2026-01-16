# Buat program Python untuk menampilkan deret Fibonacci hingga mencapai/mendekati angka batas maksimal tertentu, bukan berdasarkan jumlah suku.
# Program meminta 1 input berupa angka batas maksimal.
# Program mencetak deret Fibonacci mulai dari 0 hingga bilangan Fibonacci terbesar yang masih lebih kecil atau sama dengan batas tersebut.
# Setelah selesai → program tanya apakah ingin mengulang.

def center_text(text, width=50):
    return f"{text:^{width}}" # <--- Program fungsi judul

def generate_fibonacci(start, end): # Mendefinisikan fungsi dengan dua parameter: start (batas bawah), end (batas atas)
    fib = [0, 1] # Membuat list awal berisi dua bilangan Fibonacci pertama: 0 dan 1
    while fib[-1] <= end: # Melakukan perulangan selama elemen terakhir pada list fib (fib[-1]) kurang dari atau sama dengan end
        fib.append(fib[-1] + fib[-2])    # Menambahkan ke list fib hasil penjumlahan dua elemen terakhir (bilangan Fibonacci berikutnya)
    
    # Filter angka dalam range yang diminta
    result = [x for x in fib if start <= x <= end]
    # Membuat list baru bernama result
    # Mengambil setiap elemen x dari list fib
    # Hanya memasukkan x ke result jika nilainya berada di antara start dan end (inklusif)
    return result
    # Mengembalikan list result sebagai output fungsi
    
# Main program
print("="*50)
print(center_text("PROGRAM DERET FIBONACCI"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get range from user
        start = int(input("\nMasukkan batas bawah: "))
        end = int(input("Masukkan batas atas: "))
        
        if start < 0 or end < 0:
            print("Error: Masukkan bilangan positif!")
            continue
        if start > end:
            print("Error: Batas bawah harus lebih kecil dari batas atas!")
            continue
            
        # Generate and display sequence
        hasil = generate_fibonacci(start, end)
        print(f"\nDeret Fibonacci dari {start} sampai {end}:")
        for i, num in enumerate(hasil, 1):
            print(f"F({i}) = {num:,}")
        
        # Ask to continue
        lanjut = input("\nIngin mencoba range lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError:
        print("Error: Masukkan bilangan bulat yang valid!")

print("\nProgram selesai. Terima kasih!")
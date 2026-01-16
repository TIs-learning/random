def center_text(text, width=50):
    return f"{text:^{width}}"

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Main program
print("="*50)
print(center_text("PROGRAM DERET FIBONACCI"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get number of terms from user
        n = int(input("\nMasukkan jumlah bilangan Fibonacci yang diinginkan: "))
        
        if n < 0:
            print("Error: Masukkan bilangan positif!")
            continue
            
        # Generate and display sequence
        hasil = generate_fibonacci(n)
        print(f"\nDeret Fibonacci {n} bilangan pertama:")
        for i, num in enumerate(hasil, 1):
            print(f"F({i}) = {num:,}")
        
        # Ask to continue
        lanjut = input("\nIngin mencetak deret lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except ValueError:
        print("Error: Masukkan bilangan bulat yang valid!")

print("\nProgram selesai. Terima kasih!")

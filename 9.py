def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

def balik_kata(text):
    """
    Function to reverse words
    Parameter: text (str) - input text
    Return: str - reversed text
    """
    # Reverse whole text then reverse each word
    words = text.split()
    reversed_text = ' '.join(word[::-1] for word in words)
    return reversed_text

# Main program
print("="*50)
print(center_text("PROGRAM PEMBALIK KATA"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get input from user
        text = input("\nMasukkan teks: ").strip()
        
        if not text:
            print("Error: Teks tidak boleh kosong!")
            continue
            
        # Reverse and display result
        hasil = balik_kata(text)
        print("\nHasil Pembalikan:")
        print(f"Teks asli  : {text}")
        print(f"Teks balik : {hasil}")
        
        # Ask to continue
        lanjut = input("\nIngin membalik teks lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except Exception as e:
        print(f"Error: {str(e)}")

print("\nProgram selesai. Terima kasih!")
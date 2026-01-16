def center_text(text, width=50):
    """Function to center align text"""
    return f"{text:^{width}}"

def is_palindrom(text):
    """
    Function to check if text is palindrome
    Parameter: text (str) - input text
    Return: bool - True if palindrome, False if not
    """
    # Remove spaces and convert to lowercase
    text = ''.join(text.lower().split())
    return text == text[::-1]

# Main program
print("="*50)
print(center_text("PROGRAM CEK PALINDROM"))
print(center_text("BY GOD FATHER"))
print("="*50)

while True:
    try:
        # Get input from user
        text = input("\nMasukkan kata/kalimat: ").strip()
        
        if not text:
            print("Error: Input tidak boleh kosong!")
            continue
            
        # Check and display result
        if is_palindrom(text):
            print(f"\n'{text}' adalah palindrom")
            print(f"Jika dibalik tetap: '{text}'")
        else:
            reversed_text = text[::-1]
            print(f"\n'{text}' bukan palindrom")
            print(f"Jika dibalik menjadi: '{reversed_text}'")
        
        # Ask to continue
        lanjut = input("\nIngin mengecek kata lain? (y/n): ")
        if lanjut.lower() != 'y':
            break
            
    except Exception as e:
        print(f"Error: {str(e)}")

print("\nProgram selesai. Terima kasih!")
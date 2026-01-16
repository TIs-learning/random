# Fungsi untuk membuat Judul dan Teks ditengah
def center_text(text, width=40):
    return f"{text:^{width}}"

print('-'*40)
print(center_text("PROGRAM CEK TAHUN KABISAT"))
print(center_text("BY:GodFather"))
print('-'*40)

while True:
    try:
        Tahun = (int(input("Sebutkan Tahun Yang ingin Diketahui : ")))
        if Tahun % 4 == 0 and Tahun % 100 != 0:
            print(f"\nHasilnya adalah '{Tahun}' merupakan tahun kabisat")
        elif Tahun % 100 == 0 and Tahun % 400 == 0:
            print(f"\nHasilnya adalah '{Tahun}' merupakan tahun kabisat")
        else:
            print(f"\nHasilnya adalah '{Tahun}' bukan merupakan tahun kabisat")

        lanjut = input("Apakah ada tahun yang ingin diketahui lagi?(y/n) : ")
        if lanjut.lower != 'y':
            break
        
    except ValueError:
        print("\nMasukan tahun yang valid")

print("Thank You sir....")

# Notes:
# bagaimana mengetahui tahun itu kabisat?jika tahun itu habis dibagi 4 dan tidak habis dibagikan 100 atau bisa
# jika tahun itu habis dibagikan 100 dan habis dibagikan dengan 400
# rumus itu ditulis dari baris ke 12 - 18
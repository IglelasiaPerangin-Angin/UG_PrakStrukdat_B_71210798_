def calculate():
    kata = True
    while kata:
        iUser = input("Masukkan Pilihan Anda: ")
        
        if iUser == "1":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 + bilangan2
            print("Hasil nya: %d"%hasil)
        elif iUser == "2":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 - bilangan2
            print("Hasil nya: %d"%hasil)
        elif iUser == "3":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 * bilangan2
            print("Hasil nya: %d"%hasil)
        elif iUser == "4":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 / bilangan2
            print("Hasil nya: %d"%hasil)
        elif iUser == "Q":
            break
        else :
            print("Pilihan yang engkau masukkan tidak ada di menu ya sobat!")
        
print("Calculator Sederhana Python\n")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("Ketik 'Q' jika mau menghentikan calculator")


calculate()
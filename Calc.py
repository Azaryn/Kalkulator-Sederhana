
# Input kalkulator sederhana
def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def kali (x,y):
    return x * y

def bagi (x,y):
    return x / y

def pangkat (x,y):
    return x ** y

def modulo(x,y):
    return x % y

def pembagian_bulat(x,y):
    return x // y

print("""Selamat Datang di kalkulator simple
1. Tambah
2. Kurang
3. Perkalian
4. Pembagian
5. Pangkat/Eksponen
6. Mod
7. Pembagian bilangan bulat
""")

while True:
# Input memilih fungsi operasi
    choice = input("Silahkan pilih(1/2/3/4/5,6,7): ")
    if choice in ('1','2','3','4', '5', '6', '7'):
# tambahkan logika error handling
        try:
# Input angka yang akan dioperasikan
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Itu bukan angka!!")
            continue
# Cetak Hasil
        if choice == '1':
            print(f"{num1} +  {num2} = ", tambah(num1,num2))
        elif choice == '2':
            print(f"{num1} - {num2} = ", kurang(num1,num2))
        elif choice == '3':
            print(f"{num1} * {num2} = ", kali(num1,num2))
        elif choice == '4':
            print(f"{num1} / {num2}", bagi(num1,num2))
        elif choice == '5':
            print(f"{num1}^{num2} = ", pangkat(num1, num2))
        elif choice == '6':
            print(f"{num1} % {num2} = ", modulo(num1, num2))
        elif choice == '7':
            print(f"{num1} // {num2} = ", (num1, num2))
# Pengulangan kalkulator
        perhitungan_selanjutnya = input("Apakah ingin menghitung lagi?(y/n): ")
        if perhitungan_selanjutnya == "y" :
            continue
        else:
            break
    else:
        print("Tidak ada di opsi")

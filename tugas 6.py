print(f"tugas1 : Buat program")
print()

angka = int(input("masukan nilai  :"))

if angka % 2 == 0:
     print("INI ADALAH BILANGAN GENAP")
else:
     print("bukan bilangan genap")

# program penjumlahan waktu

jam1 = int(input("masukan jam:"))
menit1 = int(input("masukan menit:"))
print(f"waktu yang di input = {jam1}:{menit1}")

print("\nmau dijumlah berapa ?\n")

jam2 = int(input("masukan jam:"))
menit2 = int(input("masukan menit:"))
print(f"jumlah waktu yang mau di tambahkan = {jam2}:{menit2}")

hasil_jam = (jam1 + jam2)
hasil_menit = (menit1 + menit2)

if hasil_menit >= 60:
    hasil_jam += 1
    hasil_menit -= 60

print(f"\nhasilnya adalah = {hasil_jam}:{hasil_menit}")
print("="*20)

# program selisih waktu

print(f'2. Program Selisih Waktu')

jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))


jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))

total_jam = (jam1 - jam2)
total_menit = (menit1 - menit2)

if total_menit <= 0:
    total_menit = total_menit % 60
    total_jam = total_jam -1
    
    
print("Jumlah selisih waktu: 0{}:{}".format(total_jam, total_menit))

     


print('latihan-1')
nilai = 70
nilai = float(input('Masukan Nilai= '))
batas_lulus = 65
if nilai > batas_lulus:
 print('Selamat, kamu lulus!')
else:
     print('Maaf, kamu tidak lulus!')

print('latihan-2')
inp = input('Masukan suatu input: ')

if len(inp) != 3:
    print('Panjang string', len(inp),'tidak sama dengan 3')

else:
    print('Panjang input sesuai yang diinginkan')

print()
nilai = int(input('Masukan nilai: '))

if nilai >= 90:
    print('Nilai huruf: A')
elif nilai > 75:
    print('Nilai huruf: B')
elif nilai > 55:
    print('Nilai huruf: C')
else:
    print('Nilai huruf: D')

print('latihan-3')
nama = str(input('masukkan nama karyawan='))
pendapatan = int(input('pendapatan='))

if pendapatan > 1000 :
    print ('status : Berhak')
else :
    print ('status : Tidak Berhak')

print('latihan-4')
# Membaca input pendapatan dari pengguna
pendapatan = int(input("Pendapatan: "))

# Inisialisasi variabel persentase dan bonus
persentase = 0
bonus = 0

# Menentukan persentase bonus berdasarkan pendapatan
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40
else:
    persentase = 50

# Menghitung bonus dan jumlah total
bonus = (pendapatan * persentase) / 100
total = pendapatan + bonus

# Mencetak output
print(f'Pendapatan: {pendapatan}')
print(f'Persentase: {persentase}%')
print(f'Bonus: {bonus}')
print(f'Jumlah Total: {total}')








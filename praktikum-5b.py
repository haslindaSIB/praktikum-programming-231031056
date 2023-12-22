import os
os.system('clear')

nim = [2,3,1,0,3,1,0,5,6]
print(nim)
# a = ' '.join(str(nim))
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6] ',nim[-6])
print('item indeks 5: [-4] ',nim[-4])
print('item indeks -7: [4] ',nim[2])
print('item indeks 2: [-7] ',nim[-7])
# akses indeks batas
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [-4]: {nim[:-5]}')
# pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]]: {nim[1:-1]}')
print(f'item indeks [2:7]]: {nim[2:-2]}')
# nested list
kelas = [('matkul',2),
         ('matkul',3)]
print(kelas)
kelas.append(('matkul',2))
print(kelas)
# tambahkan matkul 4 dan 5 dan sksnya

# mata kuliah 1: matkul1 dengan 2 sks 
# mata kuliah 2: matkul2 dengan 3 sks
# mata kuliah 3: matkul3 dengan 2 sks
# mata kuliah 4: matkul4 dengan .. sks
# mata kuliah 5: matkul5 dengan .. sks

data = [('frankel',2023,'Aktif'),
        (76,98,89,97,99),
        (2,3,2,2,2),
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Frankel
# Inisial frankel: F
# Nim frankel: 231031056
# Program Frankel: S1-Reguler','Sistem Informasi B
# Angkatan Frankel: Ganjil-2023
# Jumlah Nilai Frankel: 5
# Nilai tertinggi Frankel: 99
# Nilai terendah Frankel: 76




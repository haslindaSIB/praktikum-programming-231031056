import os
os.system('clear')

nama ='HASLINDA'
nim  ='231031056'
meet ='praktikum 4'
prodi='Sistem Informasi'
email='haslindaindah283@gmail.com'
tgl  ='11 oktober 2023'
sp = 40
#print(len)(nama)
print('-'*31)
print(nama.center(31))
print(nim.center(31))
print('\n'*2)
print(meet.rjust(31))
print(prodi.rjust(31))
print(email.rjust(31))
print('-'*31)

print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp) + f'\r{tgl}')
print('-'*sp)
# print(prodi.rjusr(sp))
print(email.rjust(sp) + f'\r{tgl}')
print('-'*sp)

paragraf = '''Halo, selamat datang perkenalkan 
nama saya {} dengan NIM {} dari prodi {}.Ini 
adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

print('----------8+++++++++')
x = 9 #input
hasil = x>8
print(x,'hasilnya adalah',hasil)

print('+++++++++++8-----------')
x = 9 #input
hasil = x<8
print(x,'hasilnya adalah',hasil)

print('--------4++++++++8--------')
x = 9
# cek1 = x>4 true
cek1 = x>4
# cek2 = x<8 true
cek2 = x<8
# hasil = cek1 and cek2 -->true
hasil = cek1 and cek2 
# cetak hasil
print(x,'hasilnya adalah',hasil)

print('+++++++++++4----------8+++++++++++')
x = 2
# cek1 = x>4 true
cek1 = x>4
# cek2 = x<8 false
cek2 = x<8
# hasil = cek1 or cek2 -->true
hasil = cek1 or cek2 
# cetak hasil
print(x,'hasilnya adalah',hasil)







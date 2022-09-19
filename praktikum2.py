p = float(input('Masukkan Panjang: '))
l = float(input('Masukkan Lebar: '))
sat = input('Pilih Satuan, Meter/Inci: ')

if sat == 'Meter' or sat == 'meter':
    sat = 'm'
elif sat == 'Inci' or sat == 'inci':
    sat = 'i'
else:
    sat = 'Satuan tidak diketahui.'
    exit()

total = p*l

print(f'Diketahui panjang dari sebuah ruangan adalah {p}{sat} dengan lebar {l}{sat}, sehingga luas dari ruangan tersebut adalah {total}{sat}')
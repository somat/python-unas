'''
Kuis tebak angka.
Pertama, buat angka acak yang nilainya diantara 1 sampai 100.
Kemudian baca angka yang dimasukkan pengguna.
Jika angkanya sesuai dengan angka acak, maka berhenti.

Skrip ini digunakan untuk menjelaskan penulisan kode program Python
yang mencakup:
    1. Sintaks bahasa Python
    2. Penggunaan pustaka standar Python
    3. Variabel
    4. Penggunaan string beberapa baris
    5. Perulangan while
    6. Penanganan kesalahan
    7. Pencabangan if

Ditulis oleh: Akhmat Safrudin <somat@python.or.id>
'''
from random import randint


secrete_number = randint(1,100)
print('''Selamat datang di kuis tebak angka,
Silakan menebak angka antara 1 sampai 100''')

while True:
    try:
        guess = int(input('Masukkan tebakan Anda: '))
    except:
        print('Mohon masukkan angka antara 1 sampai 100.')
        continue

    print('Tebakan anda adalah', guess)

    if guess == secrete_number:
        print('Waaww selamat, anda benar.')
        break

    elif guess < secrete_number:
        print('Angka rahasia lebih dari %s, coba lagi ya.' % guess)

    else:
        print('Angka rahasia kurang dari %s, silakan coba lagi ya.' % guess)

#Assignmenet 1

#nomor 1
'''Buatlah sebuah program yang menerima 3 input dari user: 
Nama(str), umur(int), tinggi(float)
format output: Nama saya [Nama], umur saya [Umur] tahun dan tinggi saya [Tinggi] cm.'''
name = str(input('Masukkan nama: '))
age = int(input('Masukkan usia; '))
height = float(input('Masukkan tinggi badan: '))

print('Nama saya {}'.format(name) + ', umur saya {} tahun'.format(age) + ' dan tinggi saya {} cm'.format(height))

#nomor 2
print('=====================')
''' sebuah program yang dapat menghitung luas lingkaran.
Program meminta input dari user berupa angka sebagai jari-jari lingkaran.'''
phi = 22/7
radius = int(input('Masukkan panjang jari-jari lingkaran: '))
area = phi*(radius**2)

print('Luas lingkaran dengan jari-jari {} cm'.format(radius) + ' adalah {:.2f} cm\u00b2'.format(area))

#nomor 3
print('=====================')
''' sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. 
Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.'''
theory_exam = int(input('Masukkan nilai ujian teori: '))
practical_exam = int(input('Masukkan nilai ujian praktek: '))

if theory_exam >= 70 and practical_exam >= 70:
    print('Selamat Anda Lulus')
elif theory_exam >= 70 and practical_exam < 70:
    print('Anda harus mengulang ujian praktek')
elif theory_exam < 70 and practical_exam >= 70:
    print('Anda harus mengulang ujian teori')
else:
    print('Anda harus mengulang ujian teori dan praktek')
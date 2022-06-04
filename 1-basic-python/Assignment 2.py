#Assignment 2

contact_name =[]
contact_number = []

def display_contact():
        print('Daftar Kontak')
        for i in range(len(contact_name)):
            print('Nama: {}'.format(contact_name[i]))
            print('No. Telpon: {}\n'.format(contact_number[i]))

def add_contact():
    add_name = input('Nama: ')
    add_number = input('No. Telpon: ')

    contact_name.append(add_name)
    contact_number.append(add_number)
    print('Kontak berhasil ditambah\n')   

print("Selamat Datang!\n")
while True:
    print(
        "------Menu------\n"
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
    )

    menu_input= input('Pilih Menu: ')
    print()

    if menu_input == '1':
        display_contact()
           
    elif menu_input == '2':
        add_contact()

    elif menu_input == '3':
        print('Program Selesai, Sampai Jumpa!')
        break

    else:
        print('Menu Tidak Tersedia\n')
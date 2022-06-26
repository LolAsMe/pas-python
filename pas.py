import daftar
import sys
from belanja import Belanja
#PAS

#Menu
#Menu1: menu utama(list barang, inputan rencana belanja, rencana ke file)
#Menu2: input barang baru
#tombal selesai

# daftar.printProduks()

menu = True
menu_options = (
    'Rencana Belanja',
    'Tambah Daftar Barang',
    # 'Edit Daftar Barang',
    'Exit'
)

def print_menu():
    print("\n")
    n=0
    for menu in menu_options:
        n=n+1
        print (n, '--', menu )
        

def option1():
     global menu
     menu = False
     belanja = Belanja()
     while not menu:
         print('Rencana Belanja')
         print(daftar.printProduks(),"\n")
         
         noProduk = input('masukkan nomer produk! \n')
         jumlahProduk = input('masukkan jumlah produk \n')
         produk = daftar.produks[int(noProduk)-1]
         nama = produk['nama']
         harga = produk['harga']
         belanja.addBelanja(nama, harga, jumlahProduk)
         if belanja.total  != 0:
             belanja.showBelanja()
         repeat = input("tambah produk lagi? jika iya ketik iya atau y selain itu dianggap tidak \n")
         if repeat == "y" or repeat=="iya":
             
             menu=False
         else:
            belanja.toFile()
            menu=True
     
         
def option2():
        global menu
        menu = False
        while not menu:
            print("Menu Tambah Daftar Barang \n")
            print(daftar.printProduks(),"\n")
            produkBaru = input("masukkan nama produk baru! \n")
            hargaProduk = input("masukkan harga! \n")
            daftar.tambahProduk(produkBaru, hargaProduk)
            print(daftar.printProduks())
            repeat = input("tambah produk lagi? jika iya ketik iya atau y selain itu dianggap tidak \n")
            if repeat == "y" or repeat=="iya":
                menu=False
            else:
                
                menu=True
        
while(menu):
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    if option == 1:
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        print('Thanks message before exiting')
        sys.exit()
    else:
        print('Invalid option. Please enter a number between 1 and 3.')
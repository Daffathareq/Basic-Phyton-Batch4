

print ("Selamat Datang!")
print ("--- Menu ---")
print ("1. Daftar Kontak")
print("2. Tambah Kontak")
print ("3. Keluar")



daftar_kontak = []
#nomor_kontak = []

def tambah_kontak (nama, nomor):
    kontak_baru = { "nama" : nama, "nomor" : nomor}
    daftar_kontak.append(kontak_baru)
    #nomor_kontak.append(nomor)

def tampilkan_kontak ():
    for kontak in daftar_kontak:
        print(kontak["nama"])
        print(kontak["nomor"])
            

# def tampilkan_nomor ():
#     for kontak2 in nomor_kontak:
#         print(kontak2)
#     print('----')    

while True :
    menu = int (input ("Pilih Menu :"))
    if menu == 2:
        nama = str (input ("Nama :"))
        nomor = int (input("Nomor :"))
        tambah_kontak(nama, nomor)
        print("Kontak berhasil ditambahkan")
        
    elif menu == 1:
        tampilkan_kontak()
        #tampilkan_nomor()           
        
    elif menu == 3:
        print("program selesai, sampai jumpa!")
        break
    else:
        print ("Menu tidak tersedia")
        


    






import BuildInFunction as Build
import csv
def FuncUbahJin(jinlist):
    username = input("masukkan username jin: ")

    hasil = False # sebagai validasi apakah username benar
    tipe = 0 # tipe dari jin (Pengumpul / Pembangun)
    indexJin = 0 # indeks kolom dari tipe jin tersebut.
    
    for i in range(3,103): # Loop untuk mencocokkan username jin serta mencari indeksnya
        if(username == jinlist[i][0]):
            hasil = True
            tipe = jinlist[i][2]
            indexJin = i
        else:
            continue
    if(hasil == True):
        if(tipe == "Pengumpul"):
            command = str(input('Jin ini bertipe pengumpul. yakin\ningin mengubah ke tipe "Pembangun"\n(Y/N)? '))
            while command != 'Y' and command != 'N': #validasi Input
                command = str(input("\nMasukkan input yang benar (Y/N) :  "))
            if(command == 'Y'):
                jinlist[indexJin][2] = "Pembangun"
                print("Jin telah berhasil diubah")
            else:
                print("Jin tidak jadi diubah")
        else:
            command = str(input('Jin ini bertipe pembangun. yakin\ningin mengubah ke tipe "Pengumpul"\n(Y/N)? '))
            while command != 'Y' and command != 'N': #validasi Input
                command = str(input("\nMasukkan input yang benar (Y/N): "))
            if(command == 'Y'):
                jinlist[indexJin][2] = "Pengumpul"
                print("Jin telah berhasil diubah")
                print(jinlist)
            else:
                print("Jin tidak jadi diubah")
    else:
        print("Tidak ada jin dengan username tersebut")
        FuncUbahJin(jinlist)



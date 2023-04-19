def FuncUbahJin(jinlist): #jinlist merupakan list dari user pada user.csv
    # input-Field
    username = input("masukkan username jin: ") #username dari jin yang ingin diubah role-nya
    hasil = False # sebagai validasi apakah username yang dicari ada
    tipe = 0 # tipe dari jin (Pengumpul / Pembangun)
    indexJin = 0 # indeks baris dari tipe jin tersebut.
    jumlahJin = 0 # jumlahJin akan di cek, ini untuk menghindari jika tidak terdapat jin dalam list, sehingga tidak akan terjadi infinity loop
    
    # Algorithm
    for i in range(3,103): # Loop untuk mencocokkan username jin serta mencari indeksnya, indeks dimulai dari 3 karena pada user.csv, ketika jin pertama kali di summon, jin akan berada pada indeks baris ke 3
        if(jinlist[i][0] != None):
            jumlahJin += 1 # Untuk mengecek apakah terdapat jin dalam listjin
        if(username == jinlist[i][0]): # jinlist[i][0] nama jin yang sudah disummon pada kolom username user.csv
            hasil = True
            tipe = jinlist[i][2] # jinlist[i][2] adalah role dari jin saat ini 
            indexJin = i # indeks dari jin saat ini
            break # break hanya digunakan untuk optimisasi agar tidak perlu meloop hingga selesai
        else:
            continue # continue agar loop berlanjut jika username belum ditemukan

    
    if(jumlahJin == 0):
        print("Tidak ada Jin yang dapat diubah role-nya")
        print('masukkan pilihan "summon" untuk membuat jin baru')
    elif(hasil == True): # Jika username ditemukan 
        if(tipe == "Pengumpul"): 
            command = str(input('Jin ini bertipe pengumpul. yakin\ningin mengubah ke tipe "Pembangun"\n(Y/N)? ')) # jika User menginput Y, maka role jin akan diubah, jika menginput N, maka program akan dibatalkan dan balik ke MainProgram
            while command != 'Y' and command != 'N': #validasi Input
                command = str(input("\nMasukkan input yang benar (Y/N) :  "))
            if(command == 'Y'):
                jinlist[indexJin][2] = "Pembangun" #mengubah role jin saat ini ke Pembangun
                print("Jin telah berhasil diubah")
            else: # Jika Input command == 'N'
                print("Jin tidak jadi diubah") 
        else:
            command = str(input('Jin ini bertipe pembangun. yakin\ningin mengubah ke tipe "Pengumpul"\n(Y/N)? ')) # jika User menginput Y, maka role jin akan diubah, jika menginput N, maka program akan dibatalkan dan balik ke MainProgram
            while command != 'Y' and command != 'N': #validasi Input
                command = str(input("\nMasukkan input yang benar (Y/N): "))
            if(command == 'Y'):
                jinlist[indexJin][2] = "Pengumpul" # mengubah role jin saat ini ke Pengumpul
                print("Jin telah berhasil diubah")
                print(jinlist)
            else: # Jika Input command == 'N'
                print("Jin tidak jadi diubah")

    else: # jika username jin tidak ditemukan
        print("Tidak ada jin dengan username tersebut")
        FuncUbahJin(jinlist) # jika username jin tidak ditemukan akan dilakukan pengulangan input



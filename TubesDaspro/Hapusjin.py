import BuildInFunction as Build
def HapusJin (jinlist,candilist) :
    a=0
    username = str(input("Masukkan Username = ")) # Memasukkan input username (dari file user.csv)
    for i in range(3,103): 
        if(username == jinlist[i][0]): # loop untuk mengecek apakah username yang sebelumnya diinput terdapat di file
            a+=1 # apabila username terdapat kesamaan dengan di file user.csv a bertambah 1
            indeks_jin = i
    if a>0 : # a lebih dari 0 menandakan bahwa terdapat kesamaan username yang diinput dengan yang ada di file user.csv
        pilihan = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {username} , (Y/N)?")) # input pilihan antara Y atau N
        while pilihan != 'Y' and pilihan != 'N': # loop apabila input yang dimasukkkan belum sesuai ( bukan Y atau N )
            pilihan = str(input("Masukkan input yang benar (Y/N) :  ")) # input ulang pilihan
        if(pilihan == 'Y'):
            for i in range(3):
                jinlist[indeks_jin][i] = None # untuk menghapus jin pada file user.csv sesuai dengan input usernamenya
            for i in range (0,101): # loop sampai 101 karena jumlah maks candi sampai 100
                if (username == candilist[i][1]): # mencari candi yang dibuat oleh jin yang diinput usernamenya
                    for j in range(5):
                        candilist[i][j] = None # untuk menghapus candi yang telah dibuat oleh jin yang dihapus
            print("Jin telah berhasil dihapus dari alam ghaib")
        else:
            print("Masukkan input ulang")   
            HapusJin(jinlist) # apabila input pilihan N, program akan mengulang kembali
    else:
        print("Tidak ada jin dengan username tersebut")  
        HapusJin(jinlist,candilist) # apabila input username tidak memiliki kesamaan dengan di file user.csv maka program akan mengulang kembali

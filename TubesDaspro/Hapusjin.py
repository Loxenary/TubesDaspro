import BuildInFunction as Build
def HapusJin (jinlist,candilist) :
    a=0
    username = str(input("Masukkan Username = "))
    for i in range(3,103): 
        if(username == jinlist[i][0]):
            a+=1
            indeks_jin = i
    if a>0 :
        pilihan = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {username} , (Y/N)?"))
        while pilihan != 'Y' and pilihan != 'N': 
            pilihan = str(input("Masukkan input yang benar (Y/N) :  "))
        if(pilihan == 'Y'):
            for i in range(3):
                jinlist[indeks_jin][i] = None
            for i in range (0,101):
                if (username == candilist[i][1]):
                    for j in range(5):
                        candilist[i][j] = None
            print("Jin telah berhasil dihapus dari alam ghaib")
        else:
            print("Masukkan input ulang")
            HapusJin(jinlist) 
    else:
        print("Tidak ada jin dengan username tersebut")  
        HapusJin(jinlist,candilist)


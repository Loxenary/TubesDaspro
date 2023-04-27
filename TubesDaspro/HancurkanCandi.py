def HancurkanCandi(candi):

    ID = int(input("Masukkan ID candi: "))
    cek = False
    TotalCandi = 0
    for i in range (101):
        if(candi[i][0] != None):
            TotalCandi += 1
        if candi[i][0] != ID :
            continue
        else:    
            cek = True
            no = i
            break
    if(TotalCandi == 0):
        ("Tidak ada candi yang dapat dihancurkan")
    elif cek == False :
        print("Tidak ada candi dengan ID tersebut.")
        HancurkanCandi(candi)
    else:
        pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
        def keputusan(pilihan):    
            if pilihan == "y" or pilihan == "Y" :
                print("Candi telah berhasil dihancurkan.")
                for i in range(5):
                    candi[no][i] = None
            elif pilihan == "n" or pilihan == "N" :
                print("Candi tidak jadi dihancurkan.")
            else: 
                print("Masukkan salah")
                pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
                keputusan(pilihan)
        keputusan(pilihan)
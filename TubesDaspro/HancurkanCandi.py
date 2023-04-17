
def HancurkanCandi(candi):

    ID = int(input("Masukkan ID candi: "))
    cek = False
    for i in range (101):
        if candi[i][0] != ID :
            continue
        else:    
            cek = True
            no = i
            break

    if cek == False :
        print("Tidak ada candi dengan ID tersebut.")
    else:
        pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
        def keputusan(pilihan):    
            if pilihan == "y" or pilihan == "Y" :
                print("Candi telah berhasil dihancurkan.")
                for i in range(5):
                    candi[no][i] = None
                print(candi)
            elif pilihan == "n" or pilihan == "N" :
                print("Candi tidak jadi dihancurkan.")
            else: 
                print("Masukkan salah")
                pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
                keputusan(pilihan)
        keputusan(pilihan)
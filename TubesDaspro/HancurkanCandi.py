
def HancurkanCandi(candi):
    list1 = [[0 for j in range (5)] for i in range (2)]
    for i in range (2): #sementara untuk test case
        for j in range(5):
            list1[i][j] = candi[i][j]

    ID = int(input("Masukkan ID candi: "))
    cek = False
    for i in range (2):#janlup di ganti 1001
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
                candi[no] = [0,0,0,0,0]
                print(candi)
            elif pilihan == "n" or pilihan == "N" :
                print("Candi tidak dihancurkan.")
            else: 
                print("Masukkan salah")
                pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
                keputusan(pilihan)
        keputusan(pilihan)
        
candi = [['id', 'pembuat', 'pasir' ,'batu', 'air' ],[5, 'Jin1', 1,2,3]]
HancurkanCandi(candi)
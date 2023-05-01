import BuildInFunction as build

def bangun(list_candi, bahan, jin):#untuk membangun suatu candi diperlukan bahan serta jin pembangun
    hasil1 = False
    hasil2 = False
    hasil3 = False
    #ketiga variabel dummy yang akan memverifikasi ketersediaan bahan untuk membangun candi
    Pasir = build.SearchRandomNumber(1,5,218412)
    Batu = build.SearchRandomNumber(1,5,321453)
    Air = build.SearchRandomNumber(1,5,423121)
    #Ketiga variabel yang merupakan random number generator dari range 1-5 untuk bahan yang diperlukan membuat 1 candi tertentu

    if Pasir <= int(bahan[1][2]):
        hasil1 = True #pasir yang tersedia lebih atau sama dengan pasir yang dibutuhkan maka bahan pasir tercukupi
    if Batu <= int(bahan[2][2]):
        hasil2 = True#batu yang tersedia lebih atau sama dengan batu yang dibutuhkan maka bahan batu tercukupi
    if Air <= int(bahan[3][2]):
        hasil3 = True#air yang tersedia lebih atau sama dengan air yang dibutuhkan maka bahan air tercukupi
        
    if hasil1==hasil2==hasil3==True:
        print("Candi berhasil dibangun")
        bahan[1][2] = str(int(bahan[1][2]) - Pasir)#Bahan pasir yang tersedia dikurang dengan pasir yang digunakan
        bahan[2][2] = str(int(bahan[2][2]) - Batu)#Bahan batu yang tersedia dikurang dengan batu yang digunakan
        bahan[3][2] = str(int(bahan[3][2]) - Air)#Bahan air yang tersedia dikurang dengan air yang digunakan
        for i in range(1,101):#Pengecekan list candi yang available untuk diisi
            if list_candi[i][0]!=None:#Artinya listcandi[i] tersebut berisi dan tidak dapat diisi
                continue
            else:
                list_candi[i]=[i,jin,Pasir,Batu,Air] #pengisian listcandi[i] dengan data yang baru didapat
                break    

        sisa_candi = 100-jumlah_candi(list_candi)
        if sisa_candi>0:
            print('Sisa candi yang perlu dibangun : ', sisa_candi)
        elif sisa_candi<=0:#bila jin yang dibangun lebih dari 100 maka sisa candi tetap 0 dan list candi sudah tidak bisa ditambah lagi
            print('Sisa candi yang perlu dibangun: 0.')
 
    elif hasil1==False or hasil2==False or hasil3==False:#Ketika suatu bahan tidak mencukupi
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')

def jumlah_candi (list_candi):#Function untuk menghitung berapa candi yang telah dibangun
    jumlah = 0
    for i in range(1,101):
        if(list_candi[i][0] != None):
            jumlah += 1
    return jumlah

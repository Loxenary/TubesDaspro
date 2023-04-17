import BuildInFunction as build

def bangun(list_candi, bahan, jin):
    hasil1 = False
    hasil2 = False
    hasil3 = False
    Pasir = build.SearchRandomNumber(1,5,218412)
    Batu = build.SearchRandomNumber(1,5,321453)
    Air = build.SearchRandomNumber(1,5,423121)
    if Pasir <= int(bahan[1][2]):
        hasil1 = True
        bahan[1][2] = str(int(bahan[1][2] - Pasir))
    if build.SearchRandomNumber(1,5,321453)<=Batu:
        hasil2 = True
        bahan[2][2] = str(int(bahan[2][2] - Batu))
    if build.SearchRandomNumber(1,5,423121)<=Air:
        hasil3 = True
        bahan[2][3] = str(int(bahan[3][2] - Air))
    if hasil1==hasil2==hasil3==True:
        print("Candi berhasil dibangun")
        for i in range(1,101):
            if list_candi[i][0]!=0:
                continue
            else:
                list_candi[i]=[i+1,jin,Pasir,Batu,Air]
                break    

        sisa_candi = 100-jumlah_candi(list_candi)
        if sisa_candi>0:
            print('Sisa candi yang perlu dibangun : ', sisa_candi)
        elif sisa_candi<=0:
            print('Sisa candi yang perlu dibangun: 0.')
 
    elif hasil1==False or hasil2==False or hasil3==False:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')

def jumlah_candi (list_candi):
    jumlah = 0
    for i in range(1,101):
        if(list_candi[i][0] == None):
            jumlah += 1
    return jumlah
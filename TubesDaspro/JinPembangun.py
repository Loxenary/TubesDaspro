import BuildInFunction as build
import bahan as bah
candi_terbangun = 0
list_candi=[[0 for j in range(5)]for i in range(1001)]
def bangun(candi_terbangun):
    hasil1 = False
    hasil2 = False
    hasil3 = False
    if build.SearchRandomNumber(1,5,218412)<=bah.pasir:
        hasil1 = True
        pasir_dipakai = build.SearchRandomNumber(1,5,21842)
        bah.pasir=bah.pasir-pasir_dipakai
    if build.SearchRandomNumber(1,5,321453)<=bah.batu:
        hasil2 = True
        batu_dipakai = build.SearchRandomNumber(1,5,321453)
        bah.batu = bah.batu-batu_dipakai
    if build.SearchRandomNumber(1,5,423121)<=bah.air:
        hasil3 = True
        air_dipakai = build.SearchRandomNumber(1,5,423121)
        bah.air = bah.air-air_dipakai
    if hasil1==hasil2==hasil3==True:
        print("Candi berhasil dibangun")
        for i in range(0,1001):
            if list_candi[i][0]!=0:
                continue
            else:
                list_candi[i]=[i+1,'jin',pasir_dipakai,batu_dipakai,air_dipakai]
                break    
        for i in range(1,1001):
            if list_candi[i][1]!=0:
                candi_terbangun+=1  
        sisa_candi = 99-candi_terbangun
        if sisa_candi>0:
            print('Sisa candi yang perlu dibangun : ', sisa_candi)
        elif sisa_candi<=0:
            print('Sisa candi yang perlu dibangun: 0.')
 
    elif hasil1==False or hasil2==False or hasil3==False:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')
bangun(candi_terbangun)
bangun(candi_terbangun)
bangun(candi_terbangun)
bangun(candi_terbangun)
bangun(candi_terbangun)
bangun(candi_terbangun)
print(list_candi)
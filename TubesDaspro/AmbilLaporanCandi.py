from JinPembangun import list_candi
def sumcol(i):
    total=0
    for j in range(1001):
        if list_candi==0:
            continue
        else:
            total+=list_candi[j][i]
def laporancandi():
    banyak_candi=0
    harga_candi=[0 for i in range(1001)]
    total_pasir=total_batu=total_air=0
    for i in range(1001):
        if list_candi[i][1]==0:
            continue
        else:
            banyak_candi=banyak_candi+1
            total_pasir=total_pasir+list_candi[i][2]
            total_batu=total_batu+list_candi[i][3]
            total_air=total_air+list_candi[i][4]
            harga_candi[i] = 10000*list_candi[i][2]+15000*list_candi[i][3]+list_candi[i][4]*7500
        max=min=harga_candi[0]
        idmax=idmin=0
        for i in range(1001):
            if max<harga_candi[i]:
                max=harga_candi[i]
                idmax = i
        for i in range(1001):
            if min>harga_candi[i] and harga_candi[i]!=0:
                min=harga_candi[i]
                idmin = i
    if banyak_candi==0:
            print('Total Candi : 0')
            print('Total pasir yang digunakan : 0')
            print('Total batu yang digunakan : 0')
            print('Total air yang digunakan : 0')
            print('ID Candi Termahal : -')
            print('ID Candi Termurah : -')
    else:
            print('Total Candi :',banyak_candi)
            print('Total pasir yang digunakan:',total_pasir)
            print('Total batu yang digunakan:',total_batu)
            print('Total air yang digunakan',total_air)
            print('ID Candi Termahal :',idmax+1,'(',max,')')
            print('ID Candi Termurah :',idmin+1,'(',min,')')
laporancandi()

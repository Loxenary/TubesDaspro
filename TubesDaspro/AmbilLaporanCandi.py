
def laporancandi(list_candi):
    banyak_candi=0
    harga_candi=[0 for i in range(101)]
    total_pasir=total_batu=total_air=0
    for i in range(1,101):
        if list_candi[i][1]==None:
            continue
        else:
            banyak_candi += 1
            total_pasir += int(list_candi[i][2])
            total_batu += int(list_candi[i][3])
            total_air += int(list_candi[i][4])
            harga_candi[i] = 10000*int(list_candi[i][2])+15000*int(list_candi[i][3])+int(list_candi[i][4])*7500
        max=min=harga_candi[1]
        idmax=idmin=0
        for i in range(101):
            if max<harga_candi[i]:
                max=harga_candi[i]
                idmax = i
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
            print(f'ID Candi Termahal :{idmax+1} ({max})')
            print(f'ID Candi Termurah :{idmin} ({min})')

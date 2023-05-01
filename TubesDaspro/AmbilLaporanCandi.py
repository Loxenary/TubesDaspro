
def laporancandi(list_candi):
    banyak_candi=0 #Initial variable yang nanti diubah sesuai dengan jumlah candi yang terbangun
    harga_candi=[0 for i in range(101)] #Deklarasi list untuk harga dari tiap candi
    total_pasir=total_batu=total_air=0 # Initial variabel banyak bahan pasir/batu/air yang digunakan untuk pembangunan total seluruh candi
    for i in range(1,101):
        if list_candi[i][1]==None:#Pemrosesan deklarasi list sebelumnya menjadi list yang berisi value selain 0
            continue
        else: #Jika elemen listcandi[i] memiliki value selain 0 berarti candi tersebut exist
            banyak_candi += 1 #Jumlah candi ditambah 1 karena terbukti listcandi[i] merupakan candi valid
            total_pasir += int(list_candi[i][2])#Penambahan jumlah pasir dengan banyak pasir yang digunakan candi[i]
            total_batu += int(list_candi[i][3])#Penambahan jumlah batu dengan banyak pasir yang digunakan candi[i]
            total_air += int(list_candi[i][4])#Penambahan jumlah air dengan banyak pasir yang digunakan candi[i]
            harga_candi[i] = 10000*int(list_candi[i][2])+15000*int(list_candi[i][3])+int(list_candi[i][4])*7500
            #Pengonversian bahan yang dipakai suatu candi menjadi sebuah integer dengan metode 10000*pasir+15000*batu+7500*air dan dimasukan ke list
        max=min=harga_candi[1] #Dummy variabel untuk penentuan max dan min list harga candi
        idmax=idmin=0 #Initial variabel penentuan max dan min
        for i in range(101): #Metode pencarian max dan min
            if max<harga_candi[i]:
                max=harga_candi[i]
                idmax = i
            if min>harga_candi[i] and harga_candi[i]!=0:
                min=harga_candi[i]
                idmin = i
    if banyak_candi==0:#Output bila tidak ada candi yang dibangun
            print('Total Candi : 0')
            print('Total pasir yang digunakan : 0')
            print('Total batu yang digunakan : 0')
            print('Total air yang digunakan : 0')
            print('ID Candi Termahal : -')
            print('ID Candi Termurah : -')
    else:#Terbangun minimal 1 candi
            print('Total Candi :',banyak_candi)
            print('Total pasir yang digunakan:',total_pasir)
            print('Total batu yang digunakan:',total_batu)
            print('Total air yang digunakan',total_air)
            print(f'ID Candi Termahal :{idmax+1} ({max})')#Bila terdapat 2 candi atau lebih dengan harga yang sama maka didahulukan yang id pertama
            print(f'ID Candi Termurah :{idmin} ({min})')

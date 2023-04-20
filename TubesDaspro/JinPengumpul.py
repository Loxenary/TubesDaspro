import BuildInFunction as Build

def JinPengumpul (bahan_bangunan): 
    #bahan_bangunan adalah sebuah array yang berisi jumlah dari pasir , batu , dan air yang sudah ada 
    #Build.SearchRandomNumber adalah sebuah fungsi yang digunakan untuk mencari angka dengan maksimum 5
    pasir = Build.SearchRandomNumber(0,5,1) #pasir adalah variable untuk menyimpan hasil random number untuk bahan pasir
    batu = Build.SearchRandomNumber(0,5,2) #batu adalah variable untuk menyimpan hasil random number untuk bahan batu
    air = Build.SearchRandomNumber(0,5,3) #air adalah variable untuk menyimpan hasil random number untuk bahan air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.") #print untuk menghasilkan keluaran berapa saja bahan yang didapat
    
    #syntax untuk menambahkan bahan-bahan yang sudah didapat ke array bahan_bangunan
    bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir) 
    bahan_bangunan[2][2] = str(int(bahan_bangunan[1][2]) + batu)
    bahan_bangunan[3][2] = str(int(bahan_bangunan[1][2]) + air)
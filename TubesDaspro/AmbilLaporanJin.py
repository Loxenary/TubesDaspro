def AmbilLaporanJin(listjin,candilist,bahanlist): 
    # listjin (list dari user dari index 3 - 103), candilist (list yang berisi candi yang sudah terbangun), bahanlist (list yang berisi bahan yang saat ini tersedia)
    jumlahJin = 0 # variable jumlahjin yang ada saat ini
    jumlahJinPengumpul = 0 # variable yang berisi jumlahjin yang punya role Pengumpul
    jumlahJinPembangun = 0 # variable yang berisi jumlahjin yang punya role Pembangun
    jinPalingRajin = "-" # variable yang berisi nama jin paling banyak membuat candi (dengan urutan leksografis paling tinggi)
    jinPalingMalas = "-" # variable yang berisi nama jin paling sedikit membuat candi (dengan urutan leksofrafis paling tinggi)
    for i in range(3,103): # loop untuk listjin, dimulai dari indeks 3 karena jin yang muncul baru dimulai pada indeks 3, diakhiri 103 karena jumlah jin maks adalah 100
        if(listjin[i][2] == "Pengumpul"): 
            jumlahJinPengumpul += 1 
            jumlahJin += 1
            jinPalingRajin = jinTerRajin(listjin[i][0],candilist,jinPalingRajin) # jinPalingRajin tetap dipanggil karena ada kemungkinan jin yang sudah membuat candi diubah role nya
            # jinPalingMalas tidak dipanggil karena hampir keseluruhan jinPengumpul tidak pernah membuat candi
        elif (listjin[i][2] == "Pembangun"):
            jumlahJinPembangun += 1
            jumlahJin += 1
            jinPalingRajin = jinTerRajin(listjin[i][0],candilist,jinPalingRajin) 
            jinPalingMalas = jinTerMalas(listjin[i][0],candilist,jinPalingMalas)
        else: # jika hasil list[i][2] == None atau tidak ada jin
            continue
        # jumlah jin ditambahkan dari 2 if statement karena akumulasi keduanya akan menghasilkan jumlah jin keseluruhan
    
    # if statement dibawah hanya digunakan agar hasilnya menjadi "-" karena jika tidak ditemukan JinTerajin atau Termalas maka akan menghasilkan None
    if(jinPalingRajin == None):
        jinPalingRajin = "-"
        if(jinPalingMalas == None):
            jinPalingMalas = "-"
    print(f'''
    \r> Total Jin : {jumlahJin}
    \r> Total Jin Pengumpul : {jumlahJinPengumpul}
    \r> Total Jin Pembangun : {jumlahJinPembangun}
    \r> Jin Terajin : {jinPalingRajin}
    \r> Jin Termalas : {jinPalingMalas}
    \r> Jumlah Pasir : {bahanlist[1][2]}
    \r> Jumlah Air : {bahanlist[3][2]}
    \r> Jumlah Batu : {bahanlist[2][2]}''')
    # bahanlist[1][2] adalah jumlah pasir yang tersedia saat ini
    # bahanlist[2][2] adalah jumlah Batu yang tersedia saat ini
    # bahanlist[3][2] adalah jumlah air yang tersedia saat ini

# jumlahCandi adalah jumlah candi yang dibuat oleh suatu jin
def jumlahCandi(jin,candilist): # parameter jin adalah nama suatu jin, candilist adalah list dari candi yang ada saat ini
    jumlahCandi = 0
    for i in range(1,101):
        if(candilist[i][1] == jin):  
            jumlahCandi += 1
            
    return jumlahCandi

# jinTerRajin adalah function yang digunakan untuk menentukan jin paling banyak membuat candi saat itu
# Algoritma
'''
PalingRajin akan mengambil jumlah candi dari jin paling rajin saat itu, kemudian akan di compare dengan jumlah candi pada jin.
jika jumlah candi dari jin yang dibandingkan saat ini lebih banyak daripada yang paling rajin saat itu, maka akan me-return jin sebagai nama jinPalingRajin terbaru
jika jumlah candinya sama, maka akan dibandingkan jumlah leksografis nya antara kedua jin. jika jin memiliki jumlah leksografis yang lebih besar, maka akan me-return
jin sebagai jinPalingRajin saat itu dan jika lebih rendah maka jinPalingRajin akan tetap.
'''
def jinTerRajin(jin,candilist,jinPalingRajin): # jin adalah nama jin yang akan dibandingkan, candilist adalah list candi yang sudah ada saat ini, jinPalingRajin adalah nama jin yang paling sering membuat jin saat itu  
    PalingRajin = jumlahCandi(jinPalingRajin,candilist)
    if(jumlahCandi(jin,candilist) > PalingRajin):
        return jin
    elif(jumlahCandi(jin,candilist) == PalingRajin):
        if(jin > jinPalingRajin):
            return jin

# jinTerajin adalah function yang digunakan untuk menentukan jin paling sedikit membuat candi saat itu
# Algoritma
'''
untuk algoritma kurang lebih sama dengan function jinTerRajin, perbedaan nya adalah jika jumlah candi dari jin yang ada kurang dari yang paling malas
saat itu, maka baru akan me-return jin sebagai jinTerMalas. jika jumlah nya sama akan di compare jumlah leksografisnya, sama dengan function jinTerRajin
jika jumlah leksografis jin lebih besar dari jinPalingMalas maka akan me-return jin sebagai jinPalingMalas terbaru dan jika sebaliknya, maka jinPalingMalas tidak akan berubah. 
'''
def jinTerMalas(jin,candilist,jinPalingMalas): # jin adalah nama jin yang akan dibandingkan, candilist adalah list candi yang sudah ada, jinPalingMalas adalah jin yang paling sedikit membuat candi pada saat itu.
    PalingMalas = jumlahCandi(jinPalingMalas,candilist)
 
    if(jumlahCandi(jin,candilist) < PalingMalas):
        return jin
    elif(jumlahCandi(jin,candilist) == PalingMalas):
        if(jin > jinPalingMalas):
            return jin
           


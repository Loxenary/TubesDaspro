def AmbilLaporanJin(userlist,candilist,bahanlist): 
    # userlist (list dari user dari index 3 - 103), candilist (list yang berisi candi yang sudah terbangun), bahanlist (list yang berisi bahan yang saat ini tersedia)
    jumlahJin = 0 # variable jumlahjin yang ada saat ini
    jumlahJinPengumpul = 0 # variable yang berisi jumlahjin yang punya role Pengumpul
    jumlahJinPembangun = 0 # variable yang berisi jumlahjin yang punya role Pembangun
    jinPalingRajin = "-" # variable yang berisi nama jin paling banyak membuat candi (dengan urutan leksografis paling tinggi)
    jinPalingMalas = "-" # variable yang berisi nama jin paling sedikit membuat candi (dengan urutan leksofrafis paling tinggi)
    inisialisasi = False # variable untuk validasi inisialisasi variable jinPalingRajin dan jinPalingMalas
    jumlahPembangunCandi = 0 # variable untuk validasi jumlah jin yang membangun candi dari jinPengumpul dan jinPembangun

    for i in range(3,103): # loop untuk userlist, dimulai dari indeks 3 karena jin yang muncul baru dimulai pada indeks 3, diakhiri 103 karena jumlah jin maks adalah 100
        if(userlist[i][2] == "Pengumpul"): 
            jumlahJinPengumpul += 1 
            jumlahJin += 1

            if(jumlahCandi(userlist[i][0], candilist) > 0): # karena ketika jin diubah, candinya tidak hilang, maka jinTersebut diasumsikan bisa menjadi jinPalingRajin dan jinPalingMalas.
                # diasumsikan, jin baru akan dimasukkan hitungan jika pernah setidaknya sekali membuat candi, hal ini dikarenakan, kebanyakan dari jinPengumpul tidak mempunyai candi
                if(inisialisasi == False): # jika terdapat jinPengumpul yang pernah membangun candi, dan dipanggil lebih dulu daripada jinPembangun
                    jinPalingMalas = userlist[i][0]
                    jinPalingRajin = userlist[i][0]
                    inisialisasi = True
                jumlahPembangunCandi += 1
                jinPalingRajin = jinTerRajin(userlist[i][0],candilist,jinPalingRajin) # jinPalingRajin dan jinPalingMalas tetap dipanggil karena ada kemungkinan jin yang sudah membuat candi, saat diubah role nya
                jinPalingMalas = jinTerMalas(userlist[i][0],candilist,jinPalingMalas) 

        elif (userlist[i][2] == "Pembangun"):
            jumlahJinPembangun += 1
            jumlahJin += 1
            jumlahPembangunCandi += 1

            if(inisialisasi == False): # inisialisasi jinPalingRajin dan jinPalingMalas paling awal
                jinPalingRajin = userlist[i][0]
                jinPalingMalas =userlist[i][0]
                inisialisasi = True

            jinPalingRajin = jinTerRajin(userlist[i][0],candilist,jinPalingRajin) 
            jinPalingMalas = jinTerMalas(userlist[i][0],candilist,jinPalingMalas)
        else: # jika hasil userlist[i][2] == None atau tidak ada jin
            continue
        # jumlah jin ditambahkan dari 2 if statement karena akumulasi keduanya akan menghasilkan jumlah jin keseluruhan
    
    if(jumlahPembangunCandi <= 1): # asumsi: jika hanya terdapat 0-1 jin pembangun, maka dianggap tidak ada yang paling rajin maupun malas 
        jinPalingMalas = "-"
        jinPalingRajin = "-"
    print(f'''
    \r> Total Jin : {jumlahJin}
    \r> Total Jin Pengumpul : {jumlahJinPengumpul}
    \r> Total Jin Pembangun : {jumlahJinPembangun}
    \r> Jin Terajin : {jinPalingRajin}
    \r> Jin Termalas : {jinPalingMalas}
    \r> Jumlah Pasir : {bahanlist[1][2]} unit
    \r> Jumlah Air : {bahanlist[3][2]} unit
    \r> Jumlah Batu : {bahanlist[2][2]} unit''')
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
jika jumlah candinya sama, maka akan dibandingkan jumlah leksografis nya antara kedua jin. jika jin memiliki jumlah leksografis yang lebih kecil, maka akan me-return
jin sebagai jinPalingRajin saat itu dan jika lebih besar maka jinPalingRajin akan tetap.
'''
def jinTerRajin(jin,candilist,jinPalingRajin): # jin adalah nama jin yang akan dibandingkan, candilist adalah list candi yang sudah ada saat ini, jinPalingRajin adalah nama jin yang paling sering membuat jin saat itu  
    PalingRajin = jumlahCandi(jinPalingRajin,candilist)
    if(jumlahCandi(jin,candilist) > PalingRajin):
        return jin
    elif(jumlahCandi(jin,candilist) == PalingRajin):
        if(jin < jinPalingRajin): # menghitung leksografisnya
            return jin
        else:
            return jinPalingRajin
    else:
        return jinPalingRajin

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
        else: # jumlah leksografisnya lebih sedikit
            return jinPalingMalas
    else: # jumlahCandi(jin,candilist) > PalingMalas
        return jinPalingMalas
           


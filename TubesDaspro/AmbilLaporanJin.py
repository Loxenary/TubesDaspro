import BuildInFunction as Build
def AmbilLaporanJin(listjin):
    jumlahJin = 0
    jumlahJinPengumpul = 0
    jumlahJinPembangun = 0
    for i in range(3,103):
        if(listjin[i][2] == "Pengumpul"):
            jumlahJinPengumpul += 1
            jumlahJin += 1
        elif (listjin[i][2] == "Pembangun"):
            jumlahJinPembangun += 1
            jumlahJin += 1
        else:
            continue
    

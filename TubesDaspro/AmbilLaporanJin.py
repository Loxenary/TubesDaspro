import BuildInFunction as Build
def AmbilLaporanJin(listjin,candilist,bahanlist):
    jumlahJin = 0
    jumlahJinPengumpul = 0
    jumlahJinPembangun = 0
    jinPalingRajin = "-"
    jinPalingMalas = "-"
    for i in range(3,103):
        if(listjin[i][2] == "Pengumpul"):
            jumlahJinPengumpul += 1
            jumlahJin += 1
        elif (listjin[i][2] == "Pembangun"):
            jumlahJinPembangun += 1
            jumlahJin += 1
            jinPalingRajin = jinTerRajin(listjin[i][0],candilist,jinPalingRajin)
            jinPalingMalas = jinTerMalas(listjin[i][0],candilist,jinPalingMalas)
        else:
            continue
    
    print(f'''
    \r> Total Jin : {jumlahJin}
    \r> Total Jin Pengumpul : {jumlahJinPengumpul}
    \r> Total Jin Pembangun : {jumlahJinPembangun}
    \r> Jin Terajin : {jinPalingRajin}
    \r> Jin Termalas : {jinPalingMalas}
    \r> Jumlah Pasir : {bahanlist[1][2]}
    \r> Jumlah Air : {bahanlist[3][2]}
    \r> Jumlah Batu : {bahanlist[2][2]}''')
    
def jumlahCandi(jin,candilist):
    jumlahCandi = 0
    for i in range(1,101):
        if(candilist[i][1] == jin):  
            jumlahCandi += 1
            
    return jumlahCandi

def jinTerRajin(jin,candilist,jinPalingRajin):
    PalingRajin = jumlahCandi(jinPalingRajin,candilist)
    if(jumlahCandi(jin,candilist) > PalingRajin):
        return jin
    elif(jumlahCandi(jin,candilist) == PalingRajin):
        if(jin > jinPalingRajin):
            return jin


def jinTerMalas(jin,candilist,jinPalingMalas):
    PalingMalas = jumlahCandi(jinPalingMalas,candilist)
 
    if(jumlahCandi(jin,candilist) < PalingMalas):
        return jin
    elif(jumlahCandi(jin,candilist) == PalingMalas):
        if(jin > jinPalingMalas):
            return jin
           


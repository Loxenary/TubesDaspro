import BuildInFunction as Build
def batch (batch,jinlist,candilist,bahanlist):
    totaljinPengumpul=0
    totalpasir  = int(bahanlist[1][2])
    totalair = int(bahanlist[3][2])
    totalbatu = int(bahanlist[2][2])
    totalcandi = 0
    totaljinPembangun=0
    butuhpasir = 0
    butuhair = 0
    butuhbatu = 0
    jumlahAktifPembangun = 0 # asumsi : jika jumlah candi jika dilakukan batchbangun akan lebih dari 100, hanya jin yang membangun candi saja yang akan dihitung.
    if batch == "BatchKumpul":
        for i in range(3,103): 
            if jinlist[i][2] == "Pengumpul":
                totaljinPengumpul +=1
        for i in range (totaljinPengumpul):
            totalpasir += Build.SearchRandomNumber(0,5,i+1)
            totalbatu += Build.SearchRandomNumber(0,5,i+3)
            totalair += Build.SearchRandomNumber(0,5,i+2)
        if totaljinPengumpul == 0 :
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else :
            print(f"Mengerahkan {totaljinPengumpul} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")
            bahanlist[1][2] = totalpasir
            bahanlist[2][2] = totalbatu
            bahanlist[3][2] = totalair
    elif batch == "BatchBangun":
        tempCandi = [[None for i in range(5)]for j in range(101)]
        for i in range(3,103): 
            if jinlist[i][2] == "Pembangun":
                totaljinPembangun +=1
                butuhpasir = Build.SearchRandomNumber(1,5,(i+1)*2)
                butuhbatu = Build.SearchRandomNumber(1,5,(i+3)*11)
                butuhair = Build.SearchRandomNumber(1,5,(i+2)*39) 
                if butuhpasir <= totalpasir and butuhair <= totalair and butuhbatu <= totalbatu:
                    totalcandi +=1
                    totalpasir -= butuhpasir
                    totalair -= butuhair
                    totalbatu -= butuhbatu
                    for j in range(101):
                        if(tempCandi[j][1] == None):
                            tempCandi[j][1] = jinlist[i][0]
                            tempCandi[j][2] = butuhpasir
                            tempCandi[j][3] = butuhbatu
                            tempCandi[j][4] = butuhpasir
                            break
                else :
                    totalcandi = 0
                    break
        if(totaljinPembangun == 0):
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

        if totalcandi == 0 :
            print(f"Bangun gagal. Kurang {Build.Diffrence(totalpasir,butuhpasir)} pasir, {Build.Diffrence(totalbatu,butuhbatu)} batu, dan {Build.Diffrence(totalair,butuhair)} air.")
        else :
            
            for i in range(totalcandi):
                for j in range(101):
                    if(candilist[j][0] == None):
                        jumlahAktifPembangun+= 1 # menghitung jumlah pasti dari totalcandi yang akan dibangun
                        candilist[j][0] = j
                        candilist[j][1] = tempCandi[i][1]
                        candilist[j][2] = tempCandi[i][2]
                        candilist[j][3] = tempCandi[i][3]
                        candilist[j][4] = tempCandi[i][4]
                        break
                    else:
                        continue
            totalcandi = jumlahAktifPembangun # totalcandi akan sama jumlahnya dengan jumlah pembangun yang aktif. 
            print(f"Mengerahkan {jumlahAktifPembangun} jin untuk membangun candi dengan total bahan {butuhpasir} pasir, {butuhbatu} batu, dan {butuhair} air.")
            print(f"Jin berhasil membangun total {totalcandi} candi.")
                
        
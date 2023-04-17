import BuildInFunction as Build
import JinPembangun as pembangun
def batch (batch,jinlist,candilist,bahanlist):
    totaljinPengumpul=0
    totalpasir  = int(bahanlist[1][2])
    totalair = int(bahanlist[2][2])
    totalbatu = int(bahanlist[3][2])
    totalcandi = 0
    totaljinPembangun=0
    butuhpasir = 0
    butuhair = 0
    butuhbatu = 0
    if batch == "BatchKumpul":
        for i in range(3,103): 
            if jinlist[i][2] == "Pengumpul":
                totaljinPengumpul +=1
        for i in range (totaljinPengumpul):
            totalpasir += Build.SearchRandomNumber(1,5,i+1)
            totalbatu += Build.SearchRandomNumber(1,5,i+3)
            totalair += Build.SearchRandomNumber(1,5,i+2)
        if totaljinPengumpul == 0 :
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else :
            print(f"Mengerahkan {totaljinPengumpul} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")

    elif batch == "BatchBangun":
        print(totalpasir)
        for i in range(0,5): 
            if jinlist[i][2] == "Pembangun":
                totaljinPembangun +=1
        if totaljinPembangun>0 :
            for i in range (totaljinPembangun):
                butuhpasir += Build.SearchRandomNumber(1,5,(i+1)*2)
                butuhbatu += Build.SearchRandomNumber(1,5,(i+3)*11)
                butuhair += Build.SearchRandomNumber(1,5,(i+2)*39) 
                if butuhpasir <= totalpasir and butuhair <= totalair and butuhbatu <= totalbatu:
                    totalcandi +=1
                    totalpasir -= butuhpasir
                    totalair -= butuhair
                    totalbatu -= butuhbatu
                else :
                    totalcandi = 0
                    break
            if totalcandi == 0 :
                print(f"Bangun gagal. Kurang {Build.Diffrence(totalpasir,butuhpasir)} pasir, {Build.Diffrence(totalbatu,butuhbatu)} batu, dan {Build.Diffrence(totalair,butuhair)} air.")
            else :
                print(f"Mengerahkan {totaljinPembangun} jin untuk membangun candi dengan total bahan {butuhpasir} pasir, {butuhbatu} batu, dan {butuhair} air.")
                print(f"Jin berhasil membangun total {totalcandi} candi.")
                
        else :
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

import BuildInFunction as Build
def batch (jinlist):
    totaljin=0
    totalpasir  =0
    totalair = 0
    totalbatu = 0
    totalcandi = 0
    totaljin2=0
    butuhpasir = 0
    butuhair = 0
    butuhbatu = 0
    batch = str(input("Silahkan pilih batch apa (Batchkumpul/Batchbangun)?"))
    while batch != "Batchkumpul" and batch != "Batchbangun":
        batch = str(input("Silahkan ulangi pilihan batch apa (Batchkumpul/Batchbangun)?"))

    if batch == "Batchkumpul":
        for i in range(0,5): 
            if jinlist[i][2] == "Pengumpul":
                totaljin +=1
        for i in range (totaljin):
            totalpasir += Build.SearchRandomNumber(1,5,10)
            totalbatu += Build.SearchRandomNumber(1,5,10)
            totalair += Build.SearchRandomNumber(1,5,10)
        if totaljin == 0 :
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else :
            print(f"Mengerahkan {totaljin} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")

    elif batch == "Batchbangun":
        print(totalpasir)
        for i in range(0,5): 
            if jinlist[i][2] == "Pembangun":
                totaljin2 +=1
        if totaljin2>0 :
            for i in range (totaljin2):
                butuhpasir += Build.SearchRandomNumber(1,5,10)
                butuhbatu += Build.SearchRandomNumber(1,5,10)
                butuhair += Build.SearchRandomNumber(1,5,10) 
                if butuhpasir > totalpasir and butuhair > totalair and butuhbatu > totalbatu:
                    totalcandi +=1
                    totalpasir -= butuhpasir
                    totalair -= butuhair
                    totalbatu -= butuhbatu
                else :
                    break
            if totalcandi == 0 :
                print(f"Bangun gagal. Kurang {butuhpasir-totalpasir} pasir, 5 batu, dan 32 air.")
            else :
                print(f"Mengerahkan {totaljin2} jin untuk membangun candi dengan total bahan {butuhpasir} pasir, {butuhbatu} batu, dan {butuhair} air.")
                print(f"Jin berhasil membangun total {totalcandi} candi.")
        else :
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")


    
k = [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'],['Jin1','IffritGanteng','Pembangun'],['Jin2','iffritJelek','Pembangun']]
batch(k)

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
    butuhbatu = 0 # Sebagai variabel awal seperti yang diatas
    jumlahAktifPembangun = 0 # asumsi : jika jumlah candi jika dilakukan batchbangun akan lebih dari 100, hanya jin yang membangun candi saja yang akan dihitung.
    if batch == "BatchKumpul": # Untuk menentukan batch yang dipilih oleh user
        for i in range(3,103): # loop untuk mencari jin dengan role pengumpul pada list
            if jinlist[i][2] == "Pengumpul":
                totaljinPengumpul +=1 # jika ditemukan jin dengan role pengumpul, akan bertambah 1
        for i in range (totaljinPengumpul):
            totalpasir += Build.SearchRandomNumber(0,5,i+1) # total pasir yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
            totalbatu += Build.SearchRandomNumber(0,5,i+3) # total batu yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
            totalair += Build.SearchRandomNumber(0,5,i+2) # total air yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
        if totaljinPengumpul == 0 : # apabila tidak terdapat jin bertipe pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else :
            print(f"Mengerahkan {totaljinPengumpul} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")
            bahanlist[1][2] = totalpasir # total pasir dimasukkan ke bahanlist
            bahanlist[2][2] = totalbatu # total batu dimasukkan ke bahanlist
            bahanlist[3][2] = totalair # total air dimasukkan ke bahanlist
    elif batch == "BatchBangun":
        tempCandi = [[None for i in range(5)]for j in range(101)]
        for i in range(3,103): 
            if jinlist[i][2] == "Pembangun": # untuk menentukan apakah jin pada jinlist tersebut bertipe pembangun
                totaljinPembangun +=1 # variabel totaljinpembangun akan bertambah 1 bila ditemukan jin bertipe pembangun
                butuhpasir = Build.SearchRandomNumber(1,5,(i+1)*2) # total pasir yang digunakan ditentukan dengan number random generator dari buildinfunction
                butuhbatu = Build.SearchRandomNumber(1,5,(i+3)*11) # total batu yang digunakan ditentukan dengan number random generator dari buildinfunction
                butuhair = Build.SearchRandomNumber(1,5,(i+2)*39) # total air yang digunakan ditentukan dengan number random generator dari buildinfunction
                if butuhpasir <= totalpasir and butuhair <= totalair and butuhbatu <= totalbatu:  # jika bahan-bahan yang dibutuhkan mencukupi
                    totalcandi +=1 # maka candi akan terbangun dan totalcandi bertambah 1
                    totalpasir -= butuhpasir # jumlah totalpasir akan berkurang sesuai jumlah pasir yang digunakan
                    totalair -= butuhair # jumlah totalair akan berkurang sesuai jumlah air yang digunakan
                    totalbatu -= butuhbatu # jumlah totalbatu akan berkurang sesuai jumlah batu yang digunakan
                    for j in range(101):
                        if(tempCandi[j][1] == None): # sebagai list sementara tempat candi dibangun untuk melihat apakah keseluruhan candi dapat dibangun
                            tempCandi[j][1] = jinlist[i][0] # memasukkan username jin ke list sementara
                            tempCandi[j][2] = butuhpasir # memasukkan jumlah pasir yang dipakai ke list sementara
                            tempCandi[j][3] = butuhbatu # memasukkan jumlah batu yang dipakai jin ke list sementara
                            tempCandi[j][4] = butuhpasir # memasukkan jumlah air yang dipakai ke list sementara
                            break
                else :
                    totalcandi = 0 # Jika terdapat bahan yang tak mencukupi, candi tidak akan terbangun
                    break
        if(totaljinPembangun == 0): # Jika tidak ada jin pembangun maka tidak dapat melakukan bangun candi
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

        if totalcandi == 0 : # Untuk output kekurangan bahan untuk pembangunan candi
            print(f"Bangun gagal. Kurang {Build.Diffrence(totalpasir,butuhpasir)} pasir, {Build.Diffrence(totalbatu,butuhbatu)} batu, dan {Build.Diffrence(totalair,butuhair)} air.")
        else :
            
            for i in range(totalcandi):
                for j in range(101): # Bagian ini Untuk memindahkan value dari list sementara ke candilist
                    if(candilist[j][0] == None): 
                        jumlahAktifPembangun+= 1 # menghitung jumlah pasti dari totalcandi yang akan dibangun
                        candilist[j][0] = j 
                        candilist[j][1] = tempCandi[i][1] 
                        candilist[j][2] = tempCandi[i][2]
                        candilist[j][3] = tempCandi[i][3]
                        candilist[j][4] = tempCandi[i][4]
                        bahanlist[1][2] = totalpasir
                        bahanlist[3][2] = totalair
                        bahanlist[2][2] = totalbatu
                        break
                    else:
                        continue
            totalcandi = jumlahAktifPembangun # totalcandi akan sama jumlahnya dengan jumlah pembangun yang aktif. 
            print(f"Mengerahkan {jumlahAktifPembangun} jin untuk membangun candi dengan total bahan {butuhpasir} pasir, {butuhbatu} batu, dan {butuhair} air.")
            print(f"Jin berhasil membangun total {totalcandi} candi.")
                
        

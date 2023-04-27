import BuildInFunction as Build
import JinPembangun as pembangun
def batch (batch,jinlist,candilist,bahanlist):
    totaljinPengumpul=0
    totalpasir  = int(bahanlist[1][2]) #letak total pasir pada list
    totalair = int(bahanlist[3][2]) #letak total air pada list
    totalbatu = int(bahanlist[2][2]) #letak total batu pada list
    totalcandi = 0
    totaljinPembangun=0
    butuhpasir = 0
    butuhair = 0
    butuhbatu = 0 # Sebagai variabel seperti yang diatasnya
    if batch == "BatchKumpul": # apabila ingin mengumpulkan bahan
        for i in range(3,103): 
            if jinlist[i][2] == "Pengumpul": # untuk menentukan apakah jin pada jinlist tersebut bertipe pengumpul
                totaljinPengumpul +=1 # variabel totaljinpengumpul akan bertambah 1 bila ditemukan jin bertipe pengumpul
        for i in range (totaljinPengumpul): # pengulangan akan dilakukan sebanyak jumlah jin pengumpul
            totalpasir += Build.SearchRandomNumber(0,5,i+1) # total pasir yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
            print(Build.SearchRandomNumber(0,5,i+1))
            totalbatu += Build.SearchRandomNumber(0,5,i+3) # total batu yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
            
            totalair += Build.SearchRandomNumber(0,5,i+2)# total air yang berhasil didapat ditentukan dengan number random generator dari buildinfunction
        if totaljinPengumpul == 0 : # apabila tidak terdapat jin bertipe pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else :
            print(f"Mengerahkan {totaljinPengumpul} jin untuk mengumpulkan bahan")
            print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")
            bahanlist[1][2] = totalpasir # total pasir dimasukkan ke bahanlist
            bahanlist[2][2] = totalbatu # total batu dimasukkan ke bahanlist
            bahanlist[3][2] = totalair # total air dimasukkan ke bahanlist
    elif batch == "BatchBangun": # apabila ingin membangun candi
        tempCandi = [[None for i in range(5)]for j in range(101)]
        for i in range(3,103): 
            if jinlist[i][2] == "Pembangun":# untuk menentukan apakah jin pada jinlist tersebut bertipe pembangun
                totaljinPembangun +=1 # variabel totaljinpembangun akan bertambah 1 bila ditemukan jin bertipe pembangun
                butuhpasir = Build.SearchRandomNumber(1,5,(i+1)*2) # total pasir yang digunakan ditentukan dengan number random generator dari buildinfunction
                butuhbatu = Build.SearchRandomNumber(1,5,(i+3)*11) # total batu yang digunakan ditentukan dengan number random generator dari buildinfunction
                butuhair = Build.SearchRandomNumber(1,5,(i+2)*39)  # total air yang digunakan ditentukan dengan number random generator dari buildinfunction
                if butuhpasir <= totalpasir and butuhair <= totalair and butuhbatu <= totalbatu: # jika bahan-bahan yang dibutuhkan mencukupi (kurang dari persediaan)
                    totalcandi +=1 # maka candi akan terbangun dan totalcandi bertambah 1
                    totalpasir -= butuhpasir # jumlah totalpasir akan berkurang sesuai jumlah pasir yang digunakan
                    totalair -= butuhair # jumlah totalair akan berkurang sesuai jumlah air yang digunakan
                    totalbatu -= butuhbatu # jumlah totalbatu akan berkurang sesuai jumlah batu yang digunakan
                    for j in range(101): 
                        if(tempCandi[j][1] == None): # id candi akan mengisi list temp candi yang kosong
                            tempCandi[j][1] = jinlist[i][0] # untuk id jin yang membangun candi tersebut
                            tempCandi[j][2] = butuhpasir # untuk jumlah pasir yang digunakan untuk membangun candi tersebut
                            tempCandi[j][3] = butuhbatu # untuk jumlah batu yang digunakan untuk membangun candi tersebut
                            tempCandi[j][4] = butuhpasir # untuk jumlah air yang digunakan untuk membangun candi tersebut
                            break
                else :
                    totalcandi = 0 
                    break
        if(totaljinPembangun == 0): # apabila tidak ditemukan jin bertipe pembangun
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

        if totalcandi == 0 : # apabila candi tidak berhasil dibangun karena kekurangan bahan
            print(f"Bangun gagal. Kurang {Build.Diffrence(totalpasir,butuhpasir)} pasir, {Build.Diffrence(totalbatu,butuhbatu)} batu, dan {Build.Diffrence(totalair,butuhair)} air.")
        else :
            print(f"Mengerahkan {totaljinPembangun} jin untuk membangun candi dengan total bahan {butuhpasir} pasir, {butuhbatu} batu, dan {butuhair} air.")
            print(f"Jin berhasil membangun total {totalcandi} candi.")
            print(tempCandi)
            for i in range(totalcandi):
                for j in range(101):
                    if(candilist[j][0] == None):
                        candilist[j][0] = j+1
                        candilist[j][1] = tempCandi[i][1]
                        candilist[j][2] = tempCandi[i][2]
                        candilist[j][3] = tempCandi[i][3]
                        candilist[j][4] = tempCandi[i][4]
                        break
                    else:
                        continue

                
        

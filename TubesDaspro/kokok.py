import BuildInFunction as Build
import sys
def kokokayam (candilist) :
    a=0 # sebagai variabel jumlah candi
    for i in range (1,101): # loop untuk mengitung jumlah candi dari candilist 
        if candilist[i][0] == None: 
            continue # apabila candilist nya berisi [0] program akan terus berjalan
        else :
            a+=1 # apabila pada candilist telah terisi (bukan [0]), maka variabel jumlah candi bertambah 1
    print("Kukuruyuk")
    print("Jumlah Candi = ",a) # memberi output a sebagai variabel total candi
    if a==100: # apabila jumlah candi 100 maka bandung bondowoso menang
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        sys.exit("Program Keluar")# fungsi ini penentu siapa yang menang dan sebagai akhir dari permainan sehingga program akan keluar setelah ini
    else : # apabila jumlah candi kurang dari 100 roro jonggrang menang
        print("\n*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")
        sys.exit("Program Keluar") # fungsi ini penentu siapa yang menang dan sebagai akhir dari permainan sehingga program akan keluar setelah ini

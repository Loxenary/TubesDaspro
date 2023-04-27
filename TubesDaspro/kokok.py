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
    if a==100: # apabila jumlah candi 100 maka bandung bondowoso menjadi pemenangnya
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        sys.exit("Program Keluar") # fungsi kokokayam ini adalah sebagai akhir permainan dan program akan keluar setelahnya
    else : # apabila jumlah candi kurang dari 100 maka roro jonggrang menjadi pemenangnya
        print("\n*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")
        sys.exit("Program Keluar") # fungsi kokokayam ini adalah sebagai akhir permainan dan program akan keluar setelahnya

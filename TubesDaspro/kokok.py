import BuildInFunction as Build
import sys
def kokokayam (candilist) :
    a=0
    for i in range (1,101):
        if candilist[i][0] == None:
            continue
        else :
            a+=1
    print("Kukuruyuk")
    print("Jumlah Candi = ",a)
    if a==100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        sys.exit("Program Keluar")
    else :
        print("\n*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")
        sys.exit("Program Keluar")


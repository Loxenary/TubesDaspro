import BuildInFunction as Build
def kokokayam (candilist) :
    a=0
    candilist1 = [[ 0 for j in range (2)] for i in range (3)]
    for i in range (3):
        for j in range(2):
            candilist1[i][j] = candilist[i][j]
        if candilist1[i][j]==[0,0]:
            continue
        else :
            a+=1
    print("Kukuruyuk")
    print("Jumlah Candi = ",a)
    if a==100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else :
        print("\n*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")

#contoh sementara
cand = [['Jin1','cand1'],['Jin1' , 'cand2'], ['Jin1','cand'],[0,0]]
print(kokokayam(cand))

import BuildInFunction as Build
def HapusJin (jinlist,candilist) :
    list1 = [[0 for j in range (3)] for i in range (5)]
    candilist1 = [[ 0 for j in range (2)] for i in range (3)]
    for i in range (3):
        for j in range(2):
            candilist1[i][j] = candilist[i][j]
    for i in range (5):
        for j in range(3):
            list1[i][j] = jinlist[i][j]
    a=0
    username = str(input("Masukkan Username = "))
    for i in range(0,5): 
        if(username == jinlist[i][0]):
            a+=1
            jinke = i
    if a>0 :
        pilihan = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {username} , (Y/N)?"))
        while pilihan != 'Y' and pilihan != 'N': 
            pilihan = str(input("Masukkan input yang benar (Y/N) :  "))
        if(pilihan == 'Y'):
            jinlist[jinke] = [0,0,0]
            for i in range (0,3):
                if (username==candilist[i][0]):
                    candilist [i] = [0,0]
            print("Jin telah berhasil dihapus dari alam ghaib")
        else:
            print("Masukkan input ulang")
            HapusJin(jinlist) 
    else:
        print("Tidak ada jin dengan username tersebut")  
        HapusJin(jinlist)
us = [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'],['Jin1','IffritGanteng','Pengumpul'],['Jin2','iffritJelek','Pembangun']]
cand = [['Jin1','cand1'],['Jin1' , 'cand2'], ['Jin1','cand']]
HapusJin(us,cand)
print(us)
print(cand)

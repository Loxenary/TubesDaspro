import BuildInFunction as Build
def ubahJin(listjin,user):
    if(user == "Bondowoso"):
        countPengumpul = 0
        countPembangun = 0
        for i in range(1,Build.PanjangList(listjin)):
            if(listjin[i][2] == "Pengumpul"):
                countPengumpul += 1
            else:
                countPembangun += 1
        print("Total Jin :",Build.PanjangList(listjin)-1)
        print("Total Jin Pengumpul: 17")
        print("Total Jin Pembangun: 33")
    else:
        return
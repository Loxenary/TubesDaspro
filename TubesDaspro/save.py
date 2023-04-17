import os
import TempData as Data
def save(user_list,candi_list,bahan_list):
    folder = input('Masukkan nama folder:')
    if os.path.exists('/save')==False:
        os.makedirs('/save')
        os.makedirs(f'/save/{folder}')
    elif os.path.exists(f'/save/{folder}')==True:
        CsvSave(folder,user_list,candi_list,bahan_list)
    else:
        os.makedirs(f'/save/{folder}')
        CsvSave(folder,user_list,candi_list,bahan_list)

def CsvSave(folder,user_list,candi_list,bahan_list):
    with open(f'/save/{folder}/user.csv','w') as users:
        for j in range(103):
            for i in range(3):
                if user_list[j][i] == None:
                    continue
                else:
                    users.write("%s,"%user_list[j][i])
    with open(f'/save/{folder}/candi.csv','w') as candi:
        for j in range(101):
            for i in range(5):
                if candi_list[j][i] == None:
                    continue
                else:
                    candi.write("%s,"%candi_list[j][i])
    with open(f'/save/{folder}/bahan.csv','w') as bahan:
        for j in range(4):
            for i in range(3):
                bahan.write("%s,"%bahan_list[j][i])

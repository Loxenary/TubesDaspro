import os
from JinPembangun import list_candi
def save():
    folder = input('Masukkan nama folder:')
    if os.path.exists('/save')==False:
        os.makedirs('/save')
        os.makedirs(f'/save/{folder}')
    elif os.path.exists(f'/save/{folder}')==True:
        with open(f'/save/{folder}/candi.csv','w') as file:
            for j in range(1001):
                for i in range(4):
                    if list_candi[j][i]==0:
                        continue
                    else:
                        file.write("%s,"%list_candi[j][i])
    else:
        os.makedirs(f'/save/{folder}')
        with open(f'/save/{folder}/candi.csv','w') as file:
            for j in range(1001):
                for i in range(4):
                    if list_candi[j][i]==0:
                        continue
                    else:
                        file.write("%s,"%list_candi[j][i])

save()

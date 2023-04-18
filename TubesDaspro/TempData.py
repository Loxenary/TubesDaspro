import Load as load
LoginState = False
nama_user = ""
role_user = ""

users = [[None for j in range(3)]for i in range(103)]
bahan = [[None for j in range(3)]for i in range(4)]
candi = [[None for j in range(5)]for i in range(101)]

def perhitungan(csvFile,list):
    i = 0
    j = 0
    word = ""
    for char in csvFile:
        if(char == '\n'):
            if(word != ''):
                list[i][j] = word
            i += 1
            j = 0
            word = ''
        elif char != ";":
            word += char
        else:
            list[i][j] = word
            word = ''
            j += 1
with open(f'{load.folder}/user.csv') as user_file:
    user_reader = user_file.read()
    perhitungan(user_reader,users)
with open(f'{load.folder}/candi.csv') as candi_file:
    candi_reader = candi_file.read()
    perhitungan(candi_reader,candi)
with open(f'{load.folder}/bahan_bangunan.csv') as bahan_file:
    bahan_reader = bahan_file.read()
    perhitungan(bahan_reader,bahan)



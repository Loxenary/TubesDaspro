import Load as load # Module load pada kasus ini untuk mendapatkan directory folder yang dibutuhkan 
LoginState = False # variable yang berisi keadaan user saat ini (sudah login atau belum), variable ini akan terus berubah ubah seiring berjalannya program
nama_user = "" # variable ini berisi nama dari user saat ini
role_user = "" # variable ini berisi role dari user saat ini
current_csv_path = load.folder

users = [[None for j in range(3)]for i in range(103)] # list users adalah matriks dengan panjang baris 103 dan kolom 3 yang isinya adalah username, password, dan role dari users
bahan = [[None for j in range(3)]for i in range(4)] # list bahan adalah matriks dengan panjang baris 4 dan kolom 3 yang isinya adalah nama bahan, deskripsi, dan jumlah bahan saat ini
candi = [[None for j in range(5)]for i in range(101)] # list candi adalah matriks dengan panjang baris 101 dan kolom 5 yang isinya adalah id candi, pembuat, jumlah pasir, batu, dan air yang dibutuhkan 

# function perhitungan hanya digunakan untuk memasukkan isi dari csv file ke temporary list
def perhitungan(csvFile,list): # parameter csvfile adalah file csv yang akan dimasukkan ke temporary lsit (parameter list)
    i = 0 # i adalah indeks yang menyatakan baris dari matrix list
    j = 0 # j adalah indeks  yang menyatakan kolom dari matrix list
    word = "" # variable yang menyimpan data sementara 
    
    # Algoritma
    '''
    Diawali dengan membaca tiap huruf dalam csvFile, jika huruf tersebut bukan ";", maka ditambahkan ke variable word, jika terdapat ";", word di assign ke dalam matriks, word juga akan di reset dan j nya ditambah u=
    untuk berganti kolom. jika huruf yang dibaca adalah enter, jika word nya tidak kosong, maka word akan di assign ke dalam matriks, i akan ditambah untuk berganti baris 
    dan j akan di assign dengan nilai 0 untuk me-reset kolom matriks
    '''
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

with open(f'{current_csv_path}/user.csv') as user_file: # membuka user.csv dan assign ke user_file
    user_reader = user_file.read() # lalu user_file di read dan me-assignnya ke user_reader
    perhitungan(user_reader,users) # lalu function perhitungan dijalankan untuk memasukkan nya ke list users
    
with open(f'{current_csv_path}/candi.csv') as candi_file: # membuka candi.csv dan assign ke candi_file
    candi_reader = candi_file.read() # lalu candi_file di read dan me-assignnya ke candi_reader
    perhitungan(candi_reader,candi) # lalu function perhitungan dijalan kan untu me-assign nya ke list candi

with open(f'{current_csv_path}/bahan_bangunan.csv') as bahan_file: # membuka bahan_bangunan.csv dan assign ke bahan_file
    bahan_reader = bahan_file.read() # lalu user_file di read dan me-assignnya ke bahan_reader
    perhitungan(bahan_reader,bahan) # lalu function perhitungan dijalankan untuk me-assign nya ke list bahan



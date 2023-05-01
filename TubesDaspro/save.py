import os
import TempData as Data
def save():
    path = Data.current_csv_path
    parentFolder = "save"
    userFile_read = open(f'{path}/user.csv','rb')
    candiFile_read = open(f'{path}/candi.csv','rb')
    bahanFile_read = open(f'{path}/bahan_bangunan.csv','rb')
    #Pembukaan 3 file csv diatas dan dimasukkan ke 3 accesible variabel berbeda

    folder_name = str(input("Masukkan nama folder: "))#Penamaan folder yang ingin kita pakai untuk menyimpan data
    folder_path = os.path.join(parentFolder,folder_name) 
    if(os.path.exists(parentFolder) == False): # parent save/ belum ada
        os.makedirs(folder_path)#Pembuatan path parent dan folder kita di dalamnya    
        print("\nSaving...")
        print(f"Membuat folder {parentFolder}")
        print(f"Membuat folder {folder_path}")
        print(f"\nBerhasil menyimpan data di folder {folder_path}")

    else: # parent save/ sudah ada
        if(os.path.exists(folder_path) == True): # folder sudah ada
            print("\nSaving...")
            print(f"\nBerhasil menyimpan data di folder {folder_path}!")
        else: # parent save sudah ada tapi folder belum ada
            os.makedirs(folder_path,exist_ok=True)#Pembuatan folder kita didalam parent folder
            print("\nSaving...")
            print(f"\nBerhasil menyimpan data di folder {folder_path}!")

    userFile_write = open(f'{folder_path}/user.csv',"wb")
    userFile_write.write(userFile_read.read())
    candiFile_write = open(f'{folder_path}/candi.csv',"wb")
    candiFile_write.write(candiFile_read.read())
    bahanFile_write = open(f'{folder_path}/bahan_bangunan.csv',"wb")
    bahanFile_write.write(bahanFile_read.read())
    #Rewriting data baru kedalam folder yang baru dibentuk dalam bentuk 3 file csv yang berbeda
    userFile_write.close()  
    candiFile_write.close()
    bahanFile_write.close()
    #Setelah selesai penulisan file maka file file tersebut ditutup kembali agar progress terupdate di komputer
    override(folder_path)

def override(path):
    users = Data.users
    user = open(f'{path}/user.csv','w')
    writeFile(user,users,103,3)
    candi = Data.candi
    candif = open(f'{path}/candi.csv','w')
    writeFile(candif,candi,101,5)
    bahan = Data.bahan
    bahanf = open(f'{path}/bahan_bangunan.csv',"w")
    writeFile(bahanf,bahan,4,3)
    
def writeFile(file,list,PanjangBaris,PanjangKolom):#Cara penulisan yang readable tiap file difolder tersebut dengan fungsi ini
    for i in range(PanjangBaris):
        if(list[i][0] != None):
            for j in range(PanjangKolom):
                file.write(str(list[i][j]))
                if(j != PanjangKolom-1):
                    file.write(";")
            file.write("\n")
        else:
            file.write("\n")
        

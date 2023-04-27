import os
import TempData as Data
def save():
    path = Data.current_csv_path
    parentFolder = "save"
    userFile_read = open(f'{path}/user.csv','rb')
    candiFile_read = open(f'{path}/candi.csv','rb')
    bahanFile_read = open(f'{path}/bahan_bangunan.csv','rb')
    folder_name = str(input("Masukkan nama folder: "))
    folder_path = os.path.join(parentFolder,folder_name)

    userFile_write = open(f'{folder_path}/user.csv',"wb")
    userFile_write.write(userFile_read.read())
    candiFile_write = open(f'{folder_path}/candi.csv',"wb")
    candiFile_write.write(candiFile_read.read())
    bahanFile_write = open(f'{folder_path}/bahan_bangunan.csv',"wb")
    bahanFile_write.write(bahanFile_read.read())    
    if(os.path.exists("save") == False): # parent save/ belum ada
        os.makedirs(folder_path)
        print("\nSaving...")
        print(f"Membuat folder {parentFolder}")
        print(f"Membuat folder {folder_path}")
        print(f"\nBerhasil menyimpan data di folder {folder_path}")

    else: # parent save/ sudah ada
        if(os.path.exists(folder_name) == True): # folder sudah ada
            print("\nSaving...")
            print(f"\nBerhasil menyimpan data di folder {folder_path}!")
        else: # parent save sudah ada tapi folder belum ada
            os.makedirs(folder_path,exist_ok=True)
            print("\nSaving...")
            print(f"\nBerhasil menyimpan data di folder {folder_path}!")
            userFile_write.close()

    candiFile_write.close()
    bahanFile_write.close()
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
    
def writeFile(file,list,PanjangBaris,PanjangKolom):
    for i in range(PanjangBaris):
        if(list[i][0] != None):
            for j in range(PanjangKolom):
                file.write(str(list[i][j]))
                if(j != PanjangKolom-1):
                    file.write(";")
            file.write("\n")
        else:
            file.write("\n")
        
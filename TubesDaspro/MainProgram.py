import BuildInFunction as Build
import csv 
import Load
import DataBase as data

def cekLoginState(function):
    if(LoginState == True):
        function
    else:
        print("User Harus Login Terlebih dahulu")
        print('Ketik "Login" pada pilihan untuk login terlebih dahulu')
        pilihanUser()

def pilihanUser():
    pilihan = input("Masukkan Pilihan Anda: ")
    match pilihan:
        case "Login":
            data.login.UserLogin(LoginState)
        case "Logout":
            cekLoginState(data.logout.UserLogout(LoginState))
        case "UbahJin":
            cekLoginState(data.ubahjin.FuncUbahJin())

with open('user.csv') as user_file:
    user_reader = csv.reader(user_file, delimiter=";")
    users = []
    for row in user_reader:
        users = Build.TambahList(users,row)
with open('candi.csv') as candi_file:
    candi_reader = csv.reader(candi_file, delimiter=";")
    candi = []
    for row in candi_reader:
        candi = Build.TambahList(candi_file,row)
with open('bahan_bangunan.csv') as bahan_file:
    bahan_reader = csv.reader(bahan_file,delimiter=";")
    bahan = []
    for row in bahan_reader:
        bahan = Build.TambahList(bahan_file,row)

LoginState = False
pilihanUser()



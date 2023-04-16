import Login as Login
import Logout as Logout
import Load 
import SummonJin as SummonJin
import HilangkanJin as HilangkanJin
import UbahJin as UbahJin
import JinPembangun as JinPembangun
import MainProgram as main
import TempData as data

def cekLoginState(function):
    if(data.LoginState == True):
        function
    else:
        print("User Harus Login Terlebih dahulu")
        print('Ketik "Login" pada pilihan untuk login terlebih dahulu')

def pilihanUser(LoginState,nama_user):
    print("Masukkan Pilihan Anda: ")
    print(nama_user)
    pilihan = input(">>> ").upper()
    if(pilihan == "LOGIN"):
        Login.UserLogin(data.users,LoginState,nama_user)
        pilihanUser(data.LoginState,data.nama_user)
    elif(pilihan == "LOGOUT"):
        cekLoginState(Logout.UserLogout(LoginState))
        pilihanUser(data.LoginState,data.nama_user)
    elif(pilihan == "SUMMONJIN"):
        if(nama_user == "Bondowoso"):
            cekLoginState(SummonJin.SummonJin(data.users))
            pilihanUser(data.LoginState,data.nama_user)
        else:
            print("Hanya Bondowoso yang dapat Mengakses fitur SummonJin")
            pilihanUser(data.LoginState,data.nama_user)

    elif(pilihan == "UBAHJIN" ):
        if(nama_user == "Bondowoso"):
            cekLoginState(UbahJin.FuncUbahJin(data.users))
        else:
            print("Hanya Bondowoso yang dapat Mengakses fitur UbahJin")
    elif(pilihan == "USER"):
        print(data.users)
    elif(pilihan == "CANDI"):
        print(data.candi)
    else:
        print("Stuuupid")

pilihanUser(data.LoginState,data.nama_user)



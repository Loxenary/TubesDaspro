import Login as Login
import Logout as Logout
import BuildInFunction as Build
import SummonJin as SummonJin
import Hapusjin as Hapusjin
import UbahJin as UbahJin
import TempData as data
import JinPembangun as pembangun
import JinPengumpul as pengumpul
import batch as Batch
import HancurkanCandi as CandiHancur
import AmbilLaporanJin as laporanJin
import AmbilLaporanCandi as laporanCandi
import kokok as AyamBerkokok
import save as Saving
import Help as helpPlayer
import exit as ExitGame
import os 
import time

def cekLoginState():
    print("e")
    os.system('cls')
    time.sleep(0.25)
    if(data.LoginState == True):
        return True
    else:
        print("User Harus Login Terlebih dahulu")
        print('Ketik "login" pada pilihan untuk login terlebih dahulu\n')
        return False
def cekAksesUser(user_role,functionName):
    if(data.role_user == user_role):
        return True
    else:
        if(user_role == "bandung_bondowoso" or user_role == "roro_jonggrang"):
            print(f"Hanya {user_role} yang dapat Mengakses fitur {functionName}")
            return False
        else:
            print(f"Hanya Jin dengan role {user_role} yang dapat Mengakses fitur {functionName}")
            return False
def pilihanUser(LoginState,role_user):
    print("\nMasukkan Pilihan Anda: ")
    pilihan = str(input(">>> "))
    os.system("cls")
    if(pilihan == "login" and LoginState == False):
        Login.UserLogin(data.users)        
    elif(pilihan == "login" and LoginState == True):
        print('Anda sudah Login, pilih command "logout"\nuntuk ganti akun')
    elif(pilihan == "logout" and cekLoginState() == True):
        Logout.UserLogout()
    elif(pilihan == "summonjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan)):
            SummonJin.SummonJin(data.users) 
    elif(pilihan == "ubahjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan) == True):
            UbahJin.FuncUbahJin(data.users) 
    elif(pilihan == "hapusjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan)):
            Hapusjin.HapusJin(data.users,data.candi)
    elif(pilihan == "kumpul" and cekLoginState() == True):
        if(cekAksesUser("Pengumpul",pilihan)):
            pengumpul.JinPengumpul(data.bahan)
    elif(pilihan == "bangun" and cekLoginState() == True):
        if(cekAksesUser("Pembangun",pilihan)):
            pembangun.bangun(data.candi,data.bahan,data.nama_user)
    elif(pilihan == "batchkumpul" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan)):
            Batch.batch("BatchKumpul",data.users,data.candi,data.bahan)
    elif(pilihan == "batchbangun" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan)):
            Batch.batch("BatchBangun",data.users,data.candi,data.bahan)
    elif(pilihan == "laporanjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan) == True):
            laporanJin.AmbilLaporanJin(data.users,data.candi,data.bahan) 
    elif(pilihan == "laporancandi" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan) == True):
             laporanCandi.laporancandi(data.candi)
    elif(pilihan == "hancurkancandi" and cekLoginState() == True):
        if(cekAksesUser("roro_jonggrang",pilihan)):
            CandiHancur.HancurkanCandi(data.candi)
    elif(pilihan == "ayamberkokok" and cekLoginState() == True):
        if(cekAksesUser("roro_jonggrang",pilihan)):
            AyamBerkokok.kokokayam(data.candi)   
    elif(pilihan == "save" and cekLoginState() == True):
        Saving.save(data.users,data.candi,data.bahan)
    elif(pilihan == "help"):
        helpPlayer.Help(LoginState,role_user)
    elif(pilihan == "exit"):
        ExitGame.exit()
    elif(pilihan == "P"):
        print(data.users)
    elif(pilihan == "C"):
        print(data.candi)
    elif(pilihan == "B"):
        print(data.bahan)
    else:
        print("pilihan tidak tersedia")
    pilihanUser(data.LoginState,data.role_user)

pilihanUser(data.LoginState,data.role_user)

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

def cekLoginState(function):
    if(data.LoginState == True):
        function
    else:
        print("User Harus Login Terlebih dahulu")
        print('Ketik "Login" pada pilihan untuk login terlebih dahulu')
def cekAksesUser(function,user_role,functionName):
    if(data.role_user == user_role):
        function
    else:
        if(user_role == "bandung_bondowoso" or user_role == "roro_jonggrang"):
            print(f"Hanya {user_role} yang dapat Mengakses fitur {functionName}")
        else:
            print(f"Hanya Jin dengan role {user_role} yang dapat Mengakses fitur {functionName}")

def pilihanUser(LoginState,role_user):
    helpPlayer.Help(data.LoginState,data.role_user)
    print("Masukkan Pilihan Anda: ")
    pilihan = str(input(">>> "))
    pilihan = Build.uppercase(pilihan)
    if(pilihan == "LOGIN"):
        Login.UserLogin(data.users,LoginState,role_user)        
    elif(pilihan == "LOGOUT"):
        cekLoginState(Logout.UserLogout(LoginState))
    elif(pilihan == "SUMMONJIN"):
        cekLoginState(cekAksesUser(SummonJin.SummonJin(data.users),"bandung_bondowoso","SummonJin"))  
    elif(pilihan == "UBAHJIN" ):
        cekLoginState(cekAksesUser(UbahJin.FuncUbahJin(data.users),"bandung_bondowoso","UbahJin"))    
    elif(pilihan == "HAPUSJIN"):
        cekLoginState(cekAksesUser(Hapusjin.HapusJin(data.users),"bandung_bondowoso","HapusJin"))
    elif(pilihan == "JINPENGUMPUL"):
        cekLoginState(cekAksesUser(pengumpul.JinPengumpul(data.bahan),"Pengumpul","JinPengumpul"))
    elif(pilihan == "JINPEMBANGUN"):
        cekLoginState(cekAksesUser(pembangun.bangun(data.candi,data.bahan,data.nama_user),"Pembangun","JinPembangun"))
    elif(pilihan == "BATCHBANGUN"):
        cekLoginState(cekAksesUser(Batch.batch("BatchBangun",data.users,data.candi,data.bahan),"bandung_bondowoso","BatchBangun"))
    elif(pilihan == "BATCHKUMPUL"):
        cekLoginState(cekAksesUser(Batch.batch("BatchKumpul",data.users,data.candi,data.bahan),"bandung_bondowoso","BatchKumpul"))
    elif(pilihan == "HANCURKANCANDI"):
        cekLoginState(cekAksesUser(CandiHancur.HancurkanCandi(data.candi),"roro_jonggrang","HancurkanCandi"))
    elif(pilihan == "AMBILLAPORANJIN"):
        cekLoginState(cekAksesUser(laporanJin.AmbilLaporanJin(data.users),"bandung_bondowoso","AmbilLaporanJin"))
    elif(pilihan == "AMBILLAPORANCANDI"):
        cekLoginState(cekAksesUser(laporanCandi.laporancandi(data.candi),"bandung_bondowoso","AmbilLaporanCandi"))
    elif(pilihan == "AYAMBERKOKOK"):
        cekLoginState(cekAksesUser(AyamBerkokok.kokokayam(data.candi),"roro_jonggrang","AyamBerkokok"))
    elif(pilihan == "SAVE"):
        cekLoginState(Saving.save(data.users,data.candi,data.bahan))
    elif(pilihan == "EXIT"):
        ExitGame.exit()
    else:
        print("pilihan tidak tersedia")
    pilihanUser(data.LoginState,data.role_user)

pilihanUser(data.LoginState,data.role_user)



# import semua module untuk dipanggil fungsinya
import Login as Login
import Logout as Logout
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
# import os untuk clear command sehingga terlihat lebih bersih
import os 
# import time untuk memberikan jeda sehingga terkesan lebih pas
import time
def cekLoginState(): # berfungsi untuk mengecek keadaan user apakah sudah login atau belum, jika sudah akan return True jika belum akan return false
    os.system('cls')
    time.sleep(0.25)
    if(data.LoginState == True): # data.LoginState adalah variable yang diubah ubah berdasarkan keadaan login user saat itu
        return True
    else:
        print("User Harus Login Terlebih dahulu")
        print('Ketik "login" pada pilihan untuk login terlebih dahulu\n')
        return False

# cek akses user berfungsi untuk men-check apakah user saat itu dapat mengakses fitur tertentu pada sistem, akan me-return true jika role nya benar, dan return false jika tidak benar
def cekAksesUser(user_role,functionName): # user_role adalah role user apa yang boleh mengakses fitur tersebut, functionName adalah nama fitur atau fungsi yang dimaksud
    if(data.role_user == user_role): # data.role_user adalah role user saat itu, misal: jika login sebagai Bondowoso maka role nya adalah bandung_bondowoso 
        return True
    else: # jika role tidak sesuai
        if(user_role == "bandung_bondowoso" or user_role == "roro_jonggrang"): 
            print(f"Hanya {user_role} yang dapat Mengakses fitur {functionName}")
            return False
        else:
            print(f"Hanya Jin dengan role {user_role} yang dapat Mengakses fitur {functionName}")
            return False

# pilihanUser dibuat sebagai function agar dapat terus dipanggil nantinya hingga permainan berakhir 
def pilihanUser(LoginState,role_user): # menerima LoginState yaitu keadaan login user saat itu dan role dari user saat itu
    print("\nMasukkan Pilihan Anda: ") 
    pilihan = str(input(">>> ")) # menerima input dari user

    os.system("cls") 
    if(pilihan == "login" and LoginState == False): # fungsi login hanya dapat dipanggil ketika keadaan user sudah logout, dan dapat diakses siapa saja
        Login.UserLogin(data.users)

    elif(pilihan == "login" and LoginState == True): # jika fungsi login dipanggil saat keadaan user sudah login
        print('Anda sudah Login, pilih command "logout"\nuntuk ganti akun')

    elif(pilihan == "logout" and cekLoginState() == True): # fungsi logout hanya dapat dipanggil saat keadaan user sudah login
        Logout.UserLogout()

    # fungsi berikut hanya dapat dipanggil ketika user sudah login dan role user adalah bandung_bondowoso
    elif(pilihan == "summonjin" and cekLoginState() == True): 
        if(cekAksesUser("bandung_bondowoso",pilihan)): # role yang dibutuhkan adalah "bandung_bondowoso" dan nama function nya adalah pilihan karena ketika user memasukkan input, input tersebut pasti akan sama dengan function yang dimaksud 
            SummonJin.SummonJin(data.users) 

    elif(pilihan == "ubahjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan) == True): 
            UbahJin.FuncUbahJin(data.users) 

    elif(pilihan == "hapusjin" and cekLoginState() == True):
        if(cekAksesUser("bandung_bondowoso",pilihan)):
            Hapusjin.HapusJin(data.users,data.candi)

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

    # fungsi kumpul hanya dapat diakses jika user sudah login dan user_role adalah Pengumpul         
    elif(pilihan == "kumpul" and cekLoginState() == True):
        if(cekAksesUser("Pengumpul",pilihan)):
            pengumpul.JinPengumpul(data.bahan)
    # fungsi bangun hanya dapat diakses jika user sudah login dan user_role adalah Pembangun
    elif(pilihan == "bangun" and cekLoginState() == True):
        if(cekAksesUser("Pembangun",pilihan)):
            pembangun.bangun(data.candi,data.bahan,data.nama_user)

    # fungsi berikut hanya dapat diakses jika user sudah login dan user_role adalah roro_jonggrang
    elif(pilihan == "hancurkancandi" and cekLoginState() == True):
        if(cekAksesUser("roro_jonggrang",pilihan)):
            CandiHancur.HancurkanCandi(data.candi)
    elif(pilihan == "ayamberkokok" and cekLoginState() == True):
        if(cekAksesUser("roro_jonggrang",pilihan)):
            AyamBerkokok.kokokayam(data.candi)
    # fungsi save dapat dipanggil oleh siapa saja dengan syarat user sudah login
    elif(pilihan == "save" and cekLoginState() == True):
        Saving.save()
    # fungsi berikut dapat dipanggil oelh siapa saja tanpa syarat
    elif(pilihan == "help"):
        helpPlayer.Help(LoginState,role_user)
    elif(pilihan == "exit"):
        ExitGame.exit()
    else: # jika user memasukkan input selain fungsi fungsi diatas
        print("pilihan tidak tersedia")
        print('Ketik "help" untuk melihat command yang dapat dilihat')
    pilihanUser(data.LoginState,data.role_user) # untuk melakukan loop tiap kali user selesai menggunakan suatu fitur

pilihanUser(data.LoginState,data.role_user) # digunakan untuk memulai permainan dengan input user

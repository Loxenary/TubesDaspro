import BuildInFunction as Build
import TempData as data
<<<<<<< HEAD
def UserLogin(userlist): #userlist adalah parameter yang akan di assign dengan list users
    
    # input-field
    username = str(input("username: ")) # username (dari file user.csv)
    password = str(input("password: ")) # password (dari file)

    # dummy variable
    hasil1 = False # variable dummy untuk mengecek apakah username benar
    hasil2 = False # variable dummy untuk mengecek apakah password benar

    # Username-Password Validating
=======
def UserLogin(userlist):
    username = str(input("username: "))
    password = str(input("password: "))
    hasil1 = False
    hasil2 = False
>>>>>>> parent of 3ce5b4a (Update lagi)
    for i in range(1,103):
        if(username == userlist[i][0]): # userlist[i][0] mengacu pada kolom username pada user.csv
                hasil1 = True 
                if(password == userlist[i][1]): # jika username benar, akan divalidasi passwordnya, userlist[i][1] mengacu pada kolom passwrod pada user.csv
                    hasil2 = True 
                    role_user = userlist[i][2] # jika username dan password benar, role_user akan di assign dengan role pada kolom role di user.csv
                    break # break digunakan karena validasi hanya dilakukan sekali dan karena username bersifat unique, maka hanya diperlukan sekali validasi
                else:
                    hasil2 = False
                    break 
        else:
            continue # selama username belum ditemukan, akan terus di loop hingga ditemukan atau tidak ditemukan sama sekali.

    if(hasil1 == True and hasil2 == True): # jika username dan password benar 
        print("") # hanya untuk memberikan enter pada terminal
        print(f'''Selamat datang, {username}! 
        \rMasukkan command "help" untuk daftar
        \rcommand yang dapat kamu panggil.''') 
        data.LoginState = True # data.Loginstate digunakan pada file MainProgram.py untuk memvalidasi apakah user sudah login atau belum
        data.role_user = role_user # data.role_user merupakan role dari user yang sudah login saat ini
        data.nama_user = username # data.nama_user merupakan username dari user yang sudah login saat ini

    elif(hasil1 == False): # jika username salah
        print("\nUsername tidak terdaftar\n")
        UserLogin(userlist) # dilakukan looping agar user dapat meng-input username dan password kembali

    else: # jika username benar tapi password salah
        print("\npassword salah!\n")
        UserLogin(userlist) # dilakukan looping agar user dapat meng-input username dan password kembali


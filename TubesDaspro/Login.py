import BuildInFunction as Build
import TempData as data
def UserLogin(userlist):
    username = str(input("username: ")) # username (dari file user.csv)
    password = str(input("password: ")) # password (dari file)
    hasil1 = False
    hasil2 = False
    for i in range(1,103):
        if(username == userlist[i][0]):
                hasil1 = True
                if(password == userlist[i][1]):
                    hasil2 = True
                    role_user = userlist[i][2]
                    break
                else:
                    hasil2 = False
                    break
        else:
            continue
    if(hasil1 == True and hasil2 == True):
        print("")
        print(f'''Selamat datang, {username}!
        \rMasukkan command "help" untuk daftar
        \rcommand yang dapat kamu panggil.''')
        #return help(command)
        data.LoginState = True
        data.role_user = role_user
        data.nama_user = username
    elif(hasil1 == False):
        print("\nUsername tidak terdaftar\n")
        UserLogin(userlist)
    else:
        print("\npassword salah!\n")
        
        UserLogin(userlist)


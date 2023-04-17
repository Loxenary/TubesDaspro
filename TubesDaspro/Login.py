import BuildInFunction as Build
import TempData as data
def UserLogin(userlist,LoginState,user):
    print(userlist)
    username = str(input("username: "))
    password = str(input("password: "))
    hasil1 = False
    hasil2 = False
    for i in range(1,102):
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
        print(f'''    Selamat datang, {username}!
        \rMasukkan command "help" untuk daftar
        \rcommand yang dapat kamu panggil.
        \r''')
        LoginState = True
        user = username
        #return help(command)
        data.LoginState = True
        data.role_user = role_user
        data.nama_user = username
    elif(hasil1 == False):
        print("\nUsername tidak terdaftar")
        UserLogin(userlist,LoginState,user)
    else:
        print("\npassword salah!")
        
        UserLogin(userlist,LoginState,user)


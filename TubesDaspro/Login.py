import BuildInFunction as Build

def UserLogin(userlist,LoginState):
    LoginState = True
    username = str(input("username: "))
    password = str(input("password: "))
    hasil1 = False
    hasil2 = False
    for i in range(1,Build.PanjangList(userlist)):
        if(username == userlist[i][0]):
                hasil1 = True
                if(password == userlist[i][1]):
                    hasil2 = True
                else:
                    hasil2 = False
        else:
            continue
    if(hasil1 == True and hasil2 == True):
        print("")
        command = str(input(f'''    Selamat datang, {username}!
        \rMasukkan command "help" untuk daftar
        \rcommand yang dapat kamu panggil.
        \r'''))

        
        #return help(command)
    elif(hasil1 == False):
        print("\nUsername tidak terdaftar")
        UserLogin(userlist,LoginState)
    else:
        print("\npassword salah!")
        
        UserLogin(userlist,LoginState)

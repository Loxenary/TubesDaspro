import BuildInFunction as Build

def Help(LoginState,Role):
    if LoginState == False :
        print(f"""
        \r>>> help
        \r=========== HELP ===========
        \r1. login
            \r  Untuk masuk menggunakan akun
        \r2. load
            \r  Untuk memuat file eksternal ke dalam permainan
        \r# ...dan seterusnya""")
    else:
        if Role == "Bandung Bondowoso":
            print(f"""
            \r# Role: Bandung Bondowoso
            \r>>> help
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. summonjin
                \r  Untuk memanggil jin
            \r# ...dan seterusnya""")
        
        elif Role == "Roro Jonggrang" :
            print(f"""
            \r# Role: Roro Jonggrang
            \r>>> help
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. hancurkancandi
                \r  Untuk menghancurkan candi yang tersedia
            \r# ...dan seterusnya""")
        elif Role == "Jin Pengumpul":
            print(f"""
            \r# Role: Jin Pengumpul
            \r>>> help
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. kumpul
                \r  Untuk mengumpulkan resource candi
            \r# ...dan seterusnya""")
        else:
            print(f"""
            \r# Role: Jin Pembangun
            \r>>> help
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. bangun
                \r  Untuk membangun candi
            \r# ...dan seterusnya""")
            
LoginState = True
Role = "Bandung Bondowoso"
Help(LoginState,Role)
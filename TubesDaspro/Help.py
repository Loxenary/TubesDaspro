import BuildInFunction as Build

def Help(LoginState,Role):
    if LoginState == False :
        print(f"""
        \r>>> help
        \r=========== HELP ===========
        \r1. login
            \r  Untuk masuk menggunakan akun
        \r2. exit
            \r Untuk keluar dari program dan kembali ke terminal
        \r============================""")
    else:
        if Role == "bandung_bondowoso":
            print(f"""
            \r=========== HELP ===========
            \r1. Logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. SummonJin
                \r  Untuk memanggil jin
            \r3. HilangkanJin
                \r Untuk menghilangkan jin
            \r4. UbahJin
                \r Untuk Mengubah Role Jin dari Pengumpul ke Pembangun dan sebaliknya
            \r5. BatchKumpul
                \r Untuk melakukan pengumpulan bahan dengan banyak jin
            \r6. BatchBangun
                \r Untuk melakukan pembangunan jin dengan banyak jin 
            \r7. AmbilLaporanJin
                \r Untuk mengambil Laporan dari seluruh Jin yang sudah disummon
            \r8. AmbilLaporanCandi
                \r Untuk mengambil keseluruhan data dari candi yang sudah dibangun
            \r9. Save
                \r Untuk saving data temporary ke csv file
            \r10. Exit
                \r Untuk exit dari Permainan
            \r============================""")
        elif Role == "roro_jonggrang" :
            print(f"""
            \r=========== HELP ===========
            \r1. Logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. HancurkanCandi
                \r  Untuk menghancurkan candi yang tersedia
            \r3. AyamBerkokok
                \r Untuk menyelesaikan permainan dengan memalsukan pagi hari """)
        elif Role == "Pengumpul":
            print(f"""
            \r=========== HELP ===========
            \r1. Logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. JinPengumpul
                \r  Untuk mengumpulkan resource candi
            \r3. Save
                \r Untuk saving data temporary ke csv file
            \r4. Exit
                \r Untuk exit dari Permainan
            \r============================""")
        else:
            print(f"""
            \r# Role: Jin Pembangun
            \r>>> help
            \r=========== HELP ===========
            \r1. Logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. JinPembangun
            \r3. Save
                \r Untuk saving data temporary ke csv file
            \r4. Exit
                \r Untuk exit dari Permainan
            \r============================""")
        
            
LoginState = True
Role = "Bandung Bondowoso"
Help(LoginState,Role)
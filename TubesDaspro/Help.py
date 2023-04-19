
def Help(LoginState,Role):
    if LoginState == False :
        print(f"""
        \r=========== HELP ===========
        \r1. login
            \r  Untuk masuk menggunakan akun
        \r2. exit
            \r Untuk keluar dari program dan kembali ke terminal
        \r============================
        """)
    else:
        if Role == "bandung_bondowoso":
            print(f"""
            \r=========== HELP ===========
            \r1. logout
            \r   Untuk keluar dari akun yang digunakan sekarang
            \r2. summonjin
                \r  Untuk memanggil jin
            \r3. hilangkanjin
                \r Untuk menghilangkan jin
            \r4. ubahjin
                \r Untuk Mengubah Role Jin dari Pengumpul ke Pembangun dan sebaliknya
            \r5. batchkumpul
                \r Untuk melakukan pengumpulan bahan dengan banyak jin
            \r6. batchbangun
                \r Untuk melakukan pembangunan jin dengan banyak jin 
            \r7. laporanjin
                \r Untuk mengambil Laporan dari seluruh Jin yang sudah disummon
            \r8. laporancandi
                \r Untuk mengambil keseluruhan data dari candi yang sudah dibangun
            \r9. save
                \r Untuk saving data temporary ke csv file
            \r10. exit
                \r Untuk exit dari Permainan
            \r============================
            """)
        elif Role == "roro_jonggrang" :
            print(f"""
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. Hancurkancandi
                \r  Untuk menghancurkan candi yang tersedia
            \r3. ayamberkokok
                \r Untuk menyelesaikan permainan dengan memalsukan pagi hari 
            \r4. save
                \r Untuk saving data temporary ke csv file
            \r5. exit
                \r Untuk exit dari Permainan
            \r============================
            """)
            
        elif Role == "Pengumpul":
            print(f"""
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. kumpul
                \r  Untuk mengumpulkan resource candi
            \r3. save
                \r Untuk saving data temporary ke csv file
            \r4. exit
                \r Untuk exit dari Permainan
            \r============================
            """)
        else:
            print(f"""
            \r=========== HELP ===========
            \r1. logout
                \r  Untuk keluar dari akun yang digunakan sekarang
            \r2. bangun
                \r Untuk membangun suatu candi
            \r3. save
                \r Untuk saving data temporary ke csv file
            \r4. exit
                \r Untuk exit dari Permainan
            \r============================
            """)
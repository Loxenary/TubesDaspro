def SummonJin(jin,N):
    N += 1
    if N == 100 :
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print(f"""\rJenis jin yang dapat dipanggil:

                \r  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
                \r  (2) Pembangun - Bertugas membangun candi """)
        jenis = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))

        if not (jenis == 1 or jenis == 2):
            print(f"\nTidak ada jenis jin bernomor “{jenis}” !")
            SummonJin(jin,N)
        else:
            if jenis == 1 :
                jenis_jin = "Pengumpul" 
            else:
                jenis_jin = "Pembangun"
            print(f"\nmemilih jin “{jenis_jin}”.")

            username = input("\nMasukkan username jin: ")
            cek = False
            count = 0
            while cek == False:    
                for i in range (100) :
                    if jin[i][0] != str(username) :
                        count +=1   
                if count != 100 :
                    cek = False
                    print(f"\nUsername “{username}” sudah diambil!")
                    count = 0
                    username = input("\nMasukkan username jin: ")
                    continue
                    
                else:
                    cek = True

            password = input("Masukkan password jin: ")
            while not 5 <= len(password) <= 25 :
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("\nMasukkan password jin: ")
            print(f"""
            \rMengumpulkan sesajen...
            \rMenyerahkan sesajen...
            \rMembacakan mantra...

            \rJin {username} berhasil dipanggil!\n""")

            for i in range (100):   
                if jin[i][0] != 0 :
                    continue
                else:
                    jin[i][0] = username
                    break 
            print(jin)
            return (jin,N)


jin = [[0 for i in range (3)] for j in range (100)]
jin[0][0]= "genie"
N = 0

x,y = SummonJin(jin,N)
SummonJin(x , y)
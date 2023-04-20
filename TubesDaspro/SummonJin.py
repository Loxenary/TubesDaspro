def SummonJin(jin):
    jumlah = jumlah_jin(jin) #jumlah adalah variabel yang digunakan untuk menghitung ada berapa jumlah jin yang ada
    if jumlah == 100 : #kondisi jika jin sudah maksimal maka user tidak bisa mensummon lagi
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else: #kondisi yang masuk ketika user akan mensummon jin 
        print(f"""\rJenis jin yang dapat dipanggil:

                \r  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
                \r  (2) Pembangun - Bertugas membangun candi """)
        jenis = str(input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")) 
        #jenis adalah variabel yang meminta user memilih jenis jin apa yang akan disummon

        if (jenis != '1' and jenis != '2'): 
            #kondisi ini akan masuk ketika user tidak sesuai memasukkan jenis ada dan akan meminta user menginput ulang
            print(f"\nTidak ada jenis jin bernomor “{jenis}” !")
            SummonJin(jin)
        else:#jika masukkan sesuai maka akan dicek jenisnnya
            if jenis == '1' : #jika 1 maka jenis jin yang dipilih adalah pengumpul
                jenis_jin = "Pengumpul" 
            else:#jika 2 maka jenis jin yang dipilih adalah pembangun
                jenis_jin = "Pembangun"
            print(f"\nmemilih jin “{jenis_jin}”.")

            username = input("\nMasukkan username jin: ")
            #variabel username akan meminta user memasukkan nama dari jin yang disummon
            cek = False #cek adalah boolean yang akan digunakan sebagai batasan dari while loop nya
            count = 0 
            #count adalah variabel yang digunakan untuk menghitung jumlah total dari username pada list jin yang TIDAK SAMA dengan username (jika pada indeks tertentu pada list jin TIDAK SAMA dengan username , maka count nambah 1)
            while cek == False:     
                for i in range (100) : #looping yang digunakan untuk menghitung total count
                    if jin[i][0] != str(username) :
                        count +=1   
                if count != 100 : 
                    #jika total count TIDAK SAMA dengan 100 ,maka menandakan ada data yang sama pada list jin atau username sudah digunakan 
                    cek = False #maka cek akan tetap false untuk melooping ulang
                    print(f"\nUsername “{username}” sudah diambil!")
                    count = 0 #count akan dimulai lagi dari 0
                    username = input("\nMasukkan username jin: ")#dan user diminta untuk input username lagi
                    continue
                    
                else: #jika total count = 100 , maka username belum diambil
                    cek = True

            password = input("Masukkan password jin: ") #setelah itu user diminta memasukkan passwordnya
            while not 5 <= len(password) <= 25 : 
                #jika huruf dari password kurang dari 5 dan lebih dari 25 maka user diminta input ulang 
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("\nMasukkan password jin: ")
            print(f"""
            \rMengumpulkan sesajen...
            \rMenyerahkan sesajen...
            \rMembacakan mantra...

            \rJin {username} berhasil dipanggil!\n""") #maka summonjin sudah berhasil

            for i in range (100):#loop ini digunakan untuk mengisi data jin yang baru dimasukkan user kedalam list jin
                if jin[i][0] != None :
                    continue
                else:
                    jin[i][0] = username
                    jin[i][1] = password
                    jin[i][2] = jenis_jin
                    break
            jumlah += 1 #dan jumlah total jin akan bertambah 1 

def jumlah_jin(user_file): #fungsi ini digunakan untuk menghitung berapa banyak jumlah jin yang ada
    jumlah = 0
    for i in range(3,103):
        if(user_file[i][0] == None):
            continue
        else:
            jumlah += 1
    return jumlah
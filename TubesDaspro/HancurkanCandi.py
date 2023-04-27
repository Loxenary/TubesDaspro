def HancurkanCandi(candi):
    #list dari candi ini akan digunakan untuk mengakses id dari setiap candi yang ada
    TotalCandi = 0 #variabel untuk menghitung ada berapa total candi
    for i in range (1,101):
        if(candi[i][0] != None): #jika pada array candi tidak None maka ada candinya 
            TotalCandi += 1 #maka total candi akan bertambah

    if(TotalCandi == 0): #jika total candi = 0 maka user tidak dapat menghancurkan candi karena tidak ada candi yang terbangun
        print("Total candi = 0 , maka tidak ada candi yang dapat dihancurkan")
    else: #total!=0 maka akan lihat ceknya
        ID = str(input("Masukkan ID candi: ")) #variabel untuk id yang ingin user cek
        cek = False #boolean yang jika bernilai false maka id candi yang dimasukkan user tidak ada 
        for i in range (101): #looping yang digunakan untuk mengecek apakah id yang diingginkan user ada atau tidak
            if candi[i][0] != ID : #jika waktu diiterasi pada i dan tidak sesuai dengan ID maka akan dilanjutkan lagi loopnya
                continue
            else: 
                #jika ditemukan id yang sama maka loopnya akan berhenti dan cek nya akan bernilai true yang berarti id candi yang dimaksud user ditemukan    
                cek = True
                no = i
                break
        if cek == False : #jika kondisi false maka akan langsung keluar dengan output tidak ada candi dengan id tersebut
            print("Tidak ada candi dengan ID tersebut.")
            print(""" 
                  \rApakah anda ingin memasukkan ID lagi atau kembali ke menu utama?
                  \rKetik 1 untuk masukkan ID lagi
                  \rKetik 2 untuk ke menu utama""") 
            user = int(input("Ketik pilihan anda = ")) #user adalah keputusan dari user apakah dia akan kembali ke fitur hancurkan candi atau kembali ke menu utama
            while user != 1 and user != 2 : #while disini digunakan jika user salah menginput angka
                print("Masukkan anda salah, ketik yang benar!")
                user = int(input("Ketik pilihan anda = "))
            
            if user == 1 :#user memilih masukkan ID lagi
                HancurkanCandi(candi) #user akan diminta input ulang ID 
            else : #user memilih kembali ke menu utama
                print() 

        else: #jika True maka akan masuk kondisi dimana ada candi dengan id yang dimaksud user
            pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
            #pilihan adalah variabel yang diinput user yang meminta apakah candi akan dihapus atau tidak
            def keputusan(pilihan): #fungsi ini digunakan untuk mengeluarkan hasil dari pilihan user     
                if pilihan == "y" or pilihan == "Y" :#jika user mengeluarkan y maka candi akan dihapuskan
                    print("Candi telah berhasil dihancurkan.")
                    for i in range(5):
                        candi[no][i] = None #candi akan dihapuskan dengan menghapus data pada indeks yang sudah disimpan di variabel "no"
                elif pilihan == "n" or pilihan == "N" : #jika user mengeluarkan n maka candi tidak akan dihapuskan
                    print("Candi tidak jadi dihancurkan.")
                else:  #jika user mengeluarkan selain n dan y , maka program akan meminta ulang user untuk menginput pilihan
                    print("Masukkan salah")
                    pilihan = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)?")
                    keputusan(pilihan)
            keputusan(pilihan)
def HapusJin (jinlist,candilist) :
    a=0 # sebagai variabel untuk menentukan apakah username yang dimasukkan sesuai data di user.csv
    jumlahjin = 0 # sebagai variabel untuk menghitung jumlah jin pada jinlist
    username = str(input("Masukkan Username = ")) # untuk menginput username jin yang ingin dihapus
    for i in range(3,103): 
        if(jinlist[i][0] != None): # untuk mengecek apakah ada username jin pada jinlist
            jumlahjin += 1 # jika ada maka jumlahjin bertambah 1
        if(username == jinlist[i][0]): # melakukan pengecekan apakah terdapat username jin yang ingin dihapus pada jinlist
            a+=1 # jika ada maka a akan bertambah 1
            indeks_jin = i
            break # setelah ditemukan username jin yang ingin dihapus pada jinlist, loop akan berhenti
    if a>0 : # apabila terdapat username jin yang ingin dihapus pada jinlist
        pilihan = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {username} , (Y/N)?\n"))
        while pilihan != 'Y' and pilihan != 'N' and pilihan!='y' and pilihan!='n': # apabila input pilihan dari user tidak sesuai (bukan Y atau N) maka akan terjadi pengulangan input pilihan
            pilihan = str(input("Masukkan input yang benar (Y/N) :  "))
        if(pilihan == 'Y' or pilihan == 'y'): 
            for i in range(3):
                jinlist[indeks_jin][i] = None # untuk menghapus username jin pada jinnlist
            for i in range (0,101):
                if (username == candilist[i][1]):
                    for j in range(5):
                        candilist[i][j] = None # untuk menghapus candi yang dibangun oleh jin yang dihapus
            print("Jin telah berhasil dihapus dari alam ghaib")
        else: # fungsi akan mengulang kembali user menginput N/n
            print("Masukkan input ulang") 
            HapusJin(jinlist,candilist) 
    else:
        if(jumlahjin == 0): # apabila tidak terdapat satupun jin pada jinlist
            print("Tidak ada jin yang dapat dihapus")
        else: # apabila tidak ditemukan username jin yang ingin dihapus
            print("Tidak ada jin dengan username tersebut")  
            ulang = input("Apakah anda ingin kembali menginput username dan password atau kembali ke pusat control (Y/N)") # Apabila user ingin kembali ke menu utama
            while ulang != "Y" and ulang != "N" and ulang!="y" and ulang!="y":
                print("Masukkan input yang benar")  
                ulang = input("Apakah anda ingin kembali menginput username dan password atau kembali ke pusat control (Y/N)")
            if ulang == "Y" or ulang=="y":
                HapusJin(jinlist,candilist)
            else :#ulang == "n"/"N"
                return
         


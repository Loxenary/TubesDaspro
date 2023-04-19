import argparse # Module ArgParse untuk run dengan console
import sys # Module sys dalam kasus ini hanya digunakan untuk keluar dari program
import time # Module time pada kasus ini hanya sebagai jeda antar print sehingga terlihat lebih bagus
import os # Module os pada kasus ini digunakan untuk mengecek ada atau tidaknya folder yang dicari


defaultText = "Tidak ada nama folder yang diberikan!" # akan digunakan saat parser.argument

parser = argparse.ArgumentParser(prog="python MainProgram.py", usage= '%(prog)s ' "nama_folder") 
# argparse.ArgumentParser digunakan untuk membuat suatu argument parser agar dapat ditambahkan argument lain dan sejenisnya
# prog disini adalah nama program dan usage ini akan ditampilkan ketika print_usage dipanggil

parser.add_argument("nama_folder",  type=str ,nargs = '?',default = defaultText) 
# parser.add_argument() akan mendefinisikan argument dalam kontex ini yaitu "nama_folder", type = str berarti type nya string
# nargs = '? dan default = defaultText, berarti ketika tidak ada argument yang diberikan (cth: python MainProgram.py ) maka akan memunculkan variable defaultText sebagai hasil argument nya  

args = parser.parse_args() # args ini adalah variable yang menyimpan value dari parser ini, dalam kasus ini adalah hasil argument pada parser.add_argument sebelumnya

# os.path.isdir akan mengecek apakah args.nama_folder (argument yang diinput user pada command line) (dalam kasus ini adalah nama folder) ada pada folder pengguna
# args.nama_folder memanggil value dari parser.add_argument (cth, jika input user: python MainProgram.py fileSave, maka args.nama_folder adalah fileSave)
if(os.path.isdir(args.nama_folder)): # asumsi : dalam folder yang dimaksud, file-file csv yang akan digunakan sudah ada dalam folder tersebut.
    os.system('cls') # clearing command line, hanya agar terlihat lebih rapi
    print("loading...") 
    time.sleep(0.25) # memberikan jeda 0.25 detik sebelum pindah ke output berikutnya
    print('\nSelamat datang di program "Manajerial Candi"\nMasukkan command "help" untuk daftar\ncommand yang dapat kamu panggil.')
    folder = args.nama_folder # folder ini akan digunakan untuk membuka file csv nantinya pada file tempData
else: # jika folder tidak ditemukan atau input nama folder salah
    if(args.nama_folder == defaultText): # defaultText adalah variable yang dihasilkan ketika tidak ada argument yang diberikan (cth: python MainProgram.py ). 
        print("Tidak ada nama folder yang diberikan!") 
        parser.print_usage() # memanggil usage yang ada di argparse.ArgumentParser 
        sys.exit() # keluar dari program

    else: # user memasukan nama folder yang tidak ada atau folder bohong
        print(f"Tidak ada Folder yang bernama {args.nama_folder} pada sistem")
        parser.print_usage() # memanggil usage yang ada di argparser.ArgumentParser  
        sys.exit() # keluar dari program



   

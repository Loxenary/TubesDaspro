import argparse
import sys
import time
import os


defaultText = "Tidak ada nama folder yang diberikan!"
parser = argparse.ArgumentParser(prog="python main.py", usage= '%(prog)s TUBESDASPRO')
parser.add_argument("nama_folder",  type=str ,nargs = '?',default = defaultText)
args = parser.parse_args()
if(os.path.isdir(args.nama_folder)):
    print("loading",end="")
    for i in range(1,4):
        time.sleep(0.01)
        print(".",end="")
    print('''\nSelamat datang di program "Manajerial 
Candi"
    ''')
    folder = args.nama_folder

else:
    if(args.nama_folder == defaultText):
        print("Tidak ada nama folder yang diberikan!")
        parser.print_usage()
        sys.exit()
    else:
        print("salah folder awkkwkww")
        print(args.nama_folder)
        sys.exit()



   

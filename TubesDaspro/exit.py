import sys
import BuildInFunction as Build

def exit ():
    choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    while choise != "y" and choise != "Y" and choise != "N" and choise != "n":
         choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    sys.exit("Program keluar")

print(exit())

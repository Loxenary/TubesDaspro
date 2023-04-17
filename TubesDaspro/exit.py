import sys
import BuildInFunction as Build
import save as Saving
import TempData as data
def exit ():
    choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    while choise != "y" and choise != "Y" and choise != "N" and choise != "n":
         choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    if(choise == 'y' or choise == 'Y'):
        Saving.save(data.users,data.candi,data.bahan)
        sys.exit("Program Keluar")
    else:
        sys.exit("Program Keluar")

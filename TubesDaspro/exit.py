import sys
import save as Saving # untuk melakukan save progres permainan
import TempData as data
def exit ():
    choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    while choise != "y" and choise != "Y" and choise != "N" and choise != "n":
         choise = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")) # loop apabila input user tidak sesuai (bukan y atau n)
    if(choise == 'y' or choise == 'Y'): # user ingin melakukan save terlebih dahulu
        Saving.save(data.users,data.candi,data.bahan) # untuk melakukan save terlebih dahulu sebelum keluar permainan
        sys.exit("Program Keluar")
    else:
        sys.exit("Program Keluar") # langsung keluar permainan tanpa melakukan save

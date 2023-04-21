import time
import os

def SearchRandomSeed(k): # built-in random generator # k untuk biar lebih random aja
    now = time.perf_counter() # time.perf_counter akan menghasilkan angka random dari perhitungan waktu eksekusi performance benchmark 
    ProcessId= os.getpid() # os.getpid akan menghasilkan angka random dari process ID (PID) dari current process
    seed = int(now * ProcessId * k) # variable k akan menyebabkan hasil seed nya berbeda jika program dijalankan berulang-ulang dalam waktu singkat

    return seed
    
def SearchRandomNumber(minimum,maximum,k): # k agar nilai yang dihasilkan lebih random
    seed = SearchRandomSeed(k) # seed agar hasil nya makin random, k adalah variable yang akan membuat misalnya ketika dibutuhkan 3 kali pencarian random number, hasil ketiganya tidak sama
    a = 1662533 
    c = 1283463648
    m = 2**32
    r = (a * seed + c) % m # algoritma linear
    hasil = minimum + int((maximum - minimum + 1) * (r / (m + 1))) # perhitungan agar hasilnya tidak kurang dan lebih dari minimum dan maximum, serta agar hasilnya selalu integer

    return hasil 


def Diffrence(Inisial,Final): # untuk menghitung butuh berapa agar Inisial mencapai Final
    if(Inisial < Final): 
        return Final - Inisial
    else:
        return 0

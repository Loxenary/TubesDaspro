import time
import os

def SearchRandomSeed(k): # built-in random generator # k untuk biar lebih random aja
    now = time.perf_counter()
    ProcessId= os.getpid()
    seed = int(now * ProcessId * k)

    return seed
    
def SearchRandomNumber(minimum,maximum,k): # k agar nilai yang dihasilkan lebih random
    seed = SearchRandomSeed(k)
    a = 1662533
    c = 1283463648
    m = 2**32
    r = (a * seed + c) % m
    hasil = minimum + int((maximum - minimum + 1) * (r / (m + 1)))

    return hasil

def uppercase(string):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    uppercase_string = ""
    for i in range(len(string)):
       for j in range(26):
            if(string[i] == lowercase[j]):
                uppercase_string += uppercase[j]
                break
            if(j == 25):
                uppercase_string += string[i]


    return uppercase_string

def Diffrence(Inisial,Final): # untuk menghitung butuh berapa agar Inisial mencapai Final
    if(Inisial < Final):
        return Final - Inisial
    else:
        return 0

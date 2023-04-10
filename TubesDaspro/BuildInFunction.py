import time
import os

def TambahList(list1,Addvar): #built-in .append()
    if(isinstance(Addvar,int)  or isinstance(Addvar,str)):
        templist = [0 for i in range(PanjangList(list1)+1)]
        for i in range(PanjangList(templist)):
            if(i < PanjangList(templist)-1):
                templist[i] = list1[i]
            else:
                templist[i] = Addvar
        return templist
    else:
        list2 = Addvar
        templist = [0 for i in range(PanjangList(list1)+PanjangList(list2))]
        for i in range(PanjangList(templist)):
            if(i < PanjangList(templist)-PanjangList(list2)):
                templist[i] = list1[i]
            else:
                templist[i] = list2[i-PanjangList(list1)]
        return templist

def TambahListMatriks2xn(list1,list2):
    templist = [[]]
    templist2 = []
    for i in range(PanjangList(list1) + PanjangList(list2)):
        if(i < PanjangList(list1)):
            templist2 = [list1[i]]
            templist = [TambahList(templist,templist2)]
        else:
            templist2 = [list2[i-PanjangList(list1)]]
            templist = [TambahList(templist,templist2)]
    return templist
def PanjangList(list1): #built-in len()
    count = 0
    for i in list1:
        count+=1 
    return count


def SortDariTerkecil(list): # built-in sort.ascending()
    for i in range(PanjangList(list)):
        minimum = i
        for j in range(i + 1, PanjangList(list)):
           if list[j] < list[minimum]:
               minimum = j
        (list[i], list[minimum]) = (list[minimum], list[i])

def SortDariTerbesar(list): # built-in sort.descending
    for i in range(PanjangList(list)):
        maksimum = i
        for j in range(i + 1, PanjangList(list)):
           if list[j] > list[maksimum]:
               maksimum = j
        (list[i], list[maksimum]) = (list[maksimum], list[i])

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

def Maksimum(list):
    SortDariTerbesar(list)
    return list[0]

def Minimum(list):
    SortDariTerkecil(list)
    return list[0]

def Remove(list, removeVar):
    templist = []
    for k in range(PanjangList(list)):
        if(removeVar == list[k]):
            continue
        else:
            templist = TambahList(templist,list[k])
            print(PanjangList(templist))

    if(PanjangList(templist) == PanjangList(list)):
        return None
    else:
        return templist
    
def Insert(list,indexlist,apayangmaudiinsert):
    templist = []
    k = 0
    for i in range(PanjangList(list)+1):
        if(i == indexlist):
            templist = TambahList(templist,apayangmaudiinsert)
        else:
            templist = TambahList(templist,list[k])
            k+= 1
    return templist
def count(list,angkayangingindicari):
    count = 0
    for i in range(PanjangList(list)):
        if list[i] == angkayangingindicari:
            count += 1
    return count

def pop1Matriks(list,indexyangingindihapus):
    templist = []
    for i in range(PanjangList(list)):
        if (i == indexyangingindihapus):
            continue
        else:
            templist = TambahList(templist,list[i])
    return templist

def pop2Matriks(list,indexyanginginindihapus):
    templist = []
    templist2 = []
    for i in range(PanjangList(list)):
        templist2 = [list[i]]
        if (i == indexyanginginindihapus):
            continue
        else:
            templist = TambahList(templist,templist2)
    return templist
def extend(list1,list2):
    templist1 = []
    for i in range(PanjangList(list1)):
        templist = TambahList(templist,list1[i])
    for i in range(PanjangList(list2)):
        templist = TambahList(templist,list2[i])
    return templist

def index(list,var):
    hasil = 0
    for i in range(PanjangList(list)):
        if list[i] == var:
            hasil = i
            break
    return hasil

def reverse(list):
    templist = []
    for i in range(PanjangList(list)-1,-1,-1):
        templist = TambahList(templist,list[i])
    return templist

def clear(list):
    list = []
    return list

def split(list,delimeters):
    templist1 = []
    word = ""
    for i in list:
        if i != delimeters:
            word += i
        else:
            templist1 = TambahList(templist1,str(word))
            word= ''
    if word:
        templist1 = TambahList(templist1,word)
    return templist1

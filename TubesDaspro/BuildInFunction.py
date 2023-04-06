import time

def TambahList(list,Addvar): #built-in .append()
    templist = [0 for i in range(PanjangList(list)+1)]
    for i in range(PanjangList(templist)):
        if(i != PanjangList(templist)-1):
            templist[i] = list[i]
        else:
            templist[i] = Addvar
    return templist

def PanjangList(list): #built-in len()
    count = 0
    for i in (list):
        count += 1
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

def SearchRandomNumber(minimum,maximum): # built-in random generator
    now = str(time.perf_counter())
    random = float(now[4])/10
    print(int(minimum + random*(maximum-minimum)))

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
def pop(list,indexyangingindihapus):
    templist = []
    for i in range(PanjangList(list)):
        if (i == indexyangingindihapus):
            continue
        else:
            templist = TambahList(templist,list[i])
    return templist

def extend(list1,list2):
    templist = []
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


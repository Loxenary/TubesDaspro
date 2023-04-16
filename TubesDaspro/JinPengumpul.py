import BuildInFunction as Build

def JinPengumpul ():
    pasir = Build.SearchRandomNumber(0,5,1)
    batu = Build.SearchRandomNumber(0,5,2)
    air = Build.SearchRandomNumber(0,5,3)
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return pasir , batu , air 

JinPengumpul()
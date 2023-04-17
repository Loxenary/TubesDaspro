import BuildInFunction as Build

def JinPengumpul (bahan_bangunan):
    pasir = Build.SearchRandomNumber(0,5,1)
    batu = Build.SearchRandomNumber(0,5,2)
    air = Build.SearchRandomNumber(0,5,3)
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir)
    bahan_bangunan[2][2] = str(int(bahan_bangunan[1][2]) + batu)
    bahan_bangunan[3][2] = str(int(bahan_bangunan[1][2]) + air)

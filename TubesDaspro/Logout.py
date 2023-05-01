import TempData as data
def UserLogout():
    data.LoginState = False
    #keadaan login dari suatu user dikembalikan menjadi false sehingga user terlogout dari role
    print("Berhasil Logout")

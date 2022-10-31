import cek_stok
from getpass import getpass
import os
import admin
import user
import hashlib
import account

def main():
    # Program Mulai
    cek_stok.init_object()


    # Cek User atau Admin
    print("Selamat Datang di Mesin Kasir!")
    username = input("Username: ")
    password = getpass()

    hasil_cek = account.check_credential(username, password)
    if hasil_cek[0] and hasil_cek == 'admin' :
        # sistem_admin
        admin.sistem_admin()
    elif hasil_cek[0] and hasil_cek == 'user':
        # Kerjain User biasa disini
        print("Welcome to mesin kasir")
        isRun = True
        while isRun == True:
            user.daftar_belanja = []
            user.sistem_user()
            next = input("Lanjut? y / n: ")
            if next == 'n':
                isRun = False

main()
import cek_stok
from getpass import getpass
import os
import admin
import user

# Program Mulai
cek_stok.init_object()

# Cek User atau Admin
print("Selamat Datang di Mesin Kasir!")
username = input("Username: ")
password = getpass()

if username == "admin" and password == "lmao":
    # sistem_admin
    admin.sistem_admin()
elif username == 'user' and password == 'user':
    # Kerjain User biasa disini
    print("Welcome to mesin kasir")
    isRun = True
    while isRun == True:
        user.daftar_belanja = []
        user.sistem_user()
        next = input("Lanjut? y / n: ")
        if next == 'n':
            isRun = False
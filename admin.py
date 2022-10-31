import cek_stok
import clear
import daily_retail

daftar_perintah = {
        "1": ["cek stok", cek_stok.cek_stok],
        "2": ["cek semua stok", cek_stok.get_all_stok],
        "3": ["tambahin item baru"],
        "4": ["update deskripsi item"],
        "5": ["Liat statistik"]
    }

def tampilan():
    # Judul
    print("==========================================")
    print("||    Selamat Datang di Sistem ADMIN    ||")
    print("==========================================")
    
    
    print("||" + "Daftar List".center(38) + "||")
    for x in daftar_perintah:
        print("||" + f"\t{x} - {daftar_perintah[x][0]}".expandtabs(6).ljust(38) + "||")
    print("==========================================")

def sistem_admin():
    # Bersihkan layar
    clear.cls()

    isRun = True
    while isRun:
        tampilan() 

        temp = input("> ")
        if temp == '0':
            isRun = False
        elif temp == '3':
            item_id = input("item_id\t: ")
            item_name = input("nama\t: ")
            item_price = input("harga\t: ")
            item_stock = input("stok\t: ")
            args = {
                "nama": item_name,
                "harga": item_price,
                "stok": item_stock
            }
            cek_stok.update_item(item_id, args)
            print("item berhasil dimasukkan")

            x = input()
            sistem_admin()
        elif temp == '4':
            item_id = input("item_id\t: ")
            arg = input("> ")
            arg = arg.split(';')
            print("nilai arg: ", arg)
            args = {}
            while len(arg) > 0:
                arg[0] = arg[0].split(' ')
                key = arg[0][0]
                args[arg[0][0]] = ""
                arg[0].pop(0)
                arg[0] = ' '.join(arg[0])
                args[key] = arg[0]
                arg.pop(0)
            cek_stok.update_item(item_id, args)
        elif temp == '5':
            daily_retail.main()
        else:
            print("masuk sini")
            daftar_perintah[temp][1]()
            input("press any key to continue...")

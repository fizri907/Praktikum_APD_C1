users = [] 

pembelian = []  

while True:
    print("\n=== Aplikasi Pembelian Tembakau ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    opsi = input("Pilih opsi: ")
    
    if opsi == '1':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        role = input("Masukkan role (admin/pengguna biasa): ")

        if any(user[0] == username for user in users):
            print("Username sudah terdaftar!")
        else:
            users.append([username, password, role])
            print("Pendaftaran berhasil!")

    elif opsi == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        user = next((u for u in users if u[0] == username and u[1] == password), None)

        if user:
            print(f"Selamat datang, {username}!")
            while True:
                print("\n=== Menu Pengguna ===")
                if user[2] == 'admin':
                    print("1. Tambah Pembelian")
                    print("2. Update Pembelian")
                    print("3. Hapus Pembelian")
                    print("4. Lihat Pembelian")
                    print("5. Logout")
                else:
                    print("1. Tambah Pembelian")
                    print("2. Lihat Pembelian")
                    print("3. Logout")

                pengguna = input("Pilih opsi: ")
                
                if pengguna == '1':
                    item = input("Masukkan nama item pembelian: ")
                    found = False
                    for pem in pembelian:
                        if pem[0] == username:
                            pem[1].append(item)
                            found = True
                            break
                    if not found:
                        pembelian.append([username, [item]])
                    print("Item berhasil ditambahkan!")

                elif pengguna == '2':
                    if user[2] == 'admin':
                        print("Daftar pembelian:")
                        for pem in pembelian:
                            if pem[0] == username:
                                print(f"Item: {', '.join(pem[1])}")
                                break
                        old_item = input("Masukkan nama item yang ingin diupdate: ")
                        new_item = input("Masukkan nama item baru: ")
                        
                        for pem in pembelian:
                            if pem[0] == username:
                                if old_item in pem[1]:
                                    pem[1][pem[1].index(old_item)] = new_item
                                    print("Item berhasil diupdate!")
                                    break
                                else:
                                    print("Item tidak ditemukan!")
                                    break
                        else:
                            print("Tidak ada pembelian untuk pengguna ini.")

                    else:
                        print("Daftar pembelian:")
                        for pem in pembelian:
                            if pem[0] == username:
                                print(f"Item: {', '.join(pem[1])}")
                                break
                elif pengguna == '3':
                    if user[2] == 'admin':
                        print("Daftar pembelian:")
                        for pem in pembelian:
                            if pem[0] == username:
                                print(f"Item: {', '.join(pem[1])}")
                                break
                        item = input("Masukkan nama item yang ingin dihapus: ")

                        for pem in pembelian:
                            if pem[0] == username:
                                if item in pem[1]:
                                    pem[1].remove(item)
                                    print("Item berhasil dihapus!")
                                    break
                                else:
                                    print("Item tidak ditemukan!")
                                    break
                        else:
                            print("Tidak ada pembelian untuk pengguna ini.")
                    else:
                        print("Anda telah logout.")
                        break

                elif pengguna == '4' and user[2] == 'admin':
                    print("Daftar pembelian:")
                    for pem in pembelian:
                        if pem[0] == username:
                            print(f"Item: {', '.join(pem[1])}")
                            break
                elif pengguna == '5':
                    print("Anda telah logout.")
                    break
                else:
                    print("Opsi tidak valid!")
        else:
            print("Username atau password salah!")

    elif opsi == '3':
        print("Keluar dari aplikasi.")
        break
    else:
        print("Opsi tidak valid!")

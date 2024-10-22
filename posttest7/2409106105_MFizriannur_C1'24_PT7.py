users = {
    "fijri" : {'password' : '1', 'role' : 'admin'},
    "jamal" : {'password' : '1', 'role' : 'pengguna'}
}

pembelian = {

}

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

        if username in users:
            print("Username sudah terdaftar!")
        else:
            users[username] = {"password": password, "role": role}
            print("Pendaftaran berhasil!")

    elif opsi == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        user = users.get(username)
        if user and user["password"] == password:
            print(f"Selamat datang, {username}!")
            while True:
                print("\n=== Menu Pengguna ===")
                if user["role"] == 'admin':
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
                    if username not in pembelian:
                        pembelian[username] = [item]
                    else:
                        pembelian[username].append(item)
                    print("Item berhasil ditambahkan!")

                elif pengguna == '2':
                    if user["role"] == 'admin':
                        if username in pembelian:
                            print("Daftar pembelian:")
                            print(f"Item: {', '.join(pembelian[username])}")
                            old_item = input("Masukkan nama item yang ingin diupdate: ")
                            new_item = input("Masukkan nama item baru: ")
                            if old_item in pembelian[username]:
                                pembelian[username][pembelian[username].index(old_item)] = new_item
                                print("Item berhasil diupdate!")
                            else:
                                print("Item tidak ditemukan!")
                        else:
                            print("Tidak ada pembelian untuk pengguna ini.")
                    else:
                        if username in pembelian:
                            print("Daftar pembelian:")
                            print(f"Item: {', '.join(pembelian[username])}")
                        else:
                            print("Tidak ada pembelian untuk pengguna ini.")

                elif pengguna == '3':
                    if user["role"] == 'admin':
                        if username in pembelian:
                            print("Daftar pembelian:")
                            print(f"Item: {', '.join(pembelian[username])}")
                            item = input("Masukkan nama item yang ingin dihapus: ")
                            if item in pembelian[username]:
                                pembelian[username].remove(item)
                                print("Item berhasil dihapus!")
                            else:
                                print("Item tidak ditemukan!")
                        else:
                            print("Tidak ada pembelian untuk pengguna ini.")
                    else:
                        print("Anda telah logout.")
                        break

                elif pengguna == '4' and user["role"] == 'admin':
                    if username in pembelian:
                        print("Daftar pembelian:")
                        print(f"Item: {', '.join(pembelian[username])}")
                    else:
                        print("Tidak ada pembelian untuk pengguna ini.")
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
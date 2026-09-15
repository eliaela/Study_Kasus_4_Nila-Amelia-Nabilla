produk = {
    "nama": "Oversized Band Tee",
    "harga": 150000,
    "stok": 15
}

while True:
    print("\n=== DATA PRODUK FASHION TOKO DISTRICT 404 ===")
    print("1. Tampilkan Data Produk")
    print("2. Tambah Kategori")
    print("3. Ubah Harga")
    print("4. Hapus Kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n--- DATA PRODUK ---")
        for key, value in produk.items():
            print(key, ":", value)

    elif pilihan == "2":
        produk["kategori"] = "Grunge"
        print("Kategori berhasil ditambahkan.")

    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("Harga berhasil diubah.")

    elif pilihan == "4":
        if "kategori" in produk:
            del produk["kategori"]
            print("Kategori berhasil dihapus.")
        else:
            print("Kategori belum ada.")

    elif pilihan == "5":
        print("\n--- DATA PRODUK SETELAH PERUBAHAN ---")
        for key, value in produk.items():
            print(key, ":", value)
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
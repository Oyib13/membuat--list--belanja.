
transaksi_list = []

def tambah_transaksi(id_transaksi, id_produk, jumlah):
    """Menambahkan transaksi baru ke dalam daftar transaksi."""
    transaksi = (id_transaksi, id_produk, jumlah)
    transaksi_list.append(transaksi)
    print(f"Transaksi {id_transaksi} berhasil ditambahkan.")

def tampilkan_transaksi():
    """Menampilkan semua transaksi yang tercatat."""
    if not transaksi_list:
        print("Belum ada transaksi yang tercatat.")
    else:
        print("Daftar Transaksi:")
        for transaksi in transaksi_list:
            print(f"ID Transaksi: {transaksi[0]}, ID Produk: {transaksi[1]}, Jumlah: {transaksi[2]}")

if __name__ == "__main__":
    tambah_transaksi("T001", "P001", 3)
    tambah_transaksi("T002", "P002", 5)
    tambah_transaksi("T003", "P003", 2)

    tampilkan_transaksi()
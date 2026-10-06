import json
import os

FILE = "iventaris.json"


def baca_file():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []



def simpan_file(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def tampilkan_data():
    data = baca_file()

    if len(data) == 0:
        print("belum ada data barang.")
        return

    print("\n" + "=" * 50)
    print(f"{'No':<4}{'Kode':<10}{'Nama':<18}{'Stok':<8}{'Harga':<10}")
    print("=" * 50)
    no = 1
    for barang in data:
        print(f"{no:<4}{barang['kode']:<10}{barang['nama']:<18}{barang['stok']:<8}{barang['harga']:<10}")
        no += 1
        print("=" * 50)


def tambah_data():
    print("\n--- tambah barang baru ---")
    kode = input("kode barang : ")
    nama = input("nama barang : ")
    stok = input("stock :")
    harga = input("harga :")

    if not stok.isdigit() or not harga.isdigit():
        print("stok dan harga harus berupa angka. data tidak disimpan.")
        return

    barang_baru = {
        "kode": kode,
        "nama": nama,
        "stok": int(stok),
        "harga": int(harga)
    }



    data = baca_file()
    data.append(barang_baru)
    simpan_file(data)

    print("data barang berhasil ditambahkan!")


while True:
    print("\n=== iventaris barang toko ===")
    print("1. lihat semua barang")
    print("2. tambah barang baru")
    print("3. keluar")
    pilihan = input("pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("terimakasih sudah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid, coba lagi.")
# Sistem Manajemen Inventaris Barang

Program Python sederhana untuk mencatat dan melihat stok barang di sebuah toko kelontong. Data barang disimpan secara permanen di file **JSON**, sehingga tidak hilang saat program dijalankan ulang.

| | |
|---|---|
| **Nama** | Muhammad Ardhika Prasanjayu |
| **NIM** | 2609116108 |
| **Kelas** | C |
| **Soal** | Genap |

## Fitur

- Menampilkan seluruh data barang dari file `inventaris.json`.
- Menambahkan data barang baru dan menyimpannya ke file.
- Menu berjalan terus-menerus (`while` loop) sampai pengguna memilih keluar.
- Validasi sederhana: stok dan harga harus berupa angka.

File `inventaris.json` dibuat otomatis saat barang pertama ditambahkan. Tidak ada library tambahan yang perlu dipasang karena program hanya memakai modul bawaan Python (`json` dan `os`).

## Menu Program

<img width="301" height="116" alt="image" src="https://github.com/user-attachments/assets/8363be32-889c-40c4-b179-b7edf1eac993" />

| Pilihan | Fungsi |
|---|---|
| 1 | Membaca file dan menampilkan semua barang dalam bentuk tabel |
| 2 | Meminta kode, nama, stok, dan harga, lalu menyimpannya ke file |
| 3 | Menghentikan program |
| Lainnya | Menampilkan pesan "Pilihan tidak valid" lalu menu muncul lagi |

## Format Data

Data disimpan di `inventaris.json` sebagai daftar (list) berisi objek barang:

<img width="391" height="482" alt="Screenshot 2026-10-06 183251" src="https://github.com/user-attachments/assets/91119558-57cd-4bde-ad11-4af8a078c038" />


## Penjelasan Kode

| Bagian kode | Fungsi dan kegunaan |
|---|---|
| `import json`, `import os` | `json` untuk membaca dan menulis file JSON, `os` untuk mengecek apakah file sudah ada |
| `FILE = "inventaris.json"` | Menyimpan nama file data di satu tempat supaya mudah diganti |
| `baca_file()` | Membaca isi file JSON dan mengembalikannya sebagai list. Jika file belum ada atau isinya rusak, mengembalikan list kosong agar program tidak error |
| `simpan_file(data)` | Menulis seluruh list data ke file JSON dengan `json.dump` (`indent=4` agar rapi dibaca) |
| `tampilkan_data()` | Memanggil `baca_file()`, lalu menampilkan setiap barang dalam tabel memakai perulangan `for`. Jika data kosong, menampilkan "Belum ada data barang" |
| `tambah_data()` | Meminta input barang baru, mengecek stok dan harga dengan `isdigit()`, lalu menyimpannya ke file |
| `while True` (menu utama) | Menampilkan menu terus-menerus. Perulangan berhenti dengan `break` ketika pengguna memilih 3 |
| `if / elif / else` | Memilih tindakan sesuai menu yang dipilih pengguna |

### Cara data baru tersimpan permanen

Berbeda dengan CSV, file JSON tidak bisa langsung ditambah (append) di baris akhir. Karena itu `tambah_data()` bekerja dalam tiga langkah:

1. Membaca seluruh data lama dari file (`baca_file()`).
2. Menambahkan barang baru ke list dengan `append()`.
3. Menulis ulang seluruh list ke file (`simpan_file()`).

Dengan cara ini data lama tidak hilang dan data baru ikut tersimpan, sehingga saat program dijalankan lagi data tetap ada.

## Screenshot Hasil Program

### 1. Menu dan proses menambah barang

<img width="346" height="978" alt="Screenshot 2026-10-06 182316" src="https://github.com/user-attachments/assets/b7538c3f-e863-49e5-8460-131c1079e54a" />

### 2. Menampilkan seluruh data barang

<img width="502" height="516" alt="Screenshot 2026-10-06 182712" src="https://github.com/user-attachments/assets/fa7ec0c3-5fe9-40e5-b523-73836ed53bdb" />


### 3. Data baru tetap tersimpan setelah program dijalankan kembali

Program dijalankan ulang, lalu menu 1 dipilih. Data yang ditambahkan pada sesi sebelumnya masih muncul.

<img width="502" height="471" alt="Screenshot 2026-10-06 183006" src="https://github.com/user-attachments/assets/89f088df-d5fa-4790-993e-24dba9266a39" />

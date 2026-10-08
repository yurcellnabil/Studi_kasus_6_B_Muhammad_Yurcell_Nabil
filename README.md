# Studi_kasus_6_B_Muhammad_Yurcell_Nabil

# 💻 Tugas Praktikum Dasar Dasar Pemrograman

## 1. Identitas
- **Nama:** Muhammad Yurcell Nabil
- **NIM:** 2609116073
- **KELAS:** B
- **Mata Kuliah:** Praktikum Dasar Dasar Pemrograman

## 2. Deskripsi Program
Program Sistem Pencatatan Nilai Mahasiswa adalah program yang bertujuan untuk membantu pengguna terutama dosen dalam mencatat dan melihat data nilai mahasiswa dengan lebih mudah dan rapi.
Dalam program ini, pengguna (dosen) dapat melihat riwayat nilai mahasiswa yang sudah tersimpan dan dapay menambahkan data nilai mahasiswa yang baru, Data yang dicatat meliputi nama mahasiswa, NIM, mata kuliah, dan nilai ujian jadi tidak perlu manual lagi, dan file JSON sebagai tempat penyimpanan data. Jadi, ketika pengguna menambahkan data baru, data tersebut akan disimpan ke dalam file nilai_mahasiswa.json. Dengan begitu, data yang sudah dimasukkan tidak hanya tersimpan sementara, tetapi juga bisa dibuka kembali ketika program dijalankan lagi.
Program ini juga menggunakan menu pilihan yang terdiri dari tiga menu, yaitu melihat riwayat nilai mahasiswa, menambahkan rekap nilai baru, dan keluar dari program.


## 3. Kode Program yang digunakan

Mungkin sedikit tambahan yang saya sampaikan garis besar yang lebih ditekankan untuk program pencatatan nilai mahasiswa 

<img width="781" height="414" alt="Screenshot 2026-10-08 170544" src="https://github.com/user-attachments/assets/34a8895e-6fec-4a4d-a628-c93b607325c2" />

import json berfungsi sebagai memanggil library JSON untuk membaca dan menyimpan data.

with open() berfungsi sebagai membuka file yang berisi data mahasiswa.

json.load() berfungsi sebagai membaca data dari file JSON.

def tambah_data() berfungsi sebagai membuat fungsi untuk menambahkan data mahasiswa.

data.append() berfungsi sebagai menambahkan data baru ke daftar yang sudah ada.

json.dump() berfungsi sebagai menyimpan data ke file JSON.

while True berfungsi sebagai membuat menu terus muncul sampai pengguna memilih keluar.



<img width="783" height="431" alt="Screenshot 2026-10-08 170607" src="https://github.com/user-attachments/assets/d4d3836a-5deb-4a2b-a7f9-62d6fcf0cbb3" />

def tambah_data() berfungsi untuk menambahkan data nilai mahasiswa.

return berfungsi untuk mengembalikan pesan bahwa data berhasil ditambahkan atau disimpan.

def simpan_file() befungsi untuk menyimpan data ke file JSON.

with open ("w") berfungsi untuk membuka file untuk menulis atau memperbarui data.

json.dump() berufungsi sebagai menyimpan data mahasiswa ke file JSON.

indent=4 berfungsi untuk membuat susunan data lebih rapi.

while True berfungsi membuat program terus berjalan sampai pengguna memilih keluar.

print() berfungsi menampilkan pilihan menu kepada pengguna.



<img width="783" height="449" alt="Screenshot 2026-10-08 170626" src="https://github.com/user-attachments/assets/710ac326-3de3-43ac-8f64-074ad5a3d646" />

input() berfungsi meminta pengguna memilih atau memasukan menu 1, 2, atau 3.

if pilihan == "1" menjalankan menu untuk melihat riwayat nilai mahasiswa.

print() untuk menampilkan data mahasiswa ke layar.

for mhs in data untuk mengambil dan menampilkan data mahasiswa satu per satu.

mhs["nama"] untuk mengambil nama mahasiswa.

mhs["nim"] untuk mengambil NIM mahasiswa.

mhs["mata_kuliah"] untuk mengambil mata kuliah mahasiswa.

mhs["nilai"] untuk mengambil nilai mahasiswa.

print("-" * 35) untuk membuat garis pemisah supaya data terlihat rapi.

elif pilihan == "2" berfungsi menjalankan menu tambah nilai mahasiswa baru.



<img width="779" height="452" alt="Screenshot 2026-10-08 170643" src="https://github.com/user-attachments/assets/a1f0c7bd-cbe2-465d-87e0-e5dc5886d1e5" />

input() untuk meminta pengguna memasukkan data mahasiswa.

nama, nim, mata_kuliah, nilai yang berfungsi sebagai Variabel untuk menampung data yang dimasukkan.

tambah_data() untuk Menambahkan data mahasiswa baru ke daftar.

simpan_file() untuk menyimpan data mahasiswa ke file JSON agar tidak hilang.

elif pilihan == "3" untuk menjalankan menu keluar.

print() untuk menampilkan pesan kepada pengguna.

break untuk menghentikan perulangan sehingga program selesai.

else untuk menangani pilihan menu yang tidak sesuai, misalnya selain angka 1, 2, atau 3.



<img width="788" height="92" alt="Screenshot 2026-10-08 170701" src="https://github.com/user-attachments/assets/cf11005d-6340-4624-8a8e-d398c99118fa" />

else dijalankan jika pengguna memilih selain menu 1, 2, atau 3.

print() untuk menampilkan pesan "Pilihan tidak valid! Silakan pilih menu 1, 2, atau 3."

while True untuk membuat menu utama muncul kembali sehingga pengguna bisa memilih ulang.



## 4. File Penyimpanan Data


<img width="776" height="449" alt="Screenshot 2026-10-08 144452" src="https://github.com/user-attachments/assets/21462a75-e6fb-44ad-85f9-9581f0e9dea7" />


<img width="769" height="449" alt="Screenshot 2026-10-08 144735" src="https://github.com/user-attachments/assets/d2dbd25e-d532-46c4-a360-ed2644cc176f" />

File JSON digunakan untuk menyimpan data yang telah dimasukkan
agar dapat dibaca kembali ketika program dijalankan ulang.

## 5. Penjelasan Kode Program
- **Variabel:** Menyimpan data yang diperlukan program.
- **Percabangan:** Menentukan tindakan berdasarkan kondisi.
- **Perulangan:** Menjalankan menu secara berulang.
- **Pengolahan data:** Menambah, menampilkan, mengubah,
  atau menghapus data sesuai fitur program.
- **Penyimpanan JSON:** Menyimpan dan membaca data agar
  tidak hilang ketika program ditutup.

## 6. Cara Menjalankan Program
Jalankan perintah berikut melalui terminal:

```bash
python main.py
```

## 7. Screenshot Hasil Program

### A. Output Program
Bukti bahwa program berhasil dijalankan.


<img width="761" height="203" alt="Screenshot 2026-10-08 144130" src="https://github.com/user-attachments/assets/cfe259ba-93a2-4dd4-b8e6-9815a991edf3" />

<img width="755" height="206" alt="Screenshot 2026-10-08 144203" src="https://github.com/user-attachments/assets/4471c424-b554-429e-be87-298ca9774b22" />

<img width="773" height="208" alt="Screenshot 2026-10-08 144232" src="https://github.com/user-attachments/assets/63e54f5c-20aa-4ad6-8398-8e782c3781e6" />

<img width="787" height="209" alt="Screenshot 2026-10-08 144253" src="https://github.com/user-attachments/assets/15b140de-1a35-4831-8d50-0a57ae903ace" />

<img width="770" height="212" alt="Screenshot 2026-10-08 144319" src="https://github.com/user-attachments/assets/443d353f-9689-48f8-b4f9-a555efe732d3" />

<img width="776" height="449" alt="Screenshot 2026-10-08 144452" src="https://github.com/user-attachments/assets/1feeeffa-be9d-4483-9f12-2a10dde33518" />

<img width="743" height="344" alt="Screenshot 2026-10-08 144515" src="https://github.com/user-attachments/assets/7fccf4c4-d7a8-4a86-bb1f-8972cd9d64be" />

<img width="760" height="206" alt="Screenshot 2026-10-08 144622" src="https://github.com/user-attachments/assets/7dc560e8-2beb-4653-8240-ea0f49b0d2c1" />

<img width="770" height="205" alt="Screenshot 2026-10-08 144701" src="https://github.com/user-attachments/assets/39c96b5c-6c8c-457a-a048-199303a838e0" />

<img width="769" height="449" alt="Screenshot 2026-10-08 144735" src="https://github.com/user-attachments/assets/8046f602-42c5-43c6-a4ce-b7ef76ad94d4" />


<img width="764" height="211" alt="Screenshot 2026-10-08 144714" src="https://github.com/user-attachments/assets/39fdec3d-465b-47dd-a784-6ca9251abb32" />


### B. Proses Menambahkan Data
Bukti bahwa data baru berhasil ditambahkan.

<img width="780" height="288" alt="Screenshot 2026-10-08 174829" src="https://github.com/user-attachments/assets/9d208596-e333-4947-9d9c-1630bca6505c" />

### C. Bukti Data Tetap Tersimpan
Bukti bahwa data tetap tersedia setelah program ditutup
dan dijalankan kembali.

<img width="776" height="190" alt="Screenshot 2026-10-08 175049" src="https://github.com/user-attachments/assets/076f4d06-09cd-4dc1-941f-87aae4807e9d" />


## 8. Kesimpulan
Program ini dibuat untuk menerapkan konsep dasar Python
dalam pengelolaan dan penyimpanan data menggunakan JSON.
Data yang telah disimpan dapat digunakan kembali ketika
program dijalankan ulang.

---
**Dokumentasi tugas Pemrograman Python.**

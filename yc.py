import json

with open("nilai_mahasiswa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(nama, nim, mata_kuliah, nilai):
    data.append({
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    })
    return "Data nilai berhasil ditambahkan!"

def simpan_file():
    with open("nilai_mahasiswa.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Data berhasil tersimpan!"

while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Lihat Riwayat Nilai Mahasiswa")
    print("2. Tambah Rekap Nilai Baru")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        print("\n===== DATA NILAI MAHASISWA =====")
        for mhs in data:
            print("Nama        :", mhs["nama"])
            print("NIM         :", mhs["nim"])
            print("mata_Kuliah :", mhs["mata_kuliah"])
            print("Nilai       :", mhs["nilai"])
            print("-" * 35)
    elif pilihan == "2":
        print("\n--- Tambah Data Nilai Baru ---")
        nama = input("Masukkan Nama Mahasiswa : ")
        nim = input("Masukkan NIM            : ")
        mata_kuliah = input("Masukkan Mata Kuliah    : ")
        nilai = input("Masukkan Nilai Ujian    : ")
        
        print(tambah_data(nama, nim, mata_kuliah, nilai))
        print(simpan_file())
    elif pilihan == "3":
        print("\nTerima kasih! semanggat coding nya ya teman teman ku.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1, 2, atau 3.")
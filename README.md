# Pertemuan 12 - File I/O dan Error Handling

## Identitas Mahasiswa
- Nama: Salsabila Thahira
- NIM: 2225250214
- Kelas: 3B

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Struktur Folder

```text
Pertemuan 12 - file - 2225250214/
├── README.md
├── Data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── Latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## Tujuan Pembelajaran
Pada pertemuan ini dilakukan praktik membaca dan menulis file menggunakan Python, memproses data teks, serta menangani error dasar menggunakan try-except.

## Format File Input
Format yang dipakai adalah:

```text
NIM,nilai
```

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

## Cara Menjalankan
Untuk menjalankan tugas utama, gunakan perintah:

```bash
python tugas/rekap_nilai_file.py
```

Untuk menjalankan latihan, gunakan perintah sesuai nama file, contohnya:

```bash
python Latihan/01_tulis_file.py
python Latihan/02_baca_file.py
python Latihan/03_append_file.py
python Latihan/04_proses_baris.py
python Latihan/05_file_not_found.py
python Latihan/06_value_error.py
```

## Error yang Ditangani
- `FileNotFoundError`
- `ValueError`

`FileNotFoundError` ditangani ketika file input tidak ditemukan.

`ValueError` ditangani ketika nilai tidak dapat dikonversi menjadi angka atau format baris tidak sesuai.

## Test Case

| No | Kondisi | Data/Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Normal | Semua data valid | Semua data diproses dan rekap berhasil dibuat | Jumlah data valid: 5, rata-rata: 83.40, minimum: 74.00, maksimum: 92.00, jumlah lulus: 5 | PASS |
| 2 | File hilang | `Data/nilai.txt` tidak tersedia | Menampilkan pesan file tidak ditemukan dan program tidak crash | File tidak ditemukan: `Data/nilai.txt` | PASS |
| 3 | Nilai invalid | `A004,abc` | Data invalid dilewati dan data lainnya tetap diproses | Baris 4 dilewati: `A004,abc` dan 5 data valid diproses | PASS |
| 4 | Baris kosong | Terdapat satu baris kosong pada file | Baris kosong dilewati tanpa menyebabkan error | Baris kosong dilewati dan data lainnya tetap diproses | PASS |
| 5 | Batas lulus | `A004,60` | Nilai 60 dihitung sebagai lulus | Jumlah lulus bertambah dan nilai 60 dihitung lulus | PASS |

## Refleksi
Error yang ditemukan adalah `ValueError` pada data `A004,abc`. Program mencoba mengubah nilai `abc` menjadi float, tetapi data tersebut bukan angka sehingga terjadi `ValueError`.

Error tersebut ditangani menggunakan `try-except`. Ketika `ValueError` terjadi, program menampilkan pesan bahwa baris tersebut dilewati. Dengan demikian, data yang valid tetap dapat diproses dan program tidak berhenti ketika menemukan satu data yang salah.

Selain itu, `FileNotFoundError` ditangani ketika file `Data/nilai.txt` tidak tersedia. Program menampilkan pesan bahwa file tidak ditemukan sehingga program tidak mengalami crash.
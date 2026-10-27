# Pertemuan 12 - File I/O dan Error Handling

# Identitas Mahasiswa
Nama: Salsabila Thahira
NIM: 2225250214
Kelas: 3B

# Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

# Struktur Folder

pertemuan-12-file-io-NIM/
├── README.md
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py

# Tujuan Pembelajaran

Pada pertemuan ini dilakukan praktik membaca dan menulis file menggunakan Python, memproses data teks, serta menangani error dasar menggunakan try-except.

# Format File Input

NIM,nilai

Contoh:

A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

# Cara Menjalankan

Untuk menjalankan Tugas 5, gunakan perintah:

python3 tugas/rekap_nilai_file.py

Untuk menjalankan latihan, gunakan perintah sesuai nama file, contohnya:

python3 latihan/01_tulis_file.py
python3 latihan/02_baca_file.py
python3 latihan/03_append_file.py
python3 latihan/04_proses_baris.py
python3 latihan/05_file_not_found.py
python3 latihan/06_value_error.py

## Error yang Ditangani

FileNotFoundError

ValueError

FileNotFoundError ditangani ketika file input tidak ditemukan.

ValueError ditangani ketika nilai tidak dapat dikonversi menjadi angka atau format baris tidak sesuai.

# Test case
<table>
    <thead>
        <tr>
            <th>No</th>
            <th>Kondisi</th>
            <th>Data/Input</th>
            <th>Hasil yang Diharapkan</th>
            <th>Hasil Aktual</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Normal</td>
            <td>Semua data valid</td>
            <td>Semua data diproses dan rekap berhasil dibuat</td>
            <td>Jumlah data valid: 5, rata-rata: 83.40, minimum: 74.00, maksimum: 92.00, jumlah lulus: 5</td>
            <td>PASS</td>
        </tr>
        <tr>
            <td>2</td>
            <td>File hilang</td>
            <td>data/nilai.txt tidak tersedia</td>
            <td>Menampilkan pesan file tidak ditemukan dan program tidak crash</td>
            <td>File tidak ditemukan: data/nilai.txt</td>
            <td>PASS</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Nilai invalid</td>
            <td>A004,abc</td>
            <td>Data invalid dilewati dan data lainnya tetap diproses</td>
            <td>Baris 4 dilewati: A004,abc dan 5 data valid diproses</td>
            <td>PASS</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Baris kosong</td>
            <td>Terdapat satu baris kosong pada file</td>
            <td>Baris kosong dilewati tanpa menyebabkan error</td>
            <td>Baris kosong dilewati dan data lainnya tetap diproses</td>
            <td>PASS</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Batas lulus</td>
            <td>A004,60</td>
            <td>Nilai 60 dihitung sebagai lulus</td>
            <td>Jumlah lulus bertambah dan nilai 60 dihitung lulus</td>
            <td>PASS</td>
        </tr>
    </tbody>
</table>

# Refleksi 
Error yang ditemukan adalah ValueError pada data A004,abc. Program mencoba mengubah nilai abc menjadi float, tetapi data tersebut bukan angka sehingga terjadi ValueError.

Error tersebut ditangani menggunakan try-except. Ketika ValueError terjadi, program menampilkan pesan bahwa baris tersebut dilewati. Dengan demikian, data yang valid tetap dapat diproses dan program tidak berhenti ketika menemukan satu data yang salah.

Selain itu, FileNotFoundError ditangani ketika file data/nilai.txt tidak tersedia. Program menampilkan pesan bahwa file tidak ditemukan sehingga program tidak mengalami crash.
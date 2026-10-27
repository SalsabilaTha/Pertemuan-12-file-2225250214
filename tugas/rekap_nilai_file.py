def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {len(nilai)}\n")
        file.write(f"Rata-rata: {sum(nilai) / len(nilai):.2f}\n")
        file.write(f"Minimum: {min(nilai):.2f}\n")
        file.write(f"Maksimum: {max(nilai):.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data:
    tulis_rekap(output_file, data)
    print(f"Rekap ditulis ke {output_file}")
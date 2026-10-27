with open("data/catatan.txt", "r", encoding="utf-8") as file:
 for baris in file:
    baris = baris.strip()

    if not baris or "," not in baris:
        continue

    nim, teks_nilai = baris.split(",")
    print(nim, float(teks_nilai))

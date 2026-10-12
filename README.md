# Kalkulator Nilai Mahasiswa — Unit Test dengan pytest

Mini program Python untuk tugas **Pertemuan 4 – Membuat Unit Test**.

## Fungsi yang diuji

| No | Fungsi | Deskripsi |
|----|--------|-----------|
| 1 | `hitung_rata_rata(nilai)` | Rata-rata dari daftar nilai (0–100) |
| 2 | `konversi_huruf(nilai)` | Konversi nilai angka ke huruf A–E |
| 3 | `cek_kelulusan(nilai, batas_lulus=55)` | Status LULUS / TIDAK LULUS |
| 4 | `hitung_nilai_akhir(tugas, uts, uas)` | Nilai akhir berbobot (30% / 30% / 40%) |

## Cara menjalankan

```bash
pip install -r requirements.txt

# jalankan program
python kalkulator_nilai.py

# jalankan unit test
pytest -v
```

## Struktur repository

```
.
├── kalkulator_nilai.py        # kode program
├── test_kalkulator_nilai.py   # unit test (pytest)
├── requirements.txt
└── README.md
```

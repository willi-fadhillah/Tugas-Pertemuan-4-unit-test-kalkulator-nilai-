"""Mini program: Kalkulator Nilai Mahasiswa.

Berisi 4 fungsi yang akan diuji dengan unit test:
1. hitung_rata_rata(nilai)      -> rata-rata dari daftar nilai
2. konversi_huruf(nilai)        -> konversi nilai angka ke nilai huruf
3. cek_kelulusan(nilai)         -> status lulus / tidak lulus
4. hitung_nilai_akhir(tugas, uts, uas) -> nilai akhir berbobot
"""


def hitung_rata_rata(nilai):
    """Mengembalikan rata-rata dari list angka (0-100).

    Raises:
        ValueError: jika list kosong atau ada nilai di luar 0-100.
    """
    if not nilai:
        raise ValueError("Daftar nilai tidak boleh kosong")
    for n in nilai:
        if n < 0 or n > 100:
            raise ValueError("Nilai harus berada di rentang 0-100")
    return sum(nilai) / len(nilai)


def konversi_huruf(nilai):
    """Mengonversi nilai angka (0-100) menjadi huruf A/B/C/D/E.

    A: >= 85, B: >= 70, C: >= 55, D: >= 40, E: < 40
    """
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus berada di rentang 0-100")
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 55:
        return "C"
    if nilai >= 40:
        return "D"
    return "E"


def cek_kelulusan(nilai, batas_lulus=55):
    """Mengembalikan 'LULUS' jika nilai >= batas_lulus, selain itu 'TIDAK LULUS'."""
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus berada di rentang 0-100")
    return "LULUS" if nilai >= batas_lulus else "TIDAK LULUS"


def hitung_nilai_akhir(tugas, uts, uas):
    """Nilai akhir berbobot: tugas 30%, UTS 30%, UAS 40%."""
    for n in (tugas, uts, uas):
        if n < 0 or n > 100:
            raise ValueError("Nilai harus berada di rentang 0-100")
    return round(tugas * 0.3 + uts * 0.3 + uas * 0.4, 2)


if __name__ == "__main__":
    daftar = [80, 90, 75]
    rata = hitung_rata_rata(daftar)
    print(f"Rata-rata : {rata:.2f}")
    print(f"Huruf     : {konversi_huruf(rata)}")
    print(f"Status    : {cek_kelulusan(rata)}")
    print(f"Nilai akhir (80, 70, 90): {hitung_nilai_akhir(80, 70, 90)}")

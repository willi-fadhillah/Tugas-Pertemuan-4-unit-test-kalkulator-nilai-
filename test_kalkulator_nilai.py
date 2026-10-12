import pytest

from kalkulator_nilai import (
    cek_kelulusan,
    hitung_nilai_akhir,
    hitung_rata_rata,
    konversi_huruf,
)


# ---------- Fungsi 1: hitung_rata_rata ----------
class TestHitungRataRata:
    def test_tc01_rata_rata_normal(self):
        assert hitung_rata_rata([80, 90, 70]) == 80

    def test_tc02_satu_nilai(self):
        assert hitung_rata_rata([75]) == 75

    def test_tc03_list_kosong_error(self):
        with pytest.raises(ValueError):
            hitung_rata_rata([])

    def test_tc04_nilai_di_luar_rentang_error(self):
        with pytest.raises(ValueError):
            hitung_rata_rata([80, 101])


# ---------- Fungsi 2: konversi_huruf ----------
class TestKonversiHuruf:
    @pytest.mark.parametrize(
        "nilai, expected",
        [
            (90, "A"),   # TC05
            (85, "A"),   # TC06 batas bawah A
            (84, "B"),   # TC07 tepat di bawah batas A
            (70, "B"),   # TC08 batas bawah B
            (55, "C"),   # TC09 batas bawah C
            (40, "D"),   # TC10 batas bawah D
            (39, "E"),   # TC11 tepat di bawah batas D
            (0, "E"),    # TC12 nilai minimum
        ],
    )
    def test_konversi_valid(self, nilai, expected):
        assert konversi_huruf(nilai) == expected

    def test_tc13_nilai_negatif_error(self):
        with pytest.raises(ValueError):
            konversi_huruf(-1)


# ---------- Fungsi 3: cek_kelulusan ----------
class TestCekKelulusan:
    def test_tc14_lulus(self):
        assert cek_kelulusan(80) == "LULUS"

    def test_tc15_tepat_batas_lulus(self):
        assert cek_kelulusan(55) == "LULUS"

    def test_tc16_tidak_lulus(self):
        assert cek_kelulusan(54) == "TIDAK LULUS"

    def test_tc17_batas_lulus_custom(self):
        assert cek_kelulusan(60, batas_lulus=65) == "TIDAK LULUS"

    def test_tc18_nilai_tidak_valid_error(self):
        with pytest.raises(ValueError):
            cek_kelulusan(150)


# ---------- Fungsi 4: hitung_nilai_akhir ----------
class TestHitungNilaiAkhir:
    def test_tc19_nilai_akhir_normal(self):
        # 80*0.3 + 70*0.3 + 90*0.4 = 24 + 21 + 36 = 81
        assert hitung_nilai_akhir(80, 70, 90) == 81

    def test_tc20_semua_nol(self):
        assert hitung_nilai_akhir(0, 0, 0) == 0

    def test_tc21_semua_seratus(self):
        assert hitung_nilai_akhir(100, 100, 100) == 100

    def test_tc22_nilai_negatif_error(self):
        with pytest.raises(ValueError):
            hitung_nilai_akhir(80, -5, 90)

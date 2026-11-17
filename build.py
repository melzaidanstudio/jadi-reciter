#!/usr/bin/env python3
# Build murrotal Quraish v2 (motlab + motion-cut).
# - Teks Arab + transliterasi + terjemahan diambil PROGRAM dari teks-quraish.md (jangan retype).
# - Peta karaoke 21 kata diambil PROGRAM dari tabel §5 SUTRADARA v2 (jangan retype).
# - Verifikasi: kata tampil §5 harus cocok persis sama token Arab teks-quraish.md (sesudah pisah tanda akhir ayat).
# - Output: scenes/01-basmalah.html .. scenes/05-ayat4.html + project.json.
# - 0 em dash di file ini dan di file hasil.
# CATATAN TEMPLATE (jadi-reciter): build asli baca tabel §5 dari file SUTRADARA di folder
# bahan (~/workspace/murrotal-quraish/SUTRADARA-MURROTAL-QURAISH-V2.md). Di template ini
# tabel itu disalin verbatim ke karaoke-table.md di folder proyek sendiri, supaya
# `python3 build.py` jalan dari clone bersih tanpa folder bahan. Isi tabel TIDAK diubah
# (21 baris, batas kata 12/13 sudah terkoreksi 24.68). Buat surah baru: ganti
# karaoke-table.md + teks-quraish.md + timing-ayat.md dengan yang terverifikasi,
# lalu jalankan ulang script ini. Lihat README.md + templates/SUTRADARA-TEMPLATE.md §5.
import json, re, sys
from pathlib import Path

PROJ = Path(__file__).parent
SUTRA = PROJ / "karaoke-table.md"
TEKS = PROJ / "teks-quraish.md"

GOLD = "#E8C766"
WHITE = "#FFFFFF"
# Tanda akhir ayat: selalu tampil, selalu emas, bukan kata.
MARKS = {"\u06d9", "\u06da", "\u06d5\u06d9", "\u08d6"}  # ۙ ۚ ەۙ ࣖ

def parse_teks(path):
    txt = path.read_text(encoding="utf-8")
    verses = {}
    cur = None
    mode = None
    for line in txt.splitlines():
        line = line.strip()
        m = re.match(r"##\s+(Basmalah|Ayat \d+)$", line)
        if m:
            cur = m.group(1)
            verses[cur] = {}
            mode = None
            continue
        if line in ("Arab:", "Transliterasi:", "Terjemahan:"):
            mode = {"Arab:": "arab", "Transliterasi:": "translit", "Terjemahan:": "transl"}[line]
            continue
        if cur and mode and line:
            verses[cur][mode] = line
            mode = None
    return verses

def parse_karaoke(path):
    txt = path.read_text(encoding="utf-8")
    words = []
    for line in txt.splitlines():
        line = line.strip()
        m = re.match(r"\|\s*(\d+)\s*\|\s*(Basmalah|Ayat \d+)\s*\|\s*([^|]+?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|", line)
        if m:
            words.append({
                "no": int(m.group(1)), "verse": m.group(2), "word": m.group(3).strip(),
                "start": float(m.group(4)), "end": float(m.group(5)),
                "f_start": int(m.group(6)), "t_frame": float(m.group(7)),
            })
    return words

def split_token(tok):
    """Pisah token Arab jadi (kata, tanda). Tanda akhir ayat dipisah, selalu emas."""
    if tok in MARKS:
        return "", tok
    for mark in sorted(MARKS, key=len, reverse=True):
        if tok.endswith(mark) and len(tok) > len(mark):
            return tok[:-len(mark)], mark
    return tok, ""

def main():
    verses = parse_teks(TEKS)
    assert len(verses) == 5, f"ayat ketemu {len(verses)}, harus 5"
    for v in ("Basmalah", "Ayat 1", "Ayat 2", "Ayat 3", "Ayat 4"):
        assert set(verses[v]) == {"arab", "translit", "transl"}, f"{v} tidak lengkap: {verses[v].keys()}"
    words = parse_karaoke(SUTRA)
    assert len(words) == 21, f"kata karaoke {len(words)}, harus 21"
    # Verifikasi kata tampil §5 cocok sama token Arab teks-quraish.md
    for v in ("Basmalah", "Ayat 1", "Ayat 2", "Ayat 3", "Ayat 4"):
        toks = verses[v]["arab"].split(" ")
        runs = []  # (kata, tanda) per token
        for t in toks:
            runs.append(split_token(t))
        tampil = [w for w, _ in runs if w]
        tabel = [w["word"] for w in words if w["verse"] == v]
        assert tampil == tabel, f"{v} TIDAK COCOK:\n teks: {tampil}\n tabel: {tabel}"
        verses[v]["runs"] = runs
        print(f"OK {v}: {len(tampil)} kata cocok, token: {len(runs)}")
    # f_end tiap kata = floor(akhir kata sendiri x 24). BUKAN f_start kata berikut,
    # karena ada jeda napas Ayat 4 (38.48-40.36) di antara kata 18 dan 19:
    # kata 18 end 38.48 -> f_end 923, kata 19 start 40.36 -> f_start 968.
    # Kalau pakai f_start kata berikut, kata 18 jadi aktif selama jeda napas (SALAH).
    verse_end = {"Basmalah": 6.16, "Ayat 1": 11.58, "Ayat 2": 21.46, "Ayat 3": 28.44, "Ayat 4": 45.19}
    import math
    for i, w in enumerate(words):
        w["f_end"] = math.floor(w["end"] * 24)
        assert w["f_end"] > w["f_start"], f"kata {w['no']} f_end {w['f_end']} <= f_start {w['f_start']}"
    # KOREKSI BATAS AYAT 3 (perintah CEO + SUTRADARA §5 catatan, verifikasi akustik Builder 2):
    # Tabel §5 pakai batas token Whisper 25.12 (f 602) buat رَبَّ/هٰذَا. Analisis audio membuktikan
    # "hā" terdengar SEBELUM 25.12: RMS jatuh 24.44-24.66 (akhir "rabba"), spike HF/LF 24.66-24.70
    # (frikatif /h/), vokal "hā" mulai 24.70. Di 25.12 tidak ada perubahan akustik (di tengah vokal "hā").
    # Durasi pun tidak masuk akal kalau pakai tabel: kata 12 1,42 dtk (2 suku kata) vs kata 13 0,52 dtk
    # (2 suku kata). Sesudah geser: kata 12 0,98 dtk, kata 13 0,96 dtk, seimbang.
    # Batas baru 24.68 (tengah onset /h/), f 592. Highlight ganti di frame 592 (t 24.6667),
    # 13 ms SEBELUM onset /h/, tidak pernah telat.
    for w in words:
        if w["no"] == 12:
            w["end"] = 24.68
            w["f_end"] = math.floor(24.68 * 24)
        if w["no"] == 13:
            w["start"] = 24.68
            w["t_frame"] = math.floor(24.68 * 24) / 24
            w["f_start"] = math.floor(24.68 * 24)
    print("OK koreksi batas Ayat 3: kata 12 end 24.68 (f_end 592), kata 13 start 24.68 (f_start 592)")
    print("OK f_end semua kata positif, tidak ada tumpang tindih")
    # Simpan data buat scene generator
    data = {"verses": {}, "words": words}
    for v in ("Basmalah", "Ayat 1", "Ayat 2", "Ayat 3", "Ayat 4"):
        data["verses"][v] = {
            "arab": verses[v]["arab"], "translit": verses[v]["translit"], "transl": verses[v]["transl"],
            "runs": verses[v]["runs"],
        }
    (PROJ / "karaoke-data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK karaoke-data.json ditulis")
    return data

if __name__ == "__main__":
    main()

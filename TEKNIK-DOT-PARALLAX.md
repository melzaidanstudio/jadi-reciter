# SPEC TEKNIK: DOT, PARALLAX, Template Jadi-Reciter
# VideoStory, 2026-11-18 ~00:52 WIB
# Perintah Bos via CEO 2026-11-18 ~00:48 WIB. Spec teknik buat repo template jadi-reciter.
# Basis: proyek Quraish v2 motlab + motion-cut (~/workspace/murrotal-quraish-v2-motlab/).
# Repo jadi-reciter (~/workspace/jadi-reciter/) BELUM ADA saat spec ini ditulis (dicek 00:52 WIB, folder tidak ditemukan); Builder 2 yang bangun repo-nya.
# Spec ini file sendiri, jangan edit folder repo Builder 2 langsung.
# REVISI NO-KABUR 2026-11-18 (perintah Bos, Dewa): efek kabur DIHAPUS total dari spec
# ini. File spec lama diganti file ini. Transisi D1 + D4 yang
# dulu pakai efek kabur jadi cross-dissolve biasa (fade). DOT + PARALLAX tidak berubah.

## 0. Konteks + aturan dasar
- Template: video murrotal (Qur'an) dari Quraish v2 motlab + motion-cut. Engine motlab, output 720x1280 24fps, halaman 1080x1920, render --scale 0.6667.
- 5 adegan contoh: Basmalah + Ayat 1-4 (lihat tabel §4). SUTRADARA acuan: SUTRADARA-MURROTAL-QURAISH-V2.md (md5 7ebee301, 152 baris, di RENDER.md v2). Teknik di bawah ini adalah ADDENDUM ke SUTRADARA itu (pasal baru §16), bukan ganti SUTRADARA.
- Dua teknik: DOT (§1), PARALLAX (§2). Semuanya jalan di motlab + Chrome render, deterministik (tanpa Math.random, tanpa Date.now, cuma fungsi t + hash tetap), tidak nutupin teks karaoke, tidak bikin gambar utama kabur.
- Semua angka dalam piksel HALAMAN 1080x1920, kecuali disebut lain. Output 720x1280 = halaman x 0.6667 (angka output = angka halaman x 2/3).
- Urutan gambar per frame (dari belakang ke depan): (1) gambar tajam + Ken Burns + pan, (2) pola DOT, (3) partikel, (4) shadow box + pill + teks, (5) fade hitam ekor (Ayat 4 saja).

## 1. DOT: pola titik overlay di gambar
### 1.1 Tujuan
- Tekstur cetak (halftone) yang menyatukan 5 gambar berbeda jadi satu identitas visual template. Subtle, tidak bersaing sama gambar atau teks.
- BUKAN bintang herwanto (itu partikel acak jarang, §2 lapis 2). DOT adalah grid teratur rapat (ribuan titik), tekstur, bukan suasana.
### 1.2 Angka pasti
- Diameter titik: 3 px (halaman), jadi 2 px di output 720x1280.
- Jarak grid: 24 px horizontal + 24 px vertikal (halaman), jadi 16 px di output.
- Baris ganjil geser 12 px ke kanan (stagger, pola sarang lebah).
- Warna: putih #FFFFFF, opacity 0.06 (6%).
- Bentuk: lingkaran (arc, radius 1.5 px). Pengganti yang dibolehkan kalau render lambat: kotak 3x3 px (fillRect).
- Jumlah: 1080/24 = 45 kolom, 1920/24 = 80 baris, total ~3.600 titik per frame. Yang kelihatan ~3.000 (sisanya ketutup shadow box + pill).
### 1.3 Area
- Kena: SELURUH frame (0-1080 x 0-1920), di atas gambar, di bawah shadow box + pill + teks.
- Tidak kena (tertutup, bukan dihapus): area shadow box (x 60-1020, y atas kotak sampai 1731) + area pill (y 60-112). Shadow box (hitam 0.55) + pill menutupi titik di area teks, jadi titik TIDAK PERNAH menyentuh teks karaoke.
- DOT ikut lapis gambar (lapis 1, §2): titik bergerak + membesar ikut Ken Burns zoom + pan gambar. Titik adalah tekstur DI gambar, bukan lapis sendiri.
### 1.4 Implementasi (motlab, canvas 2D)
- Gambar titik sesudah gambar latar, sebelum partikel + teks.
- Terapkan transform Ken Burns yang sama kayak gambar (translate + scale + pan), lalu gambar grid titik.
- Grid tetap (tanpa random, tanpa hash). Titik dihitung dari koordinat grid, bukan dari posisi acak.
- 3.600 arc per frame: cepat di Chrome (di bawah 5 ms). Kalau mau lebih cepat, pakai fillRect 3x3.
### 1.5 Verifikasi (angka + cara ukur)
- Hitung titik di still: ambil still adegan, threshold area gambar (di luar shadow box + pill) buat piksel titik putih; harap ~3.000 titik kelihatan (toleransi +-10%).
- Diameter titik: ukur satu titik di still output (720x1280): harap 2 px (toleransi +-1 px).
- Opacity: sampling piksel titik vs piksel latar sebelahnya; selisih terang harap ~6% dari rentang latar-ke-putih (toleransi 0.04-0.08). Di latar terang selisih absolut kecil, itu normal (titik memang subtle).
- Tidak ada titik di teks: cek baris Arab di still; tidak ada artefak pola titik di dalam huruf (shadow box menutupi semua titik di area teks).
- Titik bergerak ikut gambar: bandingkan dua still satu adegan (beda waktu); posisi titik bergeser ikut pan + zoom gambar (bukan diam).

## 2. PARALLAX: gerak berlapis (adaptasi Insyirah §8)
### 2.1 Tujuan + beda sama Ken Burns biasa
- Ken Burns biasa (Quraish v2 sekarang): cuma zoom-in linear di tengah, semua elemen bergerak bersamaan. Tidak ada rasa kedalaman.
- Parallax 3 lapis semu (template ini): tiga lapis bergerak BEDA kecepatan + BEDA arah, jadi ada rasa kedalaman. Gambar datar tidak bisa dukung parallax oklusi sejati (latar depan menutupi latar belakang saat bergerak beda kecepatan), jadi yang dipakai adalah parallax semu (tanpa oklusi), sama kayak Insyirah §8.
- Template ini TIDAK pakai grid herwanto (itu elemen gaya herwanto, bukan motion-cut) dan TIDAK pakai grade navy/vignette herwanto (gambar Quraish sudah gelap emas). Lapis tengah template ini adalah PARTIKEL (bukan bintang + grid).
### 2.2 Tiga lapis + angka pasti
- LAPIS 1 (belakang, gambar + DOT): Ken Burns zoom-in (KB_END per adegan, §2.3) + pan linear 20 px (halaman) sepanjang adegan, arah per adegan (§2.3). Kecepatan acuan 1,0x. Lapis paling lambat (paling jauh dari kamera). DOT ikut lapis ini (§1.3).
- LAPIS 2 (tengah, partikel): partikel per adegan (rays/dusk/snow/night/oasis, ikut SUTRADARA §7) + drift BERLAWANAN arah pan gambar, 30 px linear sepanjang adegan (kecepatan 1,5x gambar). Gerak asli partikel (salju jatuh, debu melayang, sinar berkilau) TETAP, drift parallax adalah offset tambahan: partikelX += -1,5 x panX(t), partikelY += -1,5 x panY(t).
- LAPIS 3 (depan, blok teks): shadow box + pill + teks (Arab + transliterasi + terjemahan) drift sinusoidal BERLAWANAN arah pan gambar, amplitudo 15 px (halaman), satu siklus penuh per adegan (mulai 0, puncak -15 px di tengah adegan, kembali 0 di akhir adegan). Kecepatan nominal 2,0x gambar (lapis paling cepat, paling dekat ke kamera). Rumus: dx = -15 x sin(2 x PI x t / TOTAL) x PAN_DIR_X, dy = -15 x sin(2 x PI x t / TOTAL) x PAN_DIR_Y.
- Drift teks TIDAK BOLEH ganggu keterbacaan Arab: amplitudo maks 15 px, sinusoidal halus, tanpa goyangan (wobble) berlebihan, arah konsisten per adegan (tidak bolak-balik acak). Teks kembali ke posisi netral di akhir adegan (sinus penuh), jadi tidak ada lompatan di batas adegan (dissolve).
- Tidak ada elemen statis: gambar (zoom + pan), DOT (ikut gambar), partikel (drift + gerak asli), teks (sinusoidal). Perintah Bos "semua bergerak" terpenuhi. Tidak ada grade tambahan di template ini (gambar Quraish sudah final).
### 2.3 Arah + zoom per adegan (5 adegan Quraish)
| Adegan | Gambar | Zoom (KB_END) | Pan (20 px, linear) | Partikel drift (30 px, berlawanan) | Teks drift (±15 px, sinusoidal, berlawanan) |
|---|---|---|---|---|---|
| Basmalah | Ka'bah, sinar emas dari atas | 1.3 | ATAS (0,-1), ke arah cahaya | BAWAH, 30 px | BAWAH, sinusoidal |
| Ayat 1 | Kafilah gurun, senja | 1.3 | KANAN (1,0), ikut perjalanan | KIRI, 30 px | KIRI, sinusoidal |
| Ayat 2 | Celah gunung bersalju, dingin | 1.3 | KIRI (-1,0), lawan angin dingin | KANAN, 30 px | KANAN, sinusoidal |
| Ayat 3 | Ka'bah malam, bintang | 1.3 | KANAN (1,0), ikut bintang | KIRI, 30 px | KIRI, sinusoidal |
| Ayat 4 | Oasis, sungai, senja | 1.3 | ATAS (0,-1), ke arah senja/harapan | BAWAH, 30 px | BAWAH, sinusoidal |
- Busur arah: ATAS, KANAN, KIRI, KANAN, ATAS. Adegan berurutan tidak pakai arah sama dua kali berturut-turut (Ayat 1 + Ayat 3 sama-sama KANAN, tapi dipisah Ayat 2 KIRI).
- Aturan buat surah lain (template umum): pan ke arah sumber cahaya ATAU arah gerak subjek (kafilah, sungai, angin). Kalau tidak jelas, default KANAN. Zoom semua adegan 1.3, tidak ikut durasi lagi (perintah Bos 2026-11-18 ~00:55 WIB).
- CATATAN GATE (zoom 1.3, perintah Bos 2026-11-18 ~00:55 WIB): 1.3 jauh lebih kuat dari 1.03-1.05 (zoom 30%, bukan 3-5%). Di zoom maks, area gambar yang kelihatan cuma 1080/1.3 = 831 px lebar x 1920/1.3 = 1477 px tinggi dari gambar asli, jadi ~11.5% per sisi di keempat sisi (total ~23% per dimensi) terpotong. Builder 2 WAJIB cek dampak framing/crop per adegan di preview (bagian gambar mana yang terpotong di zoom maks, subjek utama masih di frame atau tidak: Ka'bah di Basmalah + Ayat 3, kafilah di Ayat 1, celah gunung di Ayat 2, oasis + sungai di Ayat 4). Kalau subjek utama terpotong, laporkan ke VideoStory. Jangan ubah nilainya, nilai tetap 1.3 perintah Bos; yang dicek cuma dampaknya, solusinya diputuskan sesudah lihat preview.
### 2.4 Implementasi (motlab, canvas 2D)
- Pan gambar: translate(W/2 + panX, H/2 + panY), scale(z), translate(-W/2, -H/2). panX = PAN_DIR_X x 20 x clamp(t/TOTAL), panY = PAN_DIR_Y x 20 x clamp(t/TOTAL). z = 1 + (KB_END - 1) x clamp(t/TOTAL).
- Drift partikel: tambahkan offset -1,5 x (panX, panY) ke posisi tiap partikel (sebelum gambar partikel).
- Drift teks: tambahkan (dx, dy) sinusoidal ke posisi shadow box + pill + teks (dx, dy ikut rumus §2.2). Pill + shadow box + teks bergerak BERSAMA sebagai satu lapis (jangan drift terpisah).
- Semua gerak deterministik (cuma fungsi t + hash tetap, tanpa Math.random, tanpa Date.now). Stills + render harus sama.
- VT_OFFSET (pelajaran Quraish v2): karaoke + timestamp pakai VT_OFFSET = ceil(SCENE_START x 24)/24 - SCENE_START. Drift teks TIDAK pakai VT_OFFSET (drift adalah gerak visual, bukan penanda waktu).
### 2.5 Verifikasi (angka + cara ukur)
- Pan gambar: bandingkan dua still satu adegan (beda waktu, misal awal vs akhir); fitur gambar yang sama bergeser ~20 px x (delta t / TOTAL) ke arah pan (toleransi +-5 px). Ukur dari piksel fitur yang jelas (misal menara Ka'bah, puncak gunung).
- Zoom: bandingkan skala fitur gambar di frame awal vs akhir adegan; harap zoom 1.3x (toleransi +-0.01).
- Drift partikel: bandingkan posisi partikel di dua still; partikel bergeser BERLAWANAN arah pan gambar, ~30 px x (delta t / TOTAL) (toleransi +-8 px).
- Drift teks: ukur posisi shadow box / baris Arab (centroid) di dua still (awal vs tengah adegan); harap geser ~15 px ke arah berlawanan pan di tengah adegan, kembali ~0 di akhir adegan (toleransi +-5 px).
- Tidak ada elemen statis: MAD (mean absolute difference) antar frame berurutan di tiap adegan harap >0 di semua zona (gambar, partikel, teks). Kalau ada zona yang MAD = 0, ada elemen yang diam, gagal.
- Keterbacaan: Arab tetap tajam di semua frame (teks tidak goyang). Cek lebar stroke huruf Arab di still: harap 1-2 px (sama kayak tanpa drift).

## 3. TRANSISI antar adegan (motion-cut)
- D1 Basmalah ke Ayat 1 (video 6,61-7,11): fade (cross-dissolve), duration 0.5, ease inOutCubic. Blend lembut, alir mengalir.
- D2 Ayat 1 ke Ayat 2 (video 11,64-12,14): directionalwarp, duration 0.5, ease inOutCubic, params direction [-1, 1]. Warp diagonal. Pindah tempat jauh (gurun ke gunung).
- D3 Ayat 2 ke Ayat 3 (video 21,48-21,98): fadecolor, duration 0.5, ease inOutCubic, params color [0,0,0] hitam, colorPhase 0.4. Dip ke hitam (lompat waktu + babak baru).
- D4 Ayat 3 ke Ayat 4 (video 28,69-29,19): fade (cross-dissolve), duration 0.5, ease inOutCubic. Blend lembut, alir mengalir.
- D1 + D4 dulu pakai transisi efek kabur; diganti fade per perintah Bos 2026-11-18 (no-kabur). D2 + D3 tidak berubah.
- Semua transisi ditulis di project.json di adegan yang DIMASUKI (bukan yang ditinggalkan), ikut SUTRADARA §8 + §10.
### 3.1 Verifikasi (angka + cara ukur)
- Transisi: cek frame tengah tiap transisi (D1 f164, D2 f285, D3 f521, D4 f694): D1 + D4 harap blend lembut (cross-dissolve, bukan hard cut), D2 harap warp diagonal, D3 harap gelap (dip hitam). Frame-diff penuh: 0 hard cut di luar jendela transisi (ikut RENDER.md v2: median mean 0,208, maks di luar transisi di bawah 20).
- Gambar utama tajam: ukur lebar tepi detail gambar di still; harap 1-2 px (tajam). Kalau tepi gambar kabur di mana pun, ada yang salah, gagal.
- Teks tajam: ukur lebar stroke huruf Arab di still; harap 1-2 px (tajam). Kalau stroke Arab kabur, ada yang salah di urutan gambar, gagal.
- Transisi tidak ganggu karaoke: kata aktif putih di frame yang benar (ikut peta karaoke SUTRADARA §5), tidak telat, tidak salah kata.

## 4. Tabel per adegan (5 adegan Quraish, semua teknik)
| Adegan | TOTAL | DOT | PARALLAX (pan 20 px + zoom) | Transisi (masuk) |
|---|---|---|---|---|
| Basmalah | 7.11 dtk | 3 px / 24 px / putih 0.06 | ATAS, zoom 1.3 | - (adegan pertama) |
| Ayat 1 | 5.53 dtk | sama | KANAN, zoom 1.3 | D1 fade 0.5 |
| Ayat 2 | 10.34 dtk | sama | KIRI, zoom 1.3 | D2 directionalwarp [-1,1] |
| Ayat 3 | 7.71 dtk | sama | KANAN, zoom 1.3 | D3 fadecolor hitam 0.4 |
| Ayat 4 | 19.03 dtk | sama | ATAS, zoom 1.3 | D4 fade 0.5 |
- Partikel per adegan (lapis 2, drift 30 px berlawanan pan): Basmalah rays, Ayat 1 dusk, Ayat 2 snow, Ayat 3 night, Ayat 4 oasis (ikut SUTRADARA §7).
- Teks drift (lapis 3, ±15 px sinusoidal berlawanan pan): semua adegan sama.
- SUTRADARA yang diterapin: SUTRADARA-MURROTAL-QURAISH-V2.md (motlab + motion-cut). Teknik ini addendum §16 ke SUTRADARA itu. Buat surah lain, SUTRADARA-nya diganti (teks + timing + gambar baru), tapi angka DOT/PARALLAX di spec ini TETAP (cuma arah pan yang disesuaikan per gambar, ikut aturan §2.3 (zoom tetap 1.3 semua adegan)).

## 5. Konflik + prioritas (mana yang menang, kenapa)
1. PARALLAX vs DOT: DOT ikut gambar (lapis 1), teks bergerak sendiri (lapis 3). Tidak ada konflik; titik tidak pernah menyentuh teks karena shadow box menutupi.
2. DOT vs karaoke: TEKS menang (shadow box menutupi titik di area teks). Titik tidak pernah di atas teks.
3. Gambar vs teks: TEKS menang (shadow box hitam 0.55 di atas gambar di area teks, teks putih di atasnya). Gambar utama tetap tajam di luar kotak.

## 6. Checklist verifikasi (buat VideoStory + GATE, angka + cara ukur)
- [ ] DOT: ~3.000 titik kelihatan di still, diameter 2 px (output), opacity 0.04-0.08, tidak ada titik di teks, titik bergerak ikut gambar.
- [ ] PARALLAX: pan gambar ~20 px per adegan ke arah tabel, zoom 1.3, partikel drift ~30 px berlawanan, teks drift ±15 px sinusoidal kembali 0 di akhir adegan, tidak ada elemen statis (MAD >0 semua zona).
- [ ] Zoom 1.3 framing/crop: cek per adegan di preview, subjek utama masih di frame di zoom maks (Ka'bah, kafilah, celah gunung, oasis + sungai). Kalau terpotong, laporkan ke VideoStory, jangan ubah nilai 1.3.
- [ ] Transisi: D1 + D4 blend lembut (fade), D2 warp diagonal, D3 dip hitam, 0 hard cut di luar transisi.
- [ ] Karaoke: kata aktif putih di frame yang benar (peta SUTRADARA §5), tidak telat, tidak salah kata, jeda napas Ayat 4 tidak ada kata aktif.
- [ ] Shadow box rapi, tidak tutupi pill. Pill ikut fade teks. Tanpa footer di frame mana pun.
- [ ] Deterministik: stills + render sama (bandingkan still preview vs frame MP4 di waktu yang sama; harus identik).
- [ ] Render time: catat waktu build + render (perintah Bos).

## 7. README (teks siap tempel, buat Builder 2 masukin ke README template)
---
### Efek visual template: DOT, PARALLAX

Template ini pakai dua efek visual yang sama di semua video, supaya semua surah kelihatan satu keluarga:

**DOT (pola titik).** Grid titik putih halus di atas gambar (diameter 3 px, jarak 24 px, baris ganjil geser 12 px, opacity 6%). Tekstur cetak yang menyatukan gambar-gambar beda gaya. Titik tidak pernah menutupi teks (kotak teks menutupinya).

**PARALLAX (gerak berlapis).** Tiga lapis bergerak beda kecepatan + beda arah: gambar (zoom 30% + pan 20 px), partikel (drift 30 px berlawanan arah gambar), teks (goyang halus 15 px berlawanan arah gambar). Hasilnya ada rasa kedalaman, dan tidak ada elemen yang diam di layar. Arah pan disesuaikan per gambar (ke arah cahaya atau arah gerak subjek).

Semua efek deterministik (hasil render selalu sama), tidak menutupi teks karaoke, dan tidak mengaburkan gambar utama. Detail angka lengkap ada di `TEKNIK-DOT-PARALLAX.md`.
---

## 8. Catatan implementasi (motlab + Chrome)
- Canvas 2D, gambar tajam di semua zona (tanpa efek kabur di mana pun).
- DOT: gambar sesudah gambar latar, sebelum partikel. Pakai transform Ken Burns yang sama kayak gambar (titik ikut zoom + pan).
- Partikel: offset drift parallax ditambahkan ke posisi partikel (bukan ke transform canvas), supaya gerak asli partikel (jatuh, melayang) tetap jalan.
- Teks: drift sinusoidal ditambahkan ke posisi shadow box + pill + teks (satu offset dx, dy buat ketiganya).
- Jangan pakai Math.random atau Date.now di scene manapun (aturan motlab). Posisi partikel + DOT dari grid tetap / hash tetap (fungsi hash di gen_scenes.py sudah ada: `hash = n => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); }`).
- VT_OFFSET tetap dipakai buat karaoke + timestamp (pelajaran Quraish v2). Drift teks tidak pakai VT_OFFSET.
- Kalau Builder 2 mau ganti angka (misal amplitudo drift), yang boleh diubah cuma angka di tabel §4, dan harus dicatat di RENDER.md + di-score ulang sama VideoStory. Jangan ubah struktur lapis (urutan gambar) tanpa acc VideoStory.

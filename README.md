# Jadi-Reciter

Template workflow video murrotal (Qur'an) dari build nyata QS. Quraish (106) v2,
motlab + motion-cut. Clone repo ini, ganti audio + teks + gambar dengan surah
yang kamu mau, build, preview, render, verifikasi. Output: video vertikal
720x1280, 24fps, karaoke per kata Arab, shadow box, tanpa footer, transisi
bernama motion-cut.

Contoh lengkap yang disertakan: QS. Quraish (106) v2, 47,717 detik, 21 kata
karaoke, 5 gambar, 5 adegan. Build asli: 10 menit 11 detik, render 2 menit
11 detik, total 12 menit 22 detik. Video contoh sudah di-score 10/10
(VideoStory + CEO) sebelum bug ARAB_LINES ditemukan dan di-fix (lihat
`templates/RENDER-TEMPLATE.md`).

## Syarat install (prerequisite, TIDAK masuk repo)

Motlab TIDAK di-fork dan TIDAK ikut masuk repo ini. Motlab adalah syarat
install, sama seperti alat lain di bawah. Install semuanya dulu sebelum
quickstart:

- **motlab** (video engine, scene-as-code). Repo: `staryone/motlab` (MIT).
  Install ikut petunjuk repo itu (`node install.js`, perintah `motlab` masuk
  PATH). Cek dengan `motlab doctor`. Repo ini cuma pakai motlab, tidak
  mengubahnya.
- **Node 24** (motlab jalan di Node 24).
- **Chrome for Testing** (motlab render pakai headless Chrome). Set env
  `CHROME` ke path Chrome kamu kalau motlab tidak menemukannya. Di mesin
  yang butuh `--no-sandbox`, bungkus Chrome dengan wrapper yang menambahkan
  flag itu.
- **ffmpeg** (render audio, verifikasi: ffprobe, volumedetect, blackdetect,
  ekstraksi frame). Cek dengan `ffmpeg -version`.
- **Whisper small + faster-whisper** (`pip install openai-whisper
  faster-whisper`). Dipakai buat transkrip rekaman + bangun timing ayat
  saat bikin surah BARU. Contoh Quraish di repo ini sudah bawa transkrip +
  timing terverifikasi, jadi Whisper tidak dibutuhkan buat jalanin contohnya.
- **Python 3 + Pillow** (`pip install pillow`). Python buat `build.py` +
  `gen_scenes.py`; Pillow buat contact sheet preview + cek frame.
- **Font Arab Noto Naskh** (Noto Naskh Arabic Regular + SemiBold) dan
  **Noto Sans** (Regular + SemiBold). Font sudah di-vendor di
  `assets/fonts/` repo ini, jadi tidak perlu install font di sistem buat
  jalanin contoh. Kalau bikin surah baru, pakai font yang sama.

Ruang disk: render butuh folder sementara. Jangan pakai `/tmp` kalau
`/tmp` kamu kecil (di VM contoh cuma 512 MB). Pakai `TMPDIR=$PWD/.tmp`
di folder proyek (sudah ada di perintah quickstart di bawah).

## Quickstart (dari clone bersih)

Semua perintah dari folder repo. Ganti `<...>` dengan punyamu.

```
# 0. Clone + masuk folder
git clone <URL repo ini>
cd jadi-reciter

# 1. Isi audio (WWAJIB, repo tidak bawa audio, lihat audio/README.md)
#    Taruh satu file WAV rekaman murrotal di audio/audio.wav.
#    Contoh Quraish: Ridjaal Ahmed, 47,717 detik, md5 7efb314b917618acc3103bf5eba56797.

# 2. Bangun peta karaoke dari teks + tabel (baca karaoke-table.md + teks-quraish.md)
python3 build.py
#    Cek: karaoke-data.json tertulis, 21 kata, semua assert lolos.
#    Kalau ganti surah, ganti dulu teks-quraish.md + karaoke-table.md + timing-ayat.md.

# 3. Generate adegan + project.json (baca karaoke-data.json)
python3 gen_scenes.py
#    Cek: 5 file scenes/*.html + project.json tertulis.
#    Cek gerbang kata terakhir: grep -c "خَوْفٍ" scenes/05-ayat4.html HARUS 1.
#    Kalau 0, JANGAN render (lihat Pelajaran: ARAB_LINES di bawah).

# 4. Preview (WAJIB sebelum render penuh): stills per adegan + transisi
export PATH="$HOME/.local/bin:$PATH"
export CHROME="$HOME/.local/bin/google-chrome"
export TMPDIR="$HOME/.motlab-tmp"
mkdir -p .tmp preview
motlab stills scenes/01-basmalah.html preview/s1 2.63 --scale 0.6667 --format jpg
motlab stills scenes/02-ayat1.html preview/s2 2.89 --scale 0.6667 --format jpg
motlab stills scenes/03-ayat2.html preview/s3 5.36 --scale 0.6667 --format jpg
motlab stills scenes/04-ayat3.html preview/s4 3.52 --scale 0.6667 --format jpg
motlab stills scenes/05-ayat4.html preview/s5 13.31 10.81 0.25 17.81 19.01 --scale 0.6667 --format jpg
#    Baca semua still ukuran penuh. Yang dicek: kata aktif PUTIH di frame yang
#    benar, shadow box rapi + tidak tutupi pill, Arab 2 baris Ayat 4 tidak
#    meluber, terjemahan maks 2 baris, tanpa footer, gambar per ayat benar,
#    zoom 1.3 + pan jalan, DOT kelihatan, blur latar cuma di zona teks.
#    Waktu stills lengkap (12 titik, waktu video): lihat templates/SUTRADARA-TEMPLATE.md §11.
#    Kalau preview ada yang salah, betulkan dulu, stills ulang, baru render.

# 5. Render penuh (720x1280, 24fps)
TMPDIR=$PWD/.tmp motlab render . out/murrotal-quraish-v2-motlab.mp4 --scale 0.6667
#    Output: out/*.mp4, 720x1280, 24fps, 1.146 frame, 47,75 detik.

# 6. Verifikasi MP4 (semua dari disk, bukan perkiraan)
ffprobe out/murrotal-quraish-v2-motlab.mp4
ffmpeg -i out/murrotal-quraish-v2-motlab.mp4 -af volumedetect -f null -
ffmpeg -i out/murrotal-quraish-v2-motlab.mp4 -vf blackdetect -f null -
#    Harap: volumedetect dekat -15,0 dB mean / -0,2 dB max (audio contoh),
#    blackdetect 0 segmen. Lalu ekstrak frame kunci SATU PER SATU (jangan
#    gabung select + -frames:v, hasilnya tidak bisa dipercaya):
#    f63 (kata 3 putih), f228 (kata 6), f408 (kata 9), f592 (kata 13, switch
#    tepat), f948 (jeda napas, semua emas), f1050 + f1080 (kata 21 خَوْفٍ
#    putih, WAJIB), f1116 (ekor, teks hilang), f1144 (hampir hitam).
#    Tulis hasilnya di RENDER.md + BUILD-TIMES.txt (lihat templates/).
```

## Isi repo

```
README.md                  dokumen ini
project.json               fps 24, 5 adegan + transisi, audio start 0
build.py                   bangun karaoke-data.json dari teks-quraish.md + karaoke-table.md
                           (perintah awal nyebutnya build_karaoke.py; nama asli file: build.py)
gen_scenes.py              generate scenes/*.html + project.json dari karaoke-data.json
karaoke-table.md           tabel karaoke §5 (21 kata, verbatim dari SUTRADARA asli)
karaoke-data.json          peta karaoke 21 kata (dibangun build.py, jangan edit manual)
teks-quraish.md            teks Kemenag verbatim (Arab + transliterasi + terjemahan)
timing-ayat.md             rentang tiap ayat + jeda napas Ayat 4
transcript.json            token Whisper (6 segmen, 23 token; peta karaoke digabung dari sini)
scenes/                    5 halaman motlab (01-basmalah .. 05-ayat4)
assets/images/             5 gambar webp (bismillah + ayat1-4) + default.webp (Ka'bah,
                           generik). Dipakai kalau gambar satu ayat belum ada; build
                           tetap jalan + peringatan di log.
assets/fonts/              Noto Naskh + Noto Sans (sudah di-vendor)
audio/                     KOSONG di repo. Isi sendiri, lihat audio/README.md.
templates/                 SUTRADARA-TEMPLATE.md, GATE-TEMPLATE.md, RENDER-TEMPLATE.md,
                           BUILD-TIMES-TEMPLATE.md (isi buat surah baru)
.gitignore                 audio/, out/, .tmp/, chkmp4*, scoring-frames*, scdet.log, *.mp4
```

Yang TIDAK ada di repo (sengaja): motlab (prerequisite, bukan fork),
audio recitation (hak cipta qari), MP4 hasil render (dibangun lokal).

## Efek visual template: DOT, PARALLAX, BLUR

Template ini pakai tiga efek visual yang sama di semua video, supaya semua
surah kelihatan satu keluarga. Detail angka lengkap ada di
`TEKNIK-DOT-PARALLAX-BLUR.md` (spec VideoStory, md5 fb7fbfdd, 160 baris;
ringkasnya di `templates/SUTRADARA-TEMPLATE.md` §16).

**DOT (pola titik).** Grid titik putih halus di atas gambar (diameter 3 px,
jarak 24 px, baris ganjil geser 12 px, opacity 6%). Tekstur cetak yang
menyatukan gambar-gambar beda gaya. Titik tidak pernah menutupi teks (kotak
teks menutupinya). Titik ikut lapis gambar (bergerak + membesar ikut zoom
+ pan).

**PARALLAX (gerak berlapis).** Tiga lapis bergerak beda kecepatan + beda
arah: gambar (zoom 30% + pan 20 px), partikel (drift 30 px berlawanan arah
gambar), teks (goyang halus 15 px berlawanan arah gambar). Hasilnya ada rasa
kedalaman, dan tidak ada elemen yang diam di layar. Arah pan disesuaikan per
gambar (ke arah cahaya atau arah gerak subjek). Zoom semua adegan 1.3
(perintah 2026-11-18; dulu 1.03-1.05). Di zoom maks, area gambar yang
kelihatan 831x1477 px (sekitar 11,5% per sisi terpotong); cek framing per
adegan di preview, subjek utama harus tetap di frame.

**BLUR (kaca buram + transisi).** Dua blur yang beda fungsi: (1) blur latar:
gambar di belakang kotak teks dihaluskan (radius 8 px, cuma di dalam kotak
teks, pre-render sekali per adegan) supaya karaoke gampang dibaca, gambar
utama di luar kotak tetap tajam; (2) blur transisi: tiap pindah ayat pakai
transisi bernama (blur lembut, warp, atau dip ke hitam, 0,5 detik).

Semua efek deterministik (hasil render selalu sama), tidak menutupi teks
karaoke, dan tidak mengaburkan gambar utama.

## Gambar: generate AI sesuai cerita ayat

Tiap gambar ayat di-generate AI, mengikuti cerita/arti ayat itu, gaya
konsisten, tanpa teks, 1152x2048 (9:16). Langkah generate DIPISAH dari build
+ render: gambar cuma file di `assets/images/`. Kamu generate di tempat
lain atau upload sendiri, lalu taruh filenya di `assets/images/` dengan
nama yang dipakai
`gen_scenes.py` (bismillah.webp, ayat1.webp, ...). Build + render tidak
butuh alat generate.

Gaya konsisten contoh Quraish (pakai ini sebagai patokan buat surah lain):
lukisan sinematik gelap emas, golden cinematic digital painting, tanpa teks,
tanpa watermark, 9:16, 1152x2048. Panduan lengkap generate gambar (gaya,
prompt per ayat, checklist) ada di `jadi-reciter-panduan-gambar.md`
(panduan Desain, md5 968b9135, 226 baris).

Panduan prompt per ayat (contoh Quraish, arti + isi gambar):

- **Basmalah** (bismillah.webp, 424.386 byte): Ka'bah, sinar emas tembus
  awan, cahaya pagi hangat. Arti: pembuka, nama Allah yang Maha Pengasih.
- **Ayat 1** (ayat1.webp, 446.806 byte): kafilah gurun, senja emas,
  unta + tenda di perjalanan. Arti: kebiasaan Quraisy berdagang, perjalanan
  mereka.
- **Ayat 2** (ayat2.webp, 500.576 byte): perjalanan musim dingin, celah
  gunung bersalju, dingin + perjalanan jauh. Arti: perjalanan musim dingin
  dan musim panas.
- **Ayat 3** (ayat3.webp, 333.516 byte): Ka'bah malam, jamaah, langit
  berbintang, lentera hangat. Arti: sembahlah Tuhan rumah ini (Ka'bah).
- **Ayat 4** (ayat4.webp, 874.814 byte): oasis hijau subur di lembah gurun
  saat senja, kurma, sungai, pohon buah, kota gurun di belakang. Arti:
  Dia yang memberi makan dari lapar dan memberi aman dari takut.

Kalau satu gambar ayat belum ada saat `gen_scenes.py` jalan, adegan itu
pakai `assets/images/default.webp` (Ka'bah, generik) dan log mencetak PERINGATAN
yang menyebut ayatnya. Build TETAP JALAN, video tidak kosong. Ganti gambar
default itu dengan gambarmu sendiri kalau mau, tapi jangan hapus filenya.

## Pelajaran wajib (dari build asli, jangan diulang salahnya)

### VT_OFFSET + frame-snap (baca sebelum ubah gen_scenes.py)

Mekanisme yang BENAR-BENAR ada di kode generator ini:

- Karaoke diputuskan di `drawTextBlock`: `videoFrame =
  Math.floor(videoTime * 24)`, `videoTime = SCENE_START + t`. Kata aktif
  kalau `f_start <= videoFrame < f_end`.
- `f_start = floor(start kata x 24)`, `f_end = floor(end kata SENDIRI x 24)`
  (bukan f_start kata berikut; lihat BUG 3 di bawah).
- Nama `VT_OFFSET` TIDAK ADA di generator ini (grep di file sumber asli
  hasilnya 0). Jangan klaim sebaliknya.

Pelajaran dari varian motlab + herwanto (terbukti di sana): motlab render
memanggil `renderAt(t)` dengan `t` terkuantisasi dari scene start yang
sudah snap ke grid frame (`ceil(SCENE_START*24)/24`). Akibatnya videoTime
mentah bisa ketinggalan sampai 1 frame (41,67 ms) dari waktu frame global
yang benar. Koreksinya: `VT_OFFSET = ceil(SCENE_START*24)/24 - SCENE_START`
(0 sampai 0,0417 detik), ditambahkan ke videoTime SEBELUM frame-snap dan
SEBELUM pembacaan waktu apa pun. Di varian herwanto, VT_OFFSET dipakai buat
timestamp + progress bar; karaoke di sana tetap pakai floor snap polos dan
switch-nya terverifikasi tepat di frame (contoh f592). Generator motion-cut
ini TIDAK PUNYA timestamp atau progress bar, jadi VT_OFFSET tidak dipakai
di jalur mana pun. Kalau kamu TAMBAH timestamp / progress bar ke template
ini, pakai VT_OFFSET di sana, atau pembacaan waktunya ketinggalan sampai
1 frame (di detik bulat bisa terbaca 1 detik lebih rendah). Karaoke di file
ini biarkan seperti aslinya.

### ARAB_LINES (split baris Arab Ayat 4)

Ayat 4 WAJIB `[[0, 1, 2, 3, 4], [5, 6, 7, 8]]` (9 run). Split LAMA yang
SALAH: `[[0,1,2,3],[4,5,6]]` (cuma 7 run). Akibatnya kata 21 خَوْفٍ + tanda
ࣖ TIDAK PERNAH tampil, dan ەۙ salah posisi di awal baris 2. Bug ini lolos
build pertama dan baru ketahuan dari cek frame jendela kata terakhir
(f1035-1084). Perbaikan: re-render 4 versi motlab (RENDER-FIX.md). Aturan:
SETIAP kali generate ulang, `grep خَوْفٍ scenes/05-ayat4.html` HARUS 1.
Kalau 0, JANGAN render. Ayat lain 1 baris semua; Ayat 4 2 baris: baris 1 =
kata 15,16,17,18 + ەۙ di AKHIR, baris 2 = kata 19,20,21 + ࣖ di AKHIR. Tanda
akhir ayat selalu emas, tidak pernah jadi kata aktif.

### Koreksi batas Ayat 3 (24.68, bukan 25.12)

Token Whisper "ربها" (23.70-25.12) adalah gabungan "rabba" + awal "hā".
Batas 25.12 (f 602) SALAH. Bukti akustik: RMS jatuh 24.44-24.66 (akhir
"rabba"), spike frikatif /h/ 24.66-24.70, vokal "hā" mulai 24.70. Di 25.12
tidak ada perubahan akustik. Batas baru 24.68 (f 592). Highlight ganti di
frame 592 (t 24.6667), 13 ms SEBELUM onset /h/, tidak pernah telat.
Terbukti di stills preview (24.60 kata 12 putih, 24.70 kata 13 putih) dan
di MP4 (f590 kata 12, f592 kata 13). Koreksi ini sudah ada di
karaoke-table.md + build.py.

### BUG 3 (f_end) + BUG 4 (pill)

- BUG 3: `f_end = floor(end kata SENDIRI x 24)`. Kalau pakai f_start kata
  berikut, kata 18 (جُوْعٍ, end 38.48) f_end-nya jadi 968, jadi kata 18
  tetap putih sepanjang jeda napas 38.48-40.36. Dengan f_end sendiri (923),
  jeda napas tidak ada kata aktif, semua emas (terbukti f948).
- BUG 4: opacity pill ikut blok teks (fade 0,2 detik). Pill hilang di ekor
  + jeda antar ayat. Jangan gambar pill dengan opacity tetap.

### Aturan lain dari build asli

- Teks Arab DIAMBIL PROGRAM dari teks-quraish.md (build.py + gen_scenes.py).
  Jangan retype Arab. Transliterasi + terjemahan juga programmatic.
- Jumlah frame pakai CEIL: 47,717 x 24 = 1.145,21 jadi 1.146 frame
  (frame 0-1145). Durasi MP4 1146/24 = 47,75 detik (audio tetap 47,717).
- Motlab render output floor(durasi x fps) frame di varian lain (Insyirah:
  821 bukan 822); catat angka render yang sebenarnya di RENDER.md.
- Jangan render dua video bersamaan (VM tidak kuat). Satu render jalan,
  yang lain tunggu.
- Ekstrak frame perbandingan SATU PER SATU dengan nama file beda. Ekstraksi
  gabungan `select` + `-frames:v` tidak bisa dipercaya (frame duplikat).

## Bikin surah baru (langkah ganti contoh)

1. Tulis `templates/SUTRADARA-TEMPLATE.md` + `templates/GATE-TEMPLATE.md`
   buat surah baru (teks, timing, gambar, karaoke). Minta VideoStory
   (sutradara) acc sebelum build.
2. Ganti file contoh dengan file surah baru (nama file boleh sama, isi
   baru): `teks-quraish.md` (ganti nama kalau mau, ubah juga di build.py),
   `timing-ayat.md`, `transcript.json`, `karaoke-table.md` (tabel §5
   terverifikasi surah baru), gambar di `assets/images/` (satu per ayat +
   Basmalah kalau ada di audio).
3. Isi `audio/audio.wav` dengan rekaman surah baru (lihat audio/README.md).
4. Jalankan quickstart langkah 2-6. Catat waktu di RENDER.md +
   BUILD-TIMES.txt (lihat templates/).
5. Preview dulu, acc sutradara, baru render penuh. Jangan render penuh
   dari preview yang belum acc.

## Yang dibutuhkan buat push ke GitHub

Repo ini git init lokal saja, BELUM push. Sebelum push, butuh putusan Bos:

- Akun / organisasi GitHub tujuan (nama akun atau org).
- Nama repo publik (disarankan: `jadi-reciter`).
- Lisensi (BELUM ada file LICENSE di repo; butuh putusan Bos: MIT atau lain).
- Visibilitas: publik (sesuai perintah Bos).

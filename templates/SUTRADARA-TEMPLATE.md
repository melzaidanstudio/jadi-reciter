# SUTRADARA TEMPLATE: Murrotal QS. [NAMA SURAH] ([NOMOR]) v[1], motlab + motion-cut
# Sutradara: [NAMA], [TANGGAL] WIB
# Perintah [BOS/CEO] via [JALUR]. [Revisi dari v1 / video baru].
# Engine MOTLAB (bukan HyperFrames). Gaya MOTION-CUT. Output 720x1280 24fps.
# CARA PAKAI: isi semua [PLACEHOLDER] dengan data surah baru yang terverifikasi
# dari disk. Angka contoh Quraish (106) v2 ada di tiap seksi sebagai patokan.
# Jangan tulis perkiraan: semua angka harus hasil ukur (audio, teks, timing).

## 0. Konteks, jangan salah proyek
- [Status video sebelumnya kalau ada: v1 di folder apa, sudah di mana, jangan disentuh.]
- v[1] ini proyek BARU: [NAMA FOLDER PROYEK]/ (baru, jangan timpa proyek lama).
- [PERBANDINGAN BOS kalau ada: versi apa saja yang dibandingkan, Bos putuskan sesudah lihat apa.]
- Audio, gambar, teks, timing ayat v[1] [SAMA PERSIS dengan v1 / BARU]. Yang berubah cuma [N] hal (§3).

## 1. Format + engine
- Halaman motlab 1080x1920 (9:16), project.json "fps": 24, render --scale 0.6667 jadi output 720x1280.
- Durasi [DURASI AUDIO] dtk (audio utuh). Jumlah frame: [DURASI] x 24 = [HITUNG]. Frame render [CEIL] (frame 0-[CEIL-1]), ikut aturan v1 (frame f dirender selama f/fps < durasi). Angka pasti dari render, Builder tulis di RENDER.md.
- [JUMLAH] adegan (satu per ayat: [DAFTAR AYAT]; ayat panjang dipotong jadi 2 atau 3 adegan, lihat §18), satu halaman motlab per adegan, di scenes/.
- project.json: fps 24, scenes urut [DAFTAR FILE], audio audio.wav start 0 volume 1.0 (lihat §11).
- Chrome lewat wrapper --no-sandbox di ~/.local/bin/google-chrome. TMPDIR di /home (~/.motlab-tmp). motlab sudah terpasang, doctor OK.
- Halaman ikut page contract motlab: canvas id "c" 1080x1920 x scale, window.renderAt(t), window.TOTAL, window.ready. Tidak ada Date.now, tidak ada Math.random, tidak ada fetch jaringan. Font + gambar lokal di folder proyek.
- Transisi antar adegan pakai shader gl-transitions di project.json (lihat §8). Dua adegan tumpang tindih selama durasi transisi, video jadi lebih pendek sejumlah itu, jadi TOTAL tiap adegan dihitung dengan overlap (§8).

## 2. Input, semua diverifikasi sutradara dari disk, jangan diubah
- [JUMLAH] gambar [FOLDER GAMBAR]/ (1152x2048, 9:16, [GAYA], tanpa teks), disalin ke assets/images/ proyek (copy, jangan pindah): [DAFTAR NAMA FILE + UKURAN BYTE + DESKRIPSI PER GAMBAR].
- TANYA GAMBAR DULU (WAJIB, sebelum generate, lihat §17): kalau AI yang dipakai user BISA generate gambar, tanya user mau jalur A (gambar default sesuai ayat) atau jalur B (gambar ikut satu tema yang di-input user, TIDAK sesuai ayat). Catat pilihan + tema (kalau B) di SUTRADARA ini sebelum generate. Kalau AI-nya TIDAK BISA generate gambar, lewati tanya ini, pakai gambar yang user upload sendiri.
- Gambar = file biasa di assets/images/. Langkah generate DIPISAH dari build + render: generate di tempat lain atau upload sendiri, taruh filenya di assets/images/, baru build. Kalau gambar satu ayat belum ada saat gen_scenes.py jalan, adegan itu pakai assets/images/default.webp (Ka'bah, generik) + log mencetak PERINGATAN yang menyebut ayatnya, build TETAP JALAN, video tidak kosong. Ini koreksi Bos (ganti aturan berhenti keras sebelumnya); jangan hapus default.webp.
- Audio [FOLDER]/audio.wav, md5 [MD5], [UKURAN] byte, [DURASI] dtk, [SAMPLE RATE] stereo, [NAMA QARI]. Dipakai UTUH, tanpa potong, tanpa dipercepat, tanpa BGM. Disalin ke audio/ proyek.
- Teks verbatim Kemenag [FOLDER]/teks-[SURAH].md, md5 [MD5]. Arab + transliterasi + terjemahan. Teks Arab DIAMBIL PROGRAMMATIC dari file ini saat build (script copy, jangan retype, jangan ubah). Transliterasi verbatim termasuk tanda khusus, jangan diedit. Terjemahan versi situs Kemenag saat ini, jangan ganti ke versi lama.
- Timing ayat [FOLDER]/timing-ayat.md, md5 [MD5]: [DAFTAR RENTANG PER AYAT]. Jeda antar ayat: [DAFTAR]. [Jeda napas kalau ada, di TENGAH ayat, bukan batas ayat.] Hening awal [X]-[Y] dtk, hening ekor [X]-[Y] dtk.
- transcript.json, md5 [MD5], [N] segmen, [N] token kata Whisper (lihat §5).

## 3. Perubahan, [N] saja
1. SUBTITLE KARAOKE: tiap kata Arab berubah warna pas ayat dibacain. Kata aktif PUTIH #FFFFFF, kata lain EMAS #E8C766. Pakai word timestamps Whisper (§5). Highlight ganti TEPAT di awal kata, jangan telat. Frame 24fps, batas kata snap ke grid frame 41,67 ms (§5).
2. SHADOW BOX: kotak hitam transparan di belakang blok teks (Arab + transliterasi + terjemahan), ikut screenshot referensi Ad-Dhuha (§6). Kotak rounded, isi hitam semi-transparan, border tipis terang, padding rapi, ukuran ikut tinggi teks tiap ayat. Jangan tutupi pill.
3. HAPUS footer "Qur'an Kemenag" dari video. Tidak ada di frame mana pun.

## 4. Referensi shadow box + karaoke
- File: [PATH REFERENSI], [UKURAN] byte, QS. [SURAH] Ayat [N]. Sutradara baca langsung.
- Isi gambar: pill atas "[TEKS PILL]" (kotak gelap rounded, teks terang, tengah atas). Kotak rounded hitam transparan di sepertiga bawah, border tipis terang. Di dalam kotak: Arab emas, kata terakhir PUTIH (kata aktif karaoke), terjemahan PUTIH 2 baris di bawah Arab. Tanpa footer, tanpa transliterasi di referensi (v2 tetap pakai transliterasi, lihat §6).
- Yang diambil dari referensi: pill atas, kotak rounded hitam transparan + border tipis, Arab emas + kata aktif putih, terjemahan putih di dalam kotak, tanpa footer.

## 5. Peta karaoke [N] kata (WAJIB, terverifikasi dari disk)
- Teks tampil ada [N] kata Arab ([PER AYAT]). Whisper ada [N] token. Selisih [N] karena Whisper mecah kata: [JELASKAN GABUNGAN TOKEN, contoh Quraish: Ayat 1 Li'īlāfi dipecah jadi لإيلى + في; Ayat 2 Īlāfihim dipecah jadi إيلى + فيهم]. Solusi: GABUNG token yang bersangkutan (lihat tabel, kolom catatan).
- Koreksi batas segmen dari timing-ayat.md: kata 1 [KATA] start [LAMA] jadi [BARU] ([ALASAN, hening awal]); kata [TERAKHIR] end [LAMA] jadi [BARU] ([ALASAN]).
- Snap frame: frame f mulai t = f/24. Kata aktif di frame floor(start x 24). Highlight ganti paling lambat 41,67 ms SEBELUM awal kata, tidak pernah telat. Kolom f_start + t_frame di tabel adalah waktu ganti highlight yang dipakai render.
- Tanda akhir ayat ([DAFTAR TANDA]) BUKAN kata. Tetap tampil (bagian teks Arab verbatim), tapi SELALU emas, tidak pernah jadi kata aktif putih.
- Transliterasi + terjemahan TIDAK karaoke, tetap statis (warna tetap, tidak berubah per kata).
- Saat jeda napas [AYAT] ([RENTANG]) TIDAK ADA kata aktif: semua kata Arab emas, tidak ada yang putih.

| No | Ayat | Kata tampil | Start (dtk) | End (dtk) | f_start | t_frame (dtk) | Token Whisper yang digabung |
|---|---|---|---|---|---|---|---|
| 1 | [Ayat] | [KATA] | [X] | [X] | [N] | [X] | [TOKEN + RENTANG] |
| ... | ... | ... | ... | ... | ... | ... | ... |

- Cek sutradara: [N] kata, tidak ada tumpang tindih, semua durasi positif, jeda napas [RENTANG] kosong.
- CATATAN BATAS [AYAT] (kalau ada koreksi batas seperti Quraish 24.68): [BUKTI AKUSTIK + STILLS].
- Implementasi karaoke di motlab (2D canvas): Arab digambar kata per kata (tiap kata satu run teks). Warna kata ditentukan waktu t: putih kalau frame(t) ada di [f_start, f_end) kata itu, emas kalau tidak. f_end = floor(end kata SENDIRI x 24), BUKAN f_start kata berikut (KOREKSI BUG 3): kalau f_end pakai f_start kata berikut, kata terakhir sebelum jeda napas tetap putih sepanjang jeda. Kata disusun RTL (kanan ke kiri, kata 1 paling kanan). Font Noto Naskh Arabic (disalin ke assets/fonts/ proyek, jangan CDN). Ukuran Arab diatur supaya baris terpanjang muat dalam lebar dalam kotak 880 px (lihat §6). [AYAT] Arab [N] baris, sisanya 1 baris.

## 6. Shadow box + layout teks (koordinat halaman 1080x1920)
- Semua koordinat di bawah dalam piksel halaman 1080x1920 (bukan output 720x1280). Render --scale 0.6667 mengecilkan semuanya proporsional.
- PILL (tetap dari v1): y 60-112, tengah horizontal, kotak gelap (hitam 55%) + border emas + teks emas. Basmalah: "QS. [SURAH] ([NOMOR]) - Basmalah". Ayat: "QS. [SURAH] ([NOMOR]) - Ayat n / [JUMLAH]". Pill TIDAK BOLEH ditutupi shadow box.
- SHADOW BOX: kotak rounded di belakang blok teks (Arab + transliterasi + terjemahan).
  - Posisi: tengah horizontal, x 60-1020 (lebar 960 px). Bawah kotak y ~1731. Atas kotak ikut tinggi teks tiap ayat. Jangan sampai atas kotak menyentuh pill.
  - Isi: hitam semi-transparan rgba(0,0,0,0.55). Border tipis terang rgba(255,255,255,0.35), tebal 2 px. Corner radius 24 px.
  - Padding: 36 px vertikal, 40 px horizontal. Lebar dalam 880 px.
  - Isi kotak (dari atas ke bawah, semua tengah horizontal):
    - Arab: emas #E8C766, kata aktif putih #FFFFFF (lihat §5). Font Noto Naskh Arabic. Ukuran diatur supaya baris terpanjang muat 880 px. [N] baris per ayat.
    - Transliterasi: di bawah Arab, jarak 24 px. Putih pudar rgba(255,255,255,0.85), font Noto Sans, ukuran ~36 px, 1 baris.
    - Terjemahan: di bawah transliterasi, jarak 24 px. PUTIH #FFFFFF, font Noto Sans, ukuran ~40 px, maksimal 2 baris. [BARIS PER AYAT].
  - TIDAK ADA footer "Qur'an Kemenag" di mana pun. Tidak ada teks lain di layar selain pill + isi kotak.
- PILL IKUT FADE TEKS (KOREKSI BUG 4): pill digambar dengan opacity yang sama kayak blok teks (fade 0,2 dtk di awal + akhir rentang ayat). Pill hilang di ekor + jeda antar ayat. Jangan gambar pill dengan opacity tetap.
- Teks muncul per ayat UTUH (bukan kata per kata munculnya, cuma WARNA kata yang berubah): teks ayat muncul bersama dissolve di awal ayat, tetap selama ayat, hilang di akhir ayat. Di ekor teks hilang, gambar tetap, fade hitam 0,5 dtk terakhir (§8 adegan terakhir).

## 7. Adegan ([JUMLAH] adegan, satu halaman motlab per adegan)
- Semua adegan: gambar latar (webp di assets/images/), Ken Burns zoom-in (mulai 1,00x, selesai 1.3x, linear), pan 20 px (arah per adegan, §16), partikel + cahaya digambar di atas gambar (kode canvas, bukan gambar baru), shadow box + teks (§6), pill (§6), DOT (§16). Ayat panjang yang dipotong (§18) jadi 2 atau 3 adegan, satu adegan per potongan, masing-masing gambar sendiri. Nama file potongan: scenes/[NOMOR]-ayat[N][a/b/c].html (contoh ayat 4 dipotong 2: 05-ayat4a.html + 05-ayat4b.html).
- ADEGAN 1 [NAMA] (scenes/[FILE]): gambar [FILE] ([DESKRIPSI]). TOTAL [X] dtk (video [A]-[B]). Teks [AYAT] [X]-[Y] (lokal t [X]-[Y]). [Hening awal kalau ada: gambar saja, tanpa teks.] Cahaya: [DESKRIPSI]. Partikel: [JENIS]. Transisi keluar: [JENIS] (§8).
- ADEGAN 2 [NAMA]: [SAMA, satu blok per adegan, sampai adegan terakhir.]
- Cek jumlah TOTAL: [X] + [X] + ... = [TOTAL] dtk. Kurang [N] transisi x 0,5 dtk = [OVERLAP] dtk overlap = [DURASI VIDEO] dtk. Cocok ([DURASI AUDIO] dtk).

## 8. Transisi bernama (motion-cut, tiap pindah ayat 0,5 dtk)
- Semua transisi 0,5 dtk, di tengah jeda antar ayat. Jenis + alasan:
  - D1 [A] ke [B] (video [X]-[Y]): fade (cross-dissolve). Alir mengalir.
  - D2 [A] ke [B] (video [X]-[Y]): whip (directionalwarp, direction [-1, 1]). Pindah tempat jauh.
  - D3 [A] ke [B] (video [X]-[Y]): dip (fadecolor, color [0,0,0] hitam, colorPhase 0.4). Lompat waktu + babak baru.
  - D4 [A] ke [B] (video [X]-[Y]): fade (cross-dissolve). Alir mengalir.
- Di project.json, transisi ditulis di adegan yang DIMASUKI (bukan yang ditinggalkan), format motlab: { "file": "scenes/02-ayat1.html", "transition": { "type": "fade", "duration": 0.5, "ease": "inOutCubic" } }. Nama type tidak case-sensitive.
- Potongan ayat (§18): transisi antar potongan SELALU dissolve (fade, cross-dissolve) 0,5 dtk, ease inOutCubic, sama kayak D1/D4. JANGAN pakai directionalwarp atau fadecolor antar potongan (itu buat pindah ayat yang lompat tempat/waktu/babak). Transisi potongan ditulis di project.json di adegan yang dimasuki, sama kayak transisi ayat.
- Perhatian motlab: dua adegan tumpang tindih selama transisi, jadi adegan yang ditinggalkan harus punya isi sampai akhir TOTAL-nya, dan adegan yang dimasuki sudah jalan sejak awal TOTAL-nya. Audio start di project.json pakai waktu video jadi (sesudah overlap), jangan geser audio karena transisi (audio cuma satu file, start 0).

## 9. Audio
- Satu file: audio.wav ([NAMA QARI], utuh [DURASI] dtk), di project.json: { "file": "audio/audio.wav", "start": 0, "volume": 1.0 }. Tidak ada BGM, tidak ada musik, tidak ada SFX, tidak ada bed. Motion-cut: tanpa musik, narasi di depan. Di sini narasi = murrotal itu sendiri.
- Target loudness: ukur volumedetect MP4 hasil render, tulis di RENDER.md. Contoh Quraish: -15,0 dB mean / -0,2 dB max. v[1] harus dekat angka itu (audio sama, jadi harus sama; kalau beda jauh, ada yang salah di mix).

## 10. Engine motlab, perintah build + render
- Folder proyek: [PATH PROYEK]/ (baru). Struktur: project.json, scenes/ ([N] halaman), assets/images/ ([N] webp + default.webp), assets/fonts/ (Noto Naskh Arabic + Noto Sans), audio/ (audio.wav), out/ (hasil render).
- project.json: { "fps": 24, "scenes": [ ... ], "audio": [ { "file": "audio/audio.wav", "start": 0, "volume": 1.0 } ] }.
- Halaman adegan dari template 2D motlab: canvas 1080x1920, renderAt(t), TOTAL, ready. Gambar latar digambar dengan Ken Burns (scale 1,00 ke 1.3, linear) + pan 20 px (§16). Partikel + cahaya digambar di atas gambar. Shadow box + teks digambar di atas partikel (teks paling atas, kecuali pill). Semua gerak deterministik (hanya fungsi t + hash, tanpa Math.random), supaya stills dan render sama.
- RENDER [DIPERINTAHKAN BOS SECARA EKSPLISIT DI CHAT / TUNGGU ACC BOS]. Perintah render: TMPDIR=$PWD/.tmp motlab render . --scale 0.6667 (dari folder proyek). Output: out/[NAMA].mp4 (720x1280 24fps). Catat waktu build + render (§12).
- Sebelum render penuh: preview dulu (§11). Jangan render penuh sebelum sutradara acc preview sheet.

## 11. Preview dulu, render belakangan (aturan motion-cut)
- Builder buat stills pakai motlab stills per adegan + tiap transisi, lalu contact sheet, kirim ke sutradara. Sutradara cek SEBELUM render penuh.
- Waktu stills (waktu video, dtk): [DAFTAR 12 TITIK: satu per ayat (kata aktif) + jeda napas + tiap transisi tengah + ekor + frame terakhir]. Contoh Quraish: Basmalah 2,63 (kata 3 aktif, frame 63), Ayat 1 9,50 (kata 6, frame 228), Ayat 2 17,00 (kata 9, frame 408), Ayat 3 25,00 (kata 13, frame 600), Ayat 4 42,00 (kata 20, frame 1008), Ayat 4 jeda napas 39,50 (tidak ada kata aktif, frame 948), transisi D1 6,86 (frame 164), D2 11,89 (frame 285), D3 21,73 (frame 521), D4 28,94 (frame 694), ekor 46,50 (teks hilang, frame 1116), frame terakhir 47,70 (hampir hitam, frame 1144).
- Yang dicek sutradara di preview: kata aktif putih di frame yang benar (tidak telat, tidak salah kata), shadow box rapi + tidak tutupi pill, Arab [N] baris tidak meluber, terjemahan maksimal 2 baris, tanpa footer di frame mana pun, gambar per ayat benar, Ken Burns + pan jalan, partikel + cahaya ada di tiap adegan, transisi bernama terlihat, batas [AYAT] verifikasi telinga, DOT kelihatan, framing zoom 1.3 (subjek utama masih di frame).
- Kalau preview ada yang salah, betulkan dulu, stills ulang, baru render penuh. Jangan render penuh dari preview yang belum acc.

## 12. Waktu build + render (perintah Bos, perbandingan antar versi)
- Bos bandingkan versi [DAFTAR VERSI]. Builder WAJIB catat WAKTU build + render penuh versi ini pakai angka di RENDER.md: jam mulai build, jam selesai build, jam mulai render, jam selesai render, total menit build, total menit render, total menit build + render. Pakai jam WIB + durasi menit.
- Angka waktu ini yang dibandingkan antar versi. Jangan tulis perkiraan, tulis hasil ukur jam nyata. Kalau render diulang karena revisi, catat tiap run (run 1, run 2) + total.

## 13. Yang TIDAK dipakai dari motion-cut
- Hook layar terbelah sebab/akibat: tidak dipakai (murrotal bukan explainer sebab-akibat, tidak ada hook).
- "Bagian kedua" penutup: tidak dipakai (tidak ada penutup, video selesai fade hitam, tanpa end card, tanpa CTA).
- Naskah baru: tidak dipakai (teks = ayat Qur'an verbatim, bukan naskah baru).
- TTS baru: tidak dipakai (audio = [QARI] utuh, bukan TTS).
- Caption satu kata di 44%: tidak dipakai begitu saja (karaoke ini kata aktif di dalam baris Arab, bukan caption satu kata terpisah; yang dipakai dari motion-cut: caption per kata = karaoke, transisi bernama, partikel + cahaya per adegan, tanpa musik, preview sheet dulu).
- Format motion-cut 30 fps: tidak dipakai (v[1] pakai 24 fps per perintah Bos, motlab default mobile).

## 14. Yang tetap dari v1
- [DAFTAR YANG TETAP: gambar sama, audio utuh, teks verbatim, timing ayat, Ken Burns + pan, pill, ekor teks hilang + fade hitam 0,5 dtk terakhir, tanpa end card, tanpa CTA.]
- Yang berubah cuma [N] hal di §3 + [DOT/PARALLAX §16] + engine motlab + transisi bernama + partikel/cahaya (motion-cut).

## 15. CATAT WAKTU (perintah Bos, perbandingan antar versi)
- Builder WAJIB isi tabel di bawah ini di RENDER.md, pakai JAM NYATA (WIB), bukan perkiraan. Laporan akhir versi ini HARUS bawa angka ini.
- Jam mulai build: (isi, WIB)
- Jam kelar build: (isi, WIB)
- Total menit build: (isi, menit)
- Jam mulai render: (isi, WIB)
- Jam MP4 jadi: (isi, WIB)
- Total menit render: (isi, menit)
- TOTAL menit build + render: (isi, menit)
- Kalau render diulang karena revisi, catat tiap run (run 1, run 2) + total. Jangan tulis perkiraan, tulis hasil ukur jam nyata.

## 16. ADDENDUM: DOT, PARALLAX (spec VideoStory, md5 453c281a, 142 baris)
- Teknik ini addendum ke SUTRADARA ini, bukan ganti SUTRADARA. Semua angka
  dalam piksel HALAMAN 1080x1920. Output 720x1280 = halaman x 0.6667.
- Urutan gambar per frame (dari belakang ke depan): (1) gambar tajam + Ken
  Burns + pan, (2) pola DOT, (3) partikel,
  (4) shadow box + pill + teks, (5) fade hitam ekor (adegan terakhir saja).
- DOT: diameter titik 3 px, jarak grid 24 px horizontal + 24 px vertikal,
  baris ganjil geser 12 px ke kanan (stagger), warna putih #FFFFFF, opacity
  0.06, bentuk lingkaran (radius 1.5 px). Jumlah 45 kolom x 80 baris =
  ~3.600 titik per frame. Area: SELURUH frame, di atas gambar, di bawah
  shadow box + pill + teks. DOT ikut lapis gambar (bergerak + membesar
  ikut Ken Burns zoom + pan). Titik tidak pernah menyentuh teks (shadow
  box menutupinya).
- PARALLAX (3 lapis semu, tanpa oklusi): LAPIS 1 gambar + DOT: Ken Burns
  zoom-in (KB_END 1.3 SEMUA adegan, perintah Bos 2026-11-18) + pan linear
  20 px sepanjang adegan, arah per adegan (lihat tabel). Kecepatan acuan
  1,0x. LAPIS 2 partikel: drift BERLAWANAN arah pan gambar, 30 px linear
  sepanjang adegan (1,5x gambar); gerak asli partikel TETAP, drift adalah
  offset tambahan. LAPIS 3 blok teks (shadow box + pill + teks): drift
  sinusoidal BERLAWANAN arah pan gambar, amplitudo 15 px, satu siklus
  penuh per adegan (0 di awal + akhir, puncak di tengah). Rumus: dx = -15
  x sin(2 x PI x t / TOTAL) x PAN_DIR_X, dy = -15 x sin(2 x PI x t / TOTAL)
  x PAN_DIR_Y. Drift teks TIDAK BOLEH ganggu keterbacaan (maks 15 px,
  sinusoidal halus, arah konsisten per adegan).
- Arah pan per adegan (contoh Quraish): Basmalah ATAS (0,-1), Ayat 1 KANAN
  (1,0), Ayat 2 KIRI (-1,0), Ayat 3 KANAN (1,0), Ayat 4 ATAS (0,-1).
  Aturan umum: pan ke arah sumber cahaya ATAU arah gerak subjek. Kalau
  tidak jelas, default KANAN. Zoom semua adegan 1.3, tidak ikut durasi
  lagi (perintah Bos 2026-11-18 ~00:55 WIB).
- CATATAN GATE (zoom 1.3): 1.3 jauh lebih kuat dari 1.03-1.05 (zoom 30%,
  bukan 3-5%). Di zoom maks, area gambar yang kelihatan cuma 1080/1.3 =
  831 px lebar x 1920/1.3 = 1477 px tinggi, jadi ~11,5% per sisi di
  keempat sisi (total ~23% per dimensi) terpotong. Builder WAJIB cek dampak
  framing/crop per adegan di preview (subjek utama masih di frame atau
  tidak). Kalau subjek utama terpotong, laporkan ke sutradara. Jangan ubah
  nilainya, nilai tetap 1.3 perintah Bos; yang dicek cuma dampaknya.
- TRANSISI (motion-cut): D1 + D4 fade 0.5 (cross-dissolve), D2 directionalwarp [-1,1], D3 fadecolor hitam 0.4.
- Verifikasi: DOT ~3.000 titik kelihatan di still, diameter 2 px (output),
  opacity 0.04-0.08, tidak ada titik di teks, titik bergerak ikut gambar.
  Pan ~20 px per adegan, zoom 1.3, partikel drift ~30 px berlawanan, teks
  drift ±15 px kembali 0 di akhir adegan, tidak ada elemen statis (MAD >0
  semua zona). Gambar tajam di semua zona, tepi 1-2 px, stroke Arab 1-2 px
  (tajam). Transisi: D1 + D4 blend lembut (fade), D2 warp diagonal, D3 dip
  hitam, 0 hard cut di luar transisi.

## 17. TANYA GAMBAR DULU (jalur A / jalur B, perintah Dewa 2026-11-18)
- Sebelum generate gambar apa pun, TANYA dulu ke user mau jalur yang mana.
  Aturan ini WAJIB kalau AI yang dipakai user BISA generate gambar. Kalau
  AI-nya TIDAK BISA generate gambar, lewati pertanyaan ini, pakai gambar
  yang user upload sendiri (atau default.webp kalau gambar satu ayat belum
  ada, build tetap jalan + peringatan di log).
- STOP KERAS: DILARANG generate gambar apa pun dan DILARANG lanjut ke langkah build sebelum jawaban user TERCATAT di SUTRADARA ini. Kalau belum ada jawaban, BERHENTI di sini.
- Jalur A (default, perilaku lama): tiap gambar ayat di-generate AI
  mengikuti cerita/arti ayat itu, gaya konsisten, tanpa teks, 1152x2048.
  Panduan gambar §1 sampai §4 berlaku penuh buat jalur A.
- Jalur B (tema, TIDAK sesuai ayat): user input satu tema. Semua gambar
  (satu per ayat + Basmalah kalau ada di audio) di-generate mengikuti tema
  itu. Gambar TIDAK perlu sesuai arti ayat. Teks Kemenag, karaoke, dan
  timing TIDAK berubah, cuma gambarnya yang ikut tema. Syarat yang tetap
  berlaku: generate AI (bukan stok, bukan comot), gaya konsisten satu
  video, TANPA teks di gambar, ukuran 1152x2048 WebP 9:16, parallax-ready,
  jangan gambar wajah nabi atau sahabat. Antislop: tiap gambar punya
  subjek yang jelas + komposisi yang kuat, tidak generik, tetap satu dunia
  dengan gambar lain di video yang sama.
- Catat di SUTRADARA ini sebelum generate: jalur yang dipilih user + tema
  yang di-input (kalau jalur B). GATE verifikasi pilihan ini (GATE §
  "Cek tanya gambar").
- Deskripsi gambar per adegan di §7 mengikuti jalur yang dipilih: jalur A
  deskripsi ikut cerita ayat, jalur B deskripsi ikut tema. Arah pan +
  jenis partikel per adegan dipilih dari gambar yang sebenarnya (arah
  sumber cahaya ATAU arah gerak subjek), bukan dari cerita ayat.
- Satu video cuma pakai satu jalur. Jangan campur A dan B dalam satu video.

## 18. POTONG AYAT PANJANG JADI 2 ATAU 3 BAGIAN (perintah Dewa 2026-11-18)
- Ayat yang PANJANG dipotong jadi 2 atau 3 bagian, biar tidak monoton di satu gambar. Ayat panjang = ayat yang kalau ditampilkan utuh di satu adegan, satu gambar diam terlalu lama. Sutradara yang putuskan ayat mana yang dipotong, dicatat di §7 (satu adegan per potongan). Maksimal 3 potongan per ayat.
- Potong di BATAS FRASA YANG NATURAL, BUKAN tengah kata. Titik potong yang boleh: di tanda berhenti (waqf) ayat, di batas antar klausa, atau di jeda napas di tengah ayat (kalau ada). JANGAN potong di tengah frasa, JANGAN potong di tengah kata. Tulis titik potongnya di §7 (kata terakhir potongan + kata pertama potongan berikut).
- Urutan karaoke TETAP NYAMBUNG antar potongan. Peta karaoke §5 tetap SATU urutan utuh: nomor kata lanjut terus antar potongan (kata terakhir potongan 1 = kata n, kata pertama potongan 2 = kata n+1), f_start/f_end tidak berubah. Tidak ada kata yang hilang, tidak ada kata yang diulang, tidak ada tumpang tindih.
- Tiap potongan dapat GAMBAR SENDIRI. Jalur A: gambar potongan mengikuti cerita bagian ayat itu. Jalur B: gambar potongan mengikuti tema (§17), satu gambar per potongan, tetap satu tema buat semua potongan. Gambar tiap potongan harus beda (jangan pakai gambar yang sama dua kali).
- Teks tiap potongan: adegan potongan cuma menampilkan kata-kata potongan itu (Arab + transliterasi + terjemahan bagian itu saja). Rentang teks potongan = dari start kata pertama sampai end kata terakhir potongan itu, fade 0,2 dtk di awal + akhir (ikut §6). Pill potongan: "QS. [SURAH] ([NOMOR]) - Ayat n / [JUMLAH] (bagian k / K)".
- Transisi antar potongan: SELALU dissolve (fade) 0,5 dtk (§8). Hitungan TOTAL ikut §7/§8: jumlah TOTAL semua adegan (termasuk potongan) kurang semua transisi (antar ayat + antar potongan) x 0,5 dtk = durasi video. Audio tetap satu file, start 0, tidak digeser karena potongan.
- Penamaan file potongan: scenes/[NOMOR]-ayat[N][a/b/c].html (contoh ayat 4 dipotong 2: 05-ayat4a.html + 05-ayat4b.html). Urutan scenes di project.json ikut urutan potongan.

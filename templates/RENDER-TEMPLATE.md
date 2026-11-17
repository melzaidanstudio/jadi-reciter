# RENDER TEMPLATE: Murrotal QS. [NAMA SURAH] ([NOMOR]) v[1], motlab + motion-cut
# Builder: [NAMA], [TANGGAL] WIB
# CARA PAKAI: isi semua [PLACEHOLDER] dengan angka HASIL UKUR dari disk (md5sum,
# ffprobe, volumedetect, blackdetect, frame cek). Jangan tulis perkiraan.
# Bagian "CONTOH" di bawah adalah angka ASLI build Quraish (106) v2
# (motlab + motion-cut, versi FIX) sebagai contoh kerja. Hapus bagian contoh
# kalau RENDER.md ini dipakai buat surah baru, atau pindahkan ke arsip.

## Output
- File: out/[NAMA FILE].mp4
- Ukuran: [UKURAN] byte, md5 [MD5]
- Video: h264, 720x1280, 24fps, [N] frame (frame 0-[N-1]), durasi [X] dtk
- Audio: aac, [SAMPLE RATE] stereo, durasi [X] dtk (audio sumber utuh, tanpa potong)
- Perintah render: TMPDIR=$PWD/.tmp motlab render . --scale 0.6667 (dari folder proyek)

## CATAT WAKTU (§12 + §15, perintah Bos, jam nyata WIB)
- Jam mulai build: [ISI] WIB
- Jam kelar build: [ISI] WIB
- Total menit build: [ISI]
- Jam mulai render run 1: [ISI] WIB
- Jam run 1 gagal: [ISI] WIB ([ALASAN, kalau ada])
- Jam mulai render run 2: [ISI] WIB
- Jam MP4 jadi (run 2): [ISI] WIB
- Total menit render (run 2): [ISI]
- TOTAL menit build + render: [ISI]

## Verifikasi MP4 (semua dari disk, bukan perkiraan)
- ffprobe: 720x1280, 24fps, nb_frames [N], durasi video [X] dtk, audio [X] dtk
- volumedetect: mean [X] dB, max [X] dB ([BANDINGKAN DENGAN SUMBER])
- blackdetect: [N] frame hitam
- scdet (threshold 0.10): [N] entri, [N] di dalam jendela transisi, [N] di luar ([NILAI MAKS di luar + apa itu])
- Frame-diff penuh (grayscale 270x480, [N] frame): median mean [X], rata-rata [X], maks [X]. Kandidat hard cut (mean>20 AND pct>30): [N] frame, SEMUANYA di dalam jendela transisi ([DAFTAR]). 0 hard cut di luar transisi.
- Audio korelasi: lag terbaik [N] sample = [X] ms, korelasi global [X], per jendela [DAFTAR] (tidak ada drift, audio identik sumber)

## Karaoke (dicek dari frame MP4, ekstraksi terpisah per nomor frame)
- [AYAT] frame [N] ([X] dtk): kata [N] aktif putih. Terjemahan [N] baris.
- [AYAT] frame [N] ([X] dtk): kata [N] aktif putih, tanda [TANDA] emas.
- [AYAT] frame [N] ([X] dtk): kata [N] aktif putih.
- [AYAT] frame [N] ([X] dtk): kata [N] aktif putih. Frame [N] ([X] dtk): kata [N+1] aktif putih, kata [N] emas. Switch TEPAT di frame [N].
- [AYAT] frame [N] ([X] dtk): kata [N] aktif putih di baris 2, Arab 2 baris rapi, tanda [TANDA] + [TANDA] emas.
- Jeda napas frame [N] ([X] dtk): SEMUA kata emas, tidak ada kata aktif (BUG 3 betul).
- Ekor frame [N] ([X] dtk): pill HILANG, teks HILANG, cuma gambar (BUG 4 betul).
- Frame terakhir [N] ([X] dtk): hampir hitam, fade to black jalan.
- Tanpa footer di frame mana pun. Shadow box rapi, tidak tutupi pill.

## Transisi shader (dicek dari frame MP4, blend nyata, bukan hard cut)
- D1 frame [N] ([X] dtk): [JENIS], blend [DESKRIPSI], tanpa pill/teks.
- D2 frame [N] ([X] dtk): [JENIS], [DESKRIPSI], tanpa pill/teks.
- D3 frame [N] ([X] dtk): [JENIS], [DESKRIPSI], tanpa pill/teks.
- D4 frame [N] ([X] dtk): [JENIS], [DESKRIPSI], tanpa pill/teks.

## DOT + PARALLAX + BLUR (dicek dari frame MP4 + stills, SUTRADARA §16)
- DOT: [N] titik kelihatan di still, diameter [N] px (output), opacity [X], tidak ada titik di teks, titik bergerak ikut gambar.
- PARALLAX: pan gambar [N] px per adegan ke arah tabel, zoom 1.3, partikel drift [N] px berlawanan, teks drift ±[N] px kembali 0 di akhir adegan, tidak ada elemen statis (MAD >0 semua zona).
- Zoom 1.3 framing/crop per adegan: [SUBJEK MASIH DI FRAME / TERPOTONG + APA]. Kalau terpotong, laporkan ke sutradara.
- BLUR latar: tepi di zona teks [N] px lebih halus dari tepi di luar zona, tepi di luar zona [N] px (tajam), stroke Arab [N] px (tajam).
- Transisi blur: D1 + D4 blend blur, D2 warp + motion blur, D3 dip hitam, 0 hard cut di luar transisi.

## Koreksi batas [AYAT] (berlaku di versi ini, bukti akustik + stills)
- Batas lama [X] (f [N]) SALAH. Batas baru [X] (f [N]): [BUKTI AKUSTIK]. Di [X] tidak ada perubahan akustik. Durasi kata [A] [X] dtk, kata [B] [X] dtk, seimbang.
- SUTRADARA §5/§6 mengizinkan geser batas kalau [KONDISI]. Terbukti di MP4: frame [N] kata [A] putih, frame [N] kata [B] putih.

## BUG 3 + BUG 4 (dibetulkan di build, terbukti di MP4)
- BUG 3: f_end = floor(end kata SENDIRI x 24), bukan f_start kata berikut. Kata [N] f_end [N] (bukan [N]). Jeda napas [RENTANG] tidak ada kata aktif.
- BUG 4: opacity pill ikut blok teks (fade 0,2 dtk). Pill hilang di ekor + jeda antar ayat.

## File acuan (md5 dari md5sum detik ini)
- MP4: [MD5] ([UKURAN] byte)
- karaoke-data.json: [MD5]
- project.json: [MD5]
- SUTRADARA-[SURAH]-V[1].md (disk): [MD5] ([N] baris)
- GATE-[SURAH]-V[1].md (disk): [MD5] ([N] baris)
- Contact sheet preview: [MD5] ([N] stills)

---

# CONTOH: angka ASLI build Quraish (106) v2, motlab + motion-cut (versi FIX)
# Build 2026-11-17. Jangan pakai angka ini buat surah lain, ini cuma contoh.

## Output (contoh)
- File: out/murrotal-quraish-v2-motlab-fix.mp4
- Ukuran: 42.950.561 byte, md5 c3e6fa644db7f15a34a653352b4de075
- Video: h264, 720x1280, 24fps, 1.146 frame (frame 0-1145), durasi 47,75 dtk
- Audio: aac, 48 kHz stereo, durasi 47,717 dtk (audio sumber utuh, tanpa potong)
- Perintah render: TMPDIR=$PWD/.tmp motlab render . out/murrotal-quraish-v2-motlab-fix.mp4 --scale 0.6667

## CATAT WAKTU (contoh)
- Jam mulai build: 2026-11-17 02:43:57 WIB
- Jam kelar build: 2026-11-17 02:54:08 WIB
- Total menit build: 10 menit 11 detik
- Jam mulai render run 1: 2026-11-17 03:12:05 WIB
- Jam run 1 gagal: 2026-11-17 03:12:06 WIB (ENOENT mkdtemp, folder .tmp belum ada; dibetulkan mkdir -p .tmp)
- Jam mulai render run 2: 2026-11-17 03:12:10 WIB
- Jam MP4 jadi (run 2): 2026-11-17 03:14:21 WIB
- Total menit render (run 2): 2 menit 11 detik
- TOTAL menit build + render: 12 menit 22 detik
- FIX ARAB_LINES: generate ulang 2026-11-17 07:53:47 WIB, render fix 07:54:14-07:55:20 WIB (~1 mnt 6 dtk), MP4 fix md5 c3e6fa64 (di atas)

## Verifikasi MP4 (contoh)
- ffprobe: 720x1280, 24fps, nb_frames 1146, durasi video 47,75 dtk, audio 47,717 dtk
- volumedetect: mean -15,0 dB, max -0,2 dB (v1: -15,2 / -1,5; mean hampir sama, max beda 1,3 dB karena puncak AAC, bukan defect)
- blackdetect: 0 frame hitam
- scdet (threshold 0.10): 129 entri, 45 di dalam jendela transisi, 84 di luar (skor maks di luar 1,951 di t=47.292, itu fade hitam ekor, bukan cut)
- Frame-diff penuh (streaming, grayscale 270x480, 1.146 frame): median mean 0,208, rata-rata 0,635, maks 36,06. Kandidat hard cut (mean>20 AND pct>30): 5 frame, SEMUANYA di dalam jendela transisi (D2 frame 285-286, D3 frame 520-521-523). 0 hard cut di luar transisi.
- Audio korelasi: lag terbaik 0 sample = 0,00 ms, korelasi global 1,0000, per jendela 5/5 lag 0 corr 1,0000 (tidak ada drift, audio identik sumber)

## Karaoke (contoh, dicek dari frame MP4 fix)
- Basmalah frame 63 (2,63 dtk): kata 3 aktif putih. Terjemahan 1 baris.
- Ayat 1 frame 228 (9,50 dtk): kata 6 aktif putih, tanda ۙ emas.
- Ayat 2 frame 408 (17,00 dtk): kata 9 aktif putih, tanda ۚ emas, salju kelihatan.
- Ayat 3 frame 590 (24,58 dtk): kata 12 aktif putih. Frame 592 (24,67 dtk): kata 13 aktif putih, kata 12 emas. Switch TEPAT di frame 592.
- Ayat 3 frame 600 (25,00 dtk): kata 13 aktif putih.
- Ayat 4 frame 1008 (42,00 dtk): kata 20 aktif putih di baris 2, Arab 2 baris rapi, tanda ەۙ + ࣖ emas.
- Jeda napas frame 948 (39,50 dtk): SEMUA kata emas, tidak ada kata aktif (BUG 3 betul).
- Ekor frame 1116 (46,50 dtk): pill HILANG, teks HILANG, cuma gambar oasis (BUG 4 betul).
- Frame terakhir 1144 (47,67 dtk): hampir hitam, fade to black jalan.
- Tanpa footer di frame mana pun. Shadow box rapi, tidak tutupi pill.

## Transisi shader (contoh)
- D1 frame 164 (6,83 dtk): LinearBlur, blend blur Ka'bah + gurun, tanpa pill/teks.
- D2 frame 285 (11,88 dtk): directionalwarp, gurun warp keluar diagonal + salju warp masuk, tanpa pill/teks.
- D3 frame 521 (21,71 dtk): fadecolor, frame gelap (fade lewat hitam), salju samar, tanpa pill/teks.
- D4 frame 694 (28,92 dtk): LinearBlur, blend blur Ka'bah malam + oasis, tanpa pill/teks.

## File acuan (contoh, md5 dari md5sum detik itu)
- MP4 fix: c3e6fa644db7f15a34a653352b4de075 (42.950.561 byte)
- MP4 lama (tidak ditimpa): f7cf1e15b1e5247d42adf5cbb1d22f9f (42.964.592 byte)
- karaoke-data.json: 921d0d9f554719e39385a1c625d55171
- project.json: 9c106dcab9e9cd037f1a323fa3396b8b
- SUTRADARA-MURROTAL-QURAISH-V2.md (disk): 7ebee301fe519f562da44b56a90f8d93 (152 baris)
- GATE-MURROTAL-QURAISH-V2.md (disk): 706ae0a8eef910faa2f6c8e2ce803833 (57 baris)
- Contact sheet preview: 094b0735e198c97938d1b4177e1cb30b (18 stills)

## CATAT WAKTU TEMPLATE (kerja bangun repo jadi-reciter ini, Builder 2)
- Jam mulai kerja template: 2026-11-18 00:47:26 WIB
- Jam kelar kerja template: 2026-11-18 01:09:05 WIB
- Total menit kerja template: 21 menit 39 detik
- Tes quickstart dari salinan bersih: LOLOS. Salinan tes ~/workspace/jadi-reciter-test/ (tanpa .git, audio.wav asli ditaruh di salinan tes saja). python3 build.py lolos (karaoke-data.json md5 921d0d9f sama dengan template). python3 gen_scenes.py lolos (scenes + project.json md5 sama dengan template, grep خَوْفٍ = 1, KB_END 1.3 di 5 adegan). Preview 13 stills: framing zoom 1.3 lolos (Ka'bah Basmalah + Ayat 3, kafilah Ayat 1, celah gunung Ayat 2, oasis + sungai Ayat 4 semua masih dalam frame); karaoke f1050/f1080 kata 21 putih, napas f948 semua emas. Render penuh 1 mnt 47 dtk (01:02:25-01:04:12 WIB). MP4 71.104.185 byte md5 92ed9d6b816a25f2dbd28880307fc02c, 720x1280 24fps 1.146 frame 47,75 dtk. Verifikasi: volumedetect -15,0/-0,2 dB, blackdetect 0, korelasi audio lag 0 r=1,0000 (5 jendela), frame-diff median 1,179, 5 kandidat hard cut semua di jendela transisi D2/D3, 0 di luar. Frame MP4: f592 ganti kata tepat, f1116 ekor bersih, f1144 hampir hitam (mean luma 11,6). Fallback gambar default teruji (ayat3.webp dihapus: peringatan muncul, scene pakai default.webp, lalu dipulihkan, md5 scene kembali sama). Salinan tes dihapus sesudah tes.
- Perubahan layout 2026-11-18 ~01:11-01:16 WIB (perintah Bos 00:51 + panduan Desain md5 968b9135): 5 webp contoh + default.webp pindah dari assets/ ke assets/images/; gen_scenes.py (IMG_SRC + cek fallback), README (layout + bagian gambar), SUTRADARA-TEMPLATE (§2 + §10) ikut diupdate. Aturan berhenti keras TIDAK dipakai (diganti koreksi Bos 00:52: default + peringatan, build tetap jalan). Tes quickstart ULANG dari salinan bersih LOLOS: build + gen_scenes md5 sama dengan template baru (scenes 01 b49845ae, 02 ca6cf9c0, 03 e124ae37, 04 2fd9dd75, 05 9a18f1a4), preview 13 stills, render 1 mnt 46 dtk (01:12:59-01:14:45 WIB), MP4 71.069.324 byte md5 3cd9bda69095c09940d2dc3e287a6381, verifikasi sama persis (volumedetect -15,0/-0,2, blackdetect 0, korelasi 1,0000, frame-diff median 1,18, 5 kandidat di jendela transisi), frame f592/f1050/f948 lolos. Salinan tes dihapus sesudah tes.

Murrotal QS. [NAMA SURAH] ([NOMOR]) v[1], motlab + motion-cut, catatan waktu
Build mulai: [ISI, WIB]
Build selesai: [ISI, WIB]
Total build: [ISI]
Render mulai: [ISI, WIB]
Render selesai: [ISI, WIB]
Total render: [ISI]
Total build + render: [ISI]
[CATATAN KOREKSI / REVISI kalau ada: batas kata, BUG, re-render, dengan jam + durasi]
[CATATAN PREVIEW: jam preview + acc sutradara]

CONTOH: angka ASLI build Quraish (106) v2, motlab + motion-cut (jangan pakai
angka ini buat surah lain, ini cuma contoh kerja).
Build mulai: 2026-11-17 02:43:57 WIB
Build selesai: 2026-11-17 02:54:08 WIB
Total build: 10 menit 11 detik
Render mulai (run 1): 2026-11-17 03:12:05 WIB
Render run 1 GAGAL instan (03:12:06 WIB): ENOENT mkdtemp, folder .tmp belum ada di proyek. Dibetulkan: mkdir -p .tmp.
Render mulai (run 2): 2026-11-17 03:12:10 WIB
Render selesai (run 2): 2026-11-17 03:14:21 WIB
Total render (run 2): 2 menit 11 detik
Total build + render: 12 menit 22 detik (build 10 mnt 11 dtk + render 2 mnt 11 dtk)
Output: out/murrotal-quraish-v2-motlab.mp4 (bukan nama -720p, motlab pakai nama proyek)

FIX ARAB_LINES (contoh, 2026-11-17):
Fix + generate ulang: 07:53:34-07:53:47 WIB.
Still cek f1050: ~07:54 WIB.
Arsip scoring lama: 07:54:08 WIB.
Render: ~1 mnt 6 dtk (07:54:14-07:55:20 WIB).
Verifikasi: 07:55-07:57 WIB.
Output fix: out/murrotal-quraish-v2-motlab-fix.mp4, md5 c3e6fa644db7f15a34a653352b4de075.

CATAT WAKTU TEMPLATE (kerja bangun repo jadi-reciter ini, Builder 2):
Kerja template mulai: 2026-11-18 00:47:26 WIB
Kerja template selesai: 2026-11-18 01:09:05 WIB
Total kerja template: 21 menit 39 detik
Tes quickstart dari salinan bersih: LOLOS. Salinan tes ~/workspace/jadi-reciter-test/ (tanpa .git, audio.wav asli ditaruh di salinan tes saja). python3 build.py lolos (karaoke-data.json md5 921d0d9f sama dengan template). python3 gen_scenes.py lolos (scenes + project.json md5 sama dengan template, grep خَوْفٍ = 1, KB_END 1.3 di 5 adegan). Preview 13 stills: framing zoom 1.3 lolos (Ka'bah Basmalah + Ayat 3, kafilah Ayat 1, celah gunung Ayat 2, oasis + sungai Ayat 4 semua masih dalam frame); karaoke f1050/f1080 kata 21 putih, napas f948 semua emas. Render penuh 1 mnt 47 dtk (01:02:25-01:04:12 WIB). MP4 71.104.185 byte md5 92ed9d6b816a25f2dbd28880307fc02c, 720x1280 24fps 1.146 frame 47,75 dtk. Verifikasi: volumedetect -15,0/-0,2 dB, blackdetect 0, korelasi audio lag 0 r=1,0000 (5 jendela), frame-diff median 1,179, 5 kandidat hard cut semua di jendela transisi D2/D3, 0 di luar. Frame MP4: f592 ganti kata tepat, f1116 ekor bersih, f1144 hampir hitam (mean luma 11,6). Fallback gambar default teruji (ayat3.webp dihapus: peringatan muncul, scene pakai default.webp, lalu dipulihkan, md5 scene kembali sama). Salinan tes dihapus sesudah tes.

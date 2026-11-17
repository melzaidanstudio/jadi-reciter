# Tabel karaoke §5 (salinan verbatim SUTRADARA Quraish v2, 21 kata)
# Dibaca build.py (parse_karaoke) buat bangun karaoke-data.json.
# JANGAN retype tabel ini: batas kata 12/13 sudah TERKOREKSI ke 24.68 (f 592),
# kata 1 start 0.31, kata 21 end 45.19. Kalau ganti surah, ganti SELURUH tabel
# dengan tabel terverifikasi surah baru (lihat templates/SUTRADARA-TEMPLATE.md §5).

| No | Ayat | Kata tampil | Start (dtk) | End (dtk) | f_start | t_frame (dtk) | Token Whisper yang digabung |
|---|---|---|---|---|---|---|---|
| 1 | Basmalah | بِسْمِ | 0.31 | 0.90 | 7 | 0.2917 | بسم 0.00-0.90; start dikoreksi 0.31 (timing-ayat.md, hening 0-0.31) |
| 2 | Basmalah | اللَّهِ | 0.90 | 1.90 | 21 | 0.8750 | الله 0.90-1.90 |
| 3 | Basmalah | الرَّحْمَٰنِ | 1.90 | 3.16 | 45 | 1.8750 | الرحمن 1.90-3.16 |
| 4 | Basmalah | الرَّحِيمِ | 3.16 | 6.16 | 75 | 3.1250 | الرحيم 3.16-6.16 |
| 5 | Ayat 1 | لِاِيْلٰفِ | 7.56 | 9.22 | 181 | 7.5417 | GABUNG لإيلى 7.56-8.96 + في 8.96-9.22 |
| 6 | Ayat 1 | قُرَيْشٍ | 9.22 | 11.58 | 221 | 9.2083 | قرش 9.22-11.58 (tanda ۙ di akhir ayat tetap tampil, selalu emas) |
| 7 | Ayat 2 | اٖلٰفِهِمْ | 12.20 | 14.06 | 292 | 12.1667 | GABUNG إيلى 12.20-13.38 + فيهم 13.38-14.06 |
| 8 | Ayat 2 | رِحْلَةَ | 14.06 | 15.08 | 337 | 14.0417 | رحلة 14.06-15.08 |
| 9 | Ayat 2 | الشِّتَاۤءِ | 15.08 | 17.96 | 361 | 15.0417 | الشتاء 15.08-17.96 |
| 10 | Ayat 2 | وَالصَّيْفِ | 17.96 | 21.46 | 431 | 17.9583 | والصييف 17.96-21.46 (tanda ۚ di akhir ayat tetap tampil, selalu emas) |
| 11 | Ayat 3 | فَلْيَعْبُدُوْا | 22.00 | 23.70 | 528 | 22.0000 | فاليعبد 22.00-23.70 |
| 12 | Ayat 3 | رَبَّ | 23.70 | 24.68 | 568 | 23.6667 | TERKOREKSI (Builder 2, verifikasi VideoStory): batas token Whisper 25.12 SALAH, "hā" terdengar 24.70. Batas baru 24.68 (f 592). Durasi 0,98 dtk. |
| 13 | Ayat 3 | هٰذَا | 24.68 | 25.64 | 592 | 24.6667 | TERKOREKSI: start 24.68 (f 592). Durasi 0,96 dtk. Stills preview: 24.60 kata 12 putih, 24.70 kata 13 putih. |
| 14 | Ayat 3 | الْبَيْتِ | 25.64 | 28.44 | 615 | 25.6250 | البيت 25.64-28.44 (tanda ۙ di akhir ayat tetap tampil, selalu emas) |
| 15 | Ayat 4 | الَّذِيْٓ | 29.44 | 30.46 | 706 | 29.4167 | الذي 29.44-30.46 |
| 16 | Ayat 4 | اَطْعَمَهُمْ | 30.46 | 33.84 | 731 | 30.4583 | أطعمهم 30.46-33.84 |
| 17 | Ayat 4 | مِّنْ | 33.84 | 35.58 | 812 | 33.8333 | من 33.84-35.58 |
| 18 | Ayat 4 | جُوْعٍ | 35.58 | 38.48 | 853 | 35.5417 | جور 35.58-38.48 (tanda ەۙ sesudah kata ini tetap tampil, selalu emas) |
| 19 | Ayat 4 | وَّاٰمَنَهُمْ | 40.36 | 41.76 | 968 | 40.3333 | وآمنهم 40.36-41.76 (sesudah jeda napas 38.48-40.36, tidak ada kata aktif di jeda) |
| 20 | Ayat 4 | مِّنْ | 41.76 | 43.16 | 1002 | 41.7500 | من 41.76-43.16 |
| 21 | Ayat 4 | خَوْفٍ | 43.16 | 45.19 | 1035 | 43.1250 | خور 43.16-44.30; end dikoreksi 45.19 (timing-ayat.md, suara jalan sampai 45.19; tanda ࣖ di akhir ayat tetap tampil, selalu emas) |

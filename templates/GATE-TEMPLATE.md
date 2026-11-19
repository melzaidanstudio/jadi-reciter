# GATE TEMPLATE: Murrotal QS. [NAMA SURAH] ([NOMOR]) v[1], motlab + motion-cut
# Sutradara: [NAMA], [TANGGAL] WIB
# SUTRADARA: SUTRADARA-[SURAH]-V[1].md, md5 [MD5], [N] baris, 0 em dash.
# Perintah [BOS/CEO] via [JALUR]. [Revisi dari v1 / video baru], engine motlab.
# Verdict: [GATE OK / BELUM OK + blocker]. Build + render oleh Builder sesudah preview sheet acc.
# CARA PAKAI: isi semua [PLACEHOLDER] + centang [x] kalau sudah diverifikasi dari disk.
# Satu item bertanda [ ] cuma dicek di preview, bukan blocker GATE.

## Cek input (semua diverifikasi sutradara dari disk)
- [ ] [N] gambar sama dengan [SUMBER]: [DAFTAR FILE + UKURAN BYTE]. Ada di [FOLDER]/.
- [ ] Audio utuh: audio.wav md5 [MD5], [DURASI] dtk, [NAMA QARI]. Dipakai utuh, tanpa potong, tanpa dipercepat.
- [ ] Teks verbatim: teks-[SURAH].md md5 [MD5]. Arab + transliterasi + terjemahan. Build ambil programmatic, jangan retype.
- [ ] Timing ayat: timing-ayat.md md5 [MD5]. [DAFTAR RENTANG]. Jeda napas [AYAT] [RENTANG] di tengah ayat.
- [ ] transcript.json md5 [MD5], [N] segmen, [N] token kata Whisper. Peta karaoke [N] kata dibangun dari token ini (§5 SUTRADARA).

## Cek tanya gambar (jalur A / jalur B, perintah Dewa 2026-11-18)
- [ ] Langkah tanya JALAN sebelum generate: pilihan user tercatat di SUTRADARA (§17): jalur A atau jalur B (+ tema yang di-input kalau B). Kalau AI yang dipakai user TIDAK BISA generate gambar, langkah tanya boleh dilewati (gambar dari upload user).
- [ ] Kalau pilihan TIDAK tercatat di SUTRADARA (§17) tapi gambar sudah ada di assets/images/, GATE GAGAL. Tanya dulu ke user, baru generate ulang.
- [ ] Jalur A: tiap gambar sesuai cerita/arti ayatnya (cek per ayat di preview, ikut panduan gambar §1 sampai §4).
- [ ] Jalur B: SEMUA gambar mengikuti tema yang tercatat di SUTRADARA, BUKAN arti ayat. Cek per gambar di preview: isi gambar ikut tema, gaya konsisten satu video, antislop (subjek jelas, komposisi kuat, tidak generik). Gambar yang ikut arti ayat di jalur B = SALAH, generate ulang.
- [ ] Jalur B: teks Kemenag, karaoke, dan timing TIDAK berubah ikut tema. Cek: teks Arab + transliterasi + terjemahan tetap verbatim, peta karaoke tetap sama, timing ayat tetap sama.
- [ ] Satu video cuma satu jalur: tidak ada gambar jalur A tercampur di video jalur B, atau sebaliknya.

## Cek potong ayat panjang (perintah Dewa 2026-11-18)
- [ ] Ayat yang dipotong tercatat di SUTRADARA §7 + §18: [DAFTAR AYAT + JUMLAH POTONGAN]. Maksimal 3 potongan per ayat.
- [ ] Titik potong di batas frasa yang natural (tanda berhenti / batas klausa / jeda napas tengah ayat), BUKAN tengah kata, BUKAN tengah frasa. Kata terakhir tiap potongan + kata pertama potongan berikut tercatat.
- [ ] Karaoke nyambung: nomor kata lanjut terus antar potongan, f_start/f_end tidak berubah, tidak ada kata hilang, tidak ada kata diulang, tidak ada tumpang tindih (cek karaoke-data.json + peta §5).
- [ ] Tiap potongan gambar sendiri, gambar tiap potongan beda. Jalur A: gambar potongan sesuai cerita bagian ayat itu. Jalur B: gambar potongan sesuai tema (§17).
- [ ] Transisi antar potongan SELALU dissolve (fade) 0,5 dtk, di project.json adegan yang dimasuki. Bukan directionalwarp, bukan fadecolor.
- [ ] Teks tiap potongan cuma kata-kata potongan itu; pill menunjukkan bagian (Ayat n / [JUMLAH] (bagian k / K)).
- [ ] Hitungan TOTAL: jumlah TOTAL semua adegan (termasuk potongan) kurang semua transisi x 0,5 dtk = durasi video. Cocok ([DURASI AUDIO] dtk).

## Cek peta karaoke [N] kata (WAJIB, terverifikasi dari disk)
- [ ] [N] kata tampil ([PER AYAT]). Tidak ada tumpang tindih, semua durasi positif.
- [ ] Gabung token Whisper: [DAFTAR GABUNGAN]. Batas gabung bersih (token bersambung tanpa jeda).
- [ ] Koreksi batas segmen dari timing-ayat.md: kata 1 start [BARU] (bukan [LAMA]), kata [TERAKHIR] end [BARU] (bukan [LAMA]).
- [ ] Snap frame 24fps: kata aktif di frame floor(start x 24), highlight ganti paling lambat 41,67 ms sebelum awal kata, tidak pernah telat.
- [ ] Jeda napas [AYAT] ([RENTANG]) kosong: tidak ada kata aktif di jeda.
- [ ] Tanda akhir ayat ([DAFTAR]) bukan kata, tetap tampil tapi selalu emas, tidak pernah putih.
- [ ] Transliterasi + terjemahan tidak karaoke, tetap statis.
- [ ] Batas [AYAT] [KATA A] / [KATA B] TERKOREKSI ke [BARU] (f [N]), terbukti akustik ([BUKTI]) + stills preview. Durasi kata [A] [X] dtk, kata [B] [X] dtk, seimbang. Highlight ganti frame [N], tidak pernah telat.

## Cek shadow box (ikut referensi Ad-Dhuha)
- [ ] Referensi dibaca langsung: [PATH], [UKURAN] byte, QS. [SURAH] Ayat [N]. Pill atas, kotak rounded hitam transparan + border tipis, Arab emas + kata aktif putih, terjemahan putih di dalam kotak, tanpa footer.
- [ ] Spesifikasi kotak di SUTRADARA §6: x 60-1020, isi rgba(0,0,0,0.55), border rgba(255,255,255,0.35) 2 px, radius 24 px, padding 36 px vertikal + 40 px horizontal, lebar dalam 880 px, ukuran ikut tinggi teks tiap ayat, jangan tutupi pill.
- [ ] BUG 3 (f_end): f_end = floor(end kata sendiri x 24), BUKAN f_start kata berikut. Kata [N] f_end [N] (bukan [N]). Jeda napas [RENTANG] tidak ada kata aktif, semua emas (terbukti stills video [WAKTU] + karaoke-data.json, semua f_start/f_end dicek sutradara, tidak ada tumpang tindih).
- [ ] BUG 4 (pill ikut fade teks): pill opacity sama kayak blok teks (fade 0,2 dtk), hilang di ekor + jeda antar ayat. Terbukti stills video [WAKTU]: pill HILANG, teks HILANG, cuma gambar.
- [ ] Warna teks di kotak: Arab emas #E8C766 + kata aktif putih #FFFFFF, transliterasi putih pudar rgba(255,255,255,0.85), terjemahan putih #FFFFFF.
- [ ] Arab [AYAT] [N] baris, terjemahan maksimal 2 baris, [AYAT LAIN] Arab 1 baris.

## Cek tanpa footer
- [ ] SUTRADARA tulis jelas: HAPUS footer "Qur'an Kemenag", tidak ada di frame mana pun. GATE cek preview: cari footer di semua stills, harus 0.

## Cek adegan + transisi + audio
- [ ] [N] adegan, satu halaman motlab per adegan, Ken Burns zoom-in (1,00x ke 1.3x, linear) + pan 20 px per adegan.
- [ ] TOTAL adegan: [X] + [X] + ... = [TOTAL] dtk, kurang [N] transisi x 0,5 dtk = [DURASI] dtk. Cocok ([DURASI AUDIO] dtk).
- [ ] Transisi bernama 0,5 dtk tiap pindah ayat: [DAFTAR D1-DN + JENIS]. Di tengah jeda antar ayat. Ditulis di project.json adegan yang dimasuki.
- [ ] Partikel + cahaya per adegan: [DAFTAR PER ADEGAN].
- [ ] Audio: satu file audio.wav, start 0, volume 1.0. Tanpa BGM, tanpa musik, tanpa SFX.
- [ ] Ekor: teks hilang [RENTANG], gambar tetap, fade hitam 0,5 dtk terakhir. Tanpa end card, tanpa CTA.

## Cek DOT + PARALLAX (SUTRADARA §16)
- [ ] DOT: titik putih 3 px, jarak 24 px, stagger 12 px, opacity 0.06, ~3.600 titik, ikut lapis gambar. Tidak ada titik di teks.
- [ ] PARALLAX: pan gambar ~20 px per adegan ke arah tabel, zoom 1.3 semua adegan, partikel drift ~30 px berlawanan, teks drift ±15 px sinusoidal kembali 0 di akhir adegan, tidak ada elemen statis.
- [ ] Zoom 1.3 framing/crop: cek per adegan di preview, subjek utama masih di frame di zoom maks ([DAFTAR SUBJEK PER ADEGAN]). Kalau terpotong, laporkan ke sutradara, jangan ubah nilai 1.3.
- [ ] Transisi: D1 + D4 blend lembut (fade), D2 warp diagonal, D3 dip hitam, 0 hard cut di luar transisi.

## Cek format + engine
- [ ] project.json fps 24, halaman 1080x1920, render --scale 0.6667 jadi 720x1280. Jumlah frame: [DURASI] x 24 = [HITUNG]. Frame render [CEIL] (frame 0-[CEIL-1]). Angka pasti dari render, tulis di RENDER.md.
- [ ] Proyek BARU [PATH PROYEK]/, jangan timpa proyek lama.
- [ ] Chrome wrapper --no-sandbox, TMPDIR di /home (~/.motlab-tmp). motlab terpasang, doctor OK.
- [ ] RENDER [DIPERINTAHKAN BOS SECARA EKSPLISIT / TUNGGU ACC BOS].
- [ ] Perbandingan [DAFTAR VERSI]: Builder WAJIB catat WAKTU build + render penuh versi ini pakai angka di RENDER.md (jam mulai/selesai + total menit build, render, total). Seksi CATAT WAKTU §15 di SUTRADARA sediakan tempatnya. Laporan akhir versi ini HARUS bawa angka itu.

## Rencana preview (aturan motion-cut, preview dulu sebelum render penuh)
- [ ] Builder buat stills + contact sheet, kirim ke sutradara SEBELUM render penuh. Sutradara acc dulu baru render penuh.
- Waktu stills (waktu video, dtk): [DAFTAR 12 TITIK, ikut SUTRADARA §11].
- Yang dicek sutradara di preview: kata aktif putih di frame yang benar, shadow box rapi + tidak tutupi pill, Arab [N] baris tidak meluber, terjemahan maksimal 2 baris, tanpa footer di frame mana pun, gambar per ayat benar (jalur A: sesuai cerita ayat; jalur B: sesuai tema yang tercatat), Ken Burns + pan jalan, partikel + cahaya ada di tiap adegan, transisi bernama terlihat, batas [AYAT] verifikasi telinga, DOT + framing zoom 1.3.

## Blocker: [N]
- [DAFTAR BLOCKER, atau "0" kalau semua input ada + terverifikasi.]

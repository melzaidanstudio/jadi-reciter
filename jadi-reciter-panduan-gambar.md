# PANDUAN GENERATE GAMBAR, TEMPLATE JADI-RECITER

Panduan buat siapa pun yang mau ganti gambar di template video murrotal ini.
Template: video murrotal 9:16, 720x1280, 24fps, mesin motlab + motion-cut.
Satu gambar per adegan, teks Arab tampil sebagai karaoke di atas gambar, bukan di dalam gambar.

File referensi: `~/workspace/murrotal-quraish-v2-motlab/assets/`
(bismillah + ayat1-4, contoh kerja QS. Quraish v2, CEO 10/10).

---

## 1. ATURAN WAJIB

Lima aturan ini tidak boleh dilanggar. Kalau satu dilanggar, gambar ditolak, generate ulang.

1. **Generate AI, bukan stok, bukan comot.** Tiap gambar ayat WAJIB dibuat dengan generator gambar AI dari prompt yang ditulis buat ayat itu. Dilarang pakai foto stok, gambar hasil pencarian, screenshot video orang, atau gambar dari internet. Alasannya: gaya harus seragam satu video, dan gambar harus bercerita sesuai ayat, bukan gambar generik yang kebetulan mirip.
2. **Isi ngikutin cerita dan arti ayat.** Gambar bukan hiasan. Satu ayat = satu adegan yang menunjukkan apa yang ayat itu ceritakan. Baca dulu terjemahan ayat dari Kemenag (quran.kemenag.go.id), tentukan adegan intinya, baru tulis prompt. Kalau penonton bisu melihat gambarnya saja sudah bisa menebak isi ayatnya, gambar itu benar.
3. **Gaya konsisten satu video.** Semua gambar dalam satu video pakai gaya yang sama: gaya lukisan sinematik gelap emas (lihat bagian 3). Jangan campur gaya: satu gambar lukisan, satu gambar foto, satu gambar kartun. Penonton harus merasa semua gambar dari dunia yang sama.
4. **TANPA teks di gambar.** Tidak ada huruf Arab, huruf Latin, angka, papan nama, logo, merek, atau pelat nomor yang terbaca di gambar. Teks Arab tampil sebagai karaoke di atas gambar saat video jalan, jadi gambar harus bersih dari tulisan apa pun. Periksa dengan mata sendiri sesudah generate, jangan percaya prompt saja. Generator sering menyelipkan teks sendiri: logo di jaket, tulisan di boks, pelat nomor karangan, papan toko. Kalau ada yang terbaca, generate ulang.
5. **Ukuran 1152x2048, format WebP, 9:16.** Semua gambar vertikal 9:16, 1152x2048 piksel, simpan sebagai WebP. Jangan kirim ukuran lain, jangan kirim JPG atau PNG.

Aturan tambahan dari pengalaman:

- **Jangan gambar wajah nabi atau sahabat.** Adegan cukup lewat tempat, benda, rombongan dari jauh, atau orang biasa dari belakang. Kalau ayat bercerita tentang manusia, tunjukkan manusianya sebagai figur biasa, bukan tokoh bernama.
- **Ayat yang artinya sama, gambarnya harus beda.** Kalau dua ayat mengulang pesan yang sama, jangan pakai adegan yang sama dua kali. Bedakan suasana, bedakan shot, dan buat eskalasi: yang kedua lebih terang, lebih lapang, lebih kuat. Contoh di QS. Al-Insyirah ayat 5 dan 6 (dua-duanya "bersama kesulitan ada kemudahan"): ayat 5 kereta malam padat sesak gelap, ayat 6 peron stasiun matahari terbit lapang terang.
- **Parallax-ready.** Gambar harus punya lapisan depan, tengah, dan belakang yang jelas terpisah, supaya bisa digerakkan berlapis di video. Jangan gambar satu bidang datar tanpa kedalaman.

---

## 2. CONTOH KERJA: 5 GAMBAR QS. QURAISH V2

Semua gambar di bawah ini WebP 1152x2048, gaya lukisan sinematik gelap emas.
Sumber teks: Al-Qur'an Kemenag, quran.kemenag.go.id, surah 106.

| File | Ukuran | md5 |
|---|---|---|
| `bismillah.webp` | 424.386 byte | f54b6aba |
| `ayat1.webp` | 446.806 byte | 49ec0208 |
| `ayat2.webp` | 500.576 byte | 714c5893 |
| `ayat3.webp` | 333.516 byte | c0942475 |
| `ayat4.webp` | 874.814 byte | 647362a6 |

### Basmalah, `bismillah.webp`

- Terjemahan: "Dengan nama Allah Yang Maha Pengasih, Maha Penyayang."
- Isi gambar: Ka'bah di Masjidil Haram saat fajar, kiswah hitam bersulam emas, pintu emas, menara-menara, pegunungan di belakang, cahaya menembus awan gelap dari atas.
- Kenapa cocok: Basmalah adalah pembuka, menyebut nama Allah dan sifat kasih sayang-Nya. Gambarnya membuka video dengan Rumah Allah di bawah cahaya yang turun dari langit. Cahaya dari atas itu visual dari "Maha Pengasih, Maha Penyayang": rahmat yang turun. Gambar ini juga jadi cover video, bukan adegan ayat.

### Ayat 1, `ayat1.webp`

- Terjemahan: "Disebabkan oleh kebiasaan orang-orang Quraisy,"
- Isi gambar: Rombongan kafilah unta yang panjang menyeberangi lembah gurun keemasan saat matahari terbit, unta bermuatan, musafir berjubah, tebing batu di kiri kanan.
- Kenapa cocok: Ayat ini bicara tentang kebiasaan (ili, tradisi dagang) kaum Quraisy: mereka biasa bepergian berdagang. Gambarnya menunjukkan kebiasaan itu sendiri, kafilah dagang yang sedang berjalan. Bukan kota Mekkah, bukan Ka'bah, tapi perjalanan. Itulah isi ayatnya.

### Ayat 2, `ayat2.webp`

- Terjemahan: "(yaitu) kebiasaan mereka bepergian pada musim dingin dan musim panas (sehingga mendapatkan banyak keuntungan),"
- Isi gambar: Kafilah unta yang sama mendaki celah gunung bersalju saat fajar, salju di mana-mana, langit biru dingin, matahari terbit keemasan di ujung lembah.
- Kenapa cocok: Ayat ini merinci kebiasaan ayat 1: perjalanan musim dingin dan musim panas. Gambarnya mengambil sisi musim dinginnya: salju, dingin, pendakian berat. Pasangan dengan ayat 1: ayat 1 gurun hangat keemasan (musim panas, ke Syam), ayat 2 salju biru dingin (musim dingin, ke Yaman). Dua gambar berdampingan langsung menunjukkan dua musim yang ayat ini sebut. Ini contoh terbaik aturan "satu ayat, satu adegan": jangan gabung dua musim dalam satu gambar, pisah jadi dua adegan.

### Ayat 3, `ayat3.webp`

- Terjemahan: "maka hendaklah mereka menyembah Tuhan (pemilik) rumah ini (Ka'bah)"
- Isi gambar: Ka'bah di malam hari di bawah langit berbintang, jamaah duduk berdoa menghadap Ka'bah, lentera-lentera, lengkung masjid di kiri kanan.
- Kenapa cocok: Ayat ini perintah: sembahlah Tuhan pemilik rumah ini. Gambarnya menunjukkan perintah itu sedang dilakukan: orang-orang beribadah menghadap Ka'bah. Ka'bah di tengah, manusia menghadap ke sana. Bandingkan dengan Basmalah: di sana Ka'bah sendiri yang jadi pusat; di sini manusianya yang beribadah. Gambar yang sama (Ka'bah) dipakai dua kali tapi adegannya beda: cover = Ka'bah + cahaya, ayat 3 = Ka'bah + jamaah berdoa.

### Ayat 4, `ayat4.webp`

- Terjemahan: "yang telah memberi mereka makanan untuk menghilangkan lapar dan mengamankan mereka dari rasa takut."
- Isi gambar: Lembah oasis hijau subur, pohon kurma berbuah lebat, sungai mengalir, pohon delima dan jeruk, kota berdinding di kejauhan di bawah cahaya keemasan, gunung melindungi lembah.
- Kenapa cocok: Ayat ini punya dua janji: diberi makan (lawan lapar) dan diamankan (lawan takut). Gambarnya menunjukkan dua-duanya sekaligus: makanan = kurma, buah, air sungai yang melimpah di depan; keamanan = kota yang terlindung di lembah, dikelilingi gunung. Oasis di tengah gurun itu sendiri adalah gambaran rezeki dan perlindungan.

---

## 3. PANDUAN PROMPT PER AYAT

### Struktur prompt

Tiap prompt gambar ayat disusun dari 6 bagian, urut seperti ini:

1. **Subjek + adegan.** Satu kalimat: siapa atau apa, sedang apa, di mana. Contoh: "Rombongan kafilah unta menyeberangi lembah gurun saat matahari terbit."
2. **Suasana.** Satu kalimat: terang atau gelap, hangat atau dingin, tenang atau berat. Contoh: "Suasana hangat keemasan, debu beterbangan, perjalanan panjang."
3. **Gaya.** Selalu kalimat yang sama di semua ayat: "Cinematic dark gold painting like the reference image, vertical 9:16, no watermark." Gaya ini yang bikin 5 gambar Quraish terasa satu video.
4. **Larangan teks.** Selalu kalimat yang sama di semua ayat: "No text, no letters, no brand names, no signboards anywhere in the image." Tambahkan larangan khusus kalau adegannya rawan: kendaraan = "no license plate", toko = "no big readable signboard", pakaian kerja = "plain jacket, no logos".
5. **Kedalaman parallax.** Selalu kalimat yang sama di semua ayat: "Clear layered depth: a distinct foreground, middle ground, and background, separable layers for parallax motion."
6. **Gambar referensi gaya.** Sertakan satu gambar Quraish v2 sebagai referensi gaya di tiap generate. Pilih yang suasananya paling dekat: adegan siang hangat pakai `ayat1.webp`, adegan dingin atau malam pakai `ayat2.webp`, adegan masjid atau ibadah pakai `bismillah.webp` atau `ayat3.webp`.

### Template prompt siap isi

```
[ADEGAN: subjek + apa yang terjadi + di mana],
[SUASANA: terang/gelap, hangat/dingin, tenang/berat].
No text, no letters, no brand names, no signboards anywhere in the image.
[LARANGAN KHUSUS kalau ada, contoh: plain taxi, no logo, no license plate.]
Cinematic dark gold painting like the reference image, vertical 9:16, no watermark.
Clear layered depth: a distinct foreground, middle ground, and background,
separable layers for parallax motion.
```

### Cara jaga konsistensi gaya antar ayat

- Pakai **satu gambar referensi gaya yang sama** untuk semua ayat dalam satu video, atau satu referensi per suasana (hangat, dingin, masjid) seperti di atas. Jangan ganti-ganti referensi tiap ayat.
- Pakai **kalimat gaya yang sama persis** di semua prompt (bagian 3 dan 5 di atas). Jangan ubah-ubah kata sifatnya.
- Pakai **satu generator yang sama** untuk semua gambar satu video. Generator yang beda punya "tangan" yang beda.
- **Cek berdampingan.** Sesudah semua gambar jadi, buka semuanya sekaligus dan lihat: apakah terasa satu dunia? Kalau satu gambar terasa beda sendiri (lebih terang, lebih kartun, lebih foto), generate ulang gambar itu dengan referensi yang sama seperti yang lain.
- **Satu adegan per ayat.** Jangan masukkan dua adegan dalam satu gambar (contoh: jangan gambar musim dingin dan musim panas sekaligus). Kalau satu ayat menyebut dua hal, pilih yang paling kuat, atau pisah jadi dua ayat kalau ayatnya memang dua.

### Cek akhir sebelum gambar dinyatakan jadi

Buka gambarnya, lihat langsung, jawab 5 pertanyaan ini:

1. Apakah isi gambar sesuai arti ayatnya? (Bukan sekadar bagus.)
2. Apakah ada teks, logo, merek, atau pelat nomor yang terbaca? (Periksa jaket, boks, helm, papan, pelat. Kalau ada, generate ulang.)
3. Apakah gayanya sama dengan gambar lain di video ini?
4. Apakah ada lapisan depan, tengah, dan belakang yang jelas? (Parallax-ready.)
5. Apakah ukurannya 1152x2048 WebP?

Kalau satu jawaban "tidak", gambar belum jadi.

---

## 4. CARA GANTI SURAH

Langkah ganti 5 gambar Quraish dengan gambar surah baru. Jangan ubah struktur folder, cuma ganti isinya.

1. **Baca surah baru dari Kemenag.** Buka quran.kemenag.go.id, baca teks Arab, transliterasi, dan terjemahan tiap ayat. Catat arti tiap ayat dalam satu kalimat pendek. Jangan percaya ingatan atau transkrip otomatis.
2. **Tentukan satu adegan per ayat.** Untuk tiap ayat, tulis satu adegan: subjek + apa yang terjadi + di mana + suasana. Kalau dua ayat artinya sama, bedakan adegannya dan buat eskalasi (lihat aturan di bagian 1). Tulis daftar adegan ini dulu sebelum generate apa pun.
3. **Tulis prompt per ayat.** Pakai template di bagian 3. Satu prompt per ayat, satu generate per ayat. Simpan promptnya, supaya kalau perlu generate ulang, hasilnya konsisten.
4. **Generate dan cek.** Generate tiap gambar, lalu cek dengan 5 pertanyaan di bagian 3. Gambar yang gagal (ada teks, gaya beda, adegan salah) generate ulang, jangan dipaksakan.
5. **Simpan dengan nama yang sama.** Nama file mengikuti pola template: `bismillah.webp`, `ayat1.webp`, `ayat2.webp`, dan seterusnya sesuai jumlah ayat surah baru. Letakkan di folder `assets/images/`, timpa file Quraish yang lama. Kalau jumlah ayat beda, tambah atau kurangi file sesuai jumlah ayat, dan sesuaikan daftarnya di `gen_scenes.py`.
6. **Perbarui teks + timing + karaoke.** Ganti `teks-quraish.md` dengan teks surah baru (Arab + transliterasi + terjemahan dari Kemenag), perbarui `timing-ayat.md` dan `karaoke-data.json` dari audio murrotal surah baru. Gambar saja yang diganti tidak cukup, teks dan timing harus ikut surah baru.
7. **Verifikasi akhir.** Cek md5 dan ukuran tiap file dari disk, buka semua gambar berdampingan, pastikan gaya konsisten dan tidak ada teks. Baru serahkan buat di-score.

---

## 5. BAGIAN README (TEKS SIAP TEMPEL)

Bagian di bawah ini siap ditempel ke README template oleh Builder 2. Jangan ubah isinya tanpa sepengetahuan Desain.

```markdown
## Gambar ayat

Tiap adegan video memakai satu gambar latar, dibuat dengan generator gambar AI
dari prompt yang ditulis khusus buat ayat itu. Gambar bukan stok dan bukan comot
dari internet.

### Aturan wajib

1. **Generate AI.** Tiap gambar ayat dibuat dengan generator gambar AI dari
   prompt buat ayat itu. Dilarang pakai foto stok, gambar hasil pencarian,
   screenshot, atau gambar dari internet.
2. **Ngikutin arti ayat.** Satu ayat = satu adegan yang menunjukkan apa yang
   ayat itu ceritakan. Baca dulu terjemahan ayat dari Kemenag
   (quran.kemenag.go.id), tentukan adegan intinya, baru tulis prompt.
3. **Gaya konsisten.** Semua gambar satu video pakai gaya yang sama: lukisan
   sinematik gelap emas. Jangan campur gaya dalam satu video.
4. **Tanpa teks di gambar.** Tidak ada huruf, angka, logo, merek, atau pelat
   nomor yang terbaca di gambar. Teks Arab tampil sebagai karaoke di atas
   gambar saat video jalan. Periksa gambarnya langsung sesudah generate.
5. **Ukuran 1152x2048, WebP, 9:16.** Semua gambar vertikal 9:16,
   1152x2048 piksel, format WebP.
6. **Parallax-ready.** Gambar harus punya lapisan depan, tengah, dan belakang
   yang jelas terpisah, supaya bisa digerakkan berlapis di video.
7. **Ayat yang artinya sama, gambarnya harus beda.** Bedakan suasana dan
   shot, buat eskalasi: yang kedua lebih terang, lebih lapang, lebih kuat.

### Contoh kerja: QS. Quraish (106)

| File | Ayat | Adegan |
|---|---|---|
| `assets/images/bismillah.webp` | Basmalah | Ka'bah di bawah cahaya dari langit, pembuka video |
| `assets/images/ayat1.webp` | Ayat 1 | Kafilah unta di gurun keemasan, kebiasaan dagang Quraisy |
| `assets/images/ayat2.webp` | Ayat 2 | Kafilah di celah gunung bersalju, perjalanan musim dingin |
| `assets/images/ayat3.webp` | Ayat 3 | Jamaah berdoa menghadap Ka'bah di malam berbintang |
| `assets/images/ayat4.webp` | Ayat 4 | Oasis hijau subur, makanan melimpah dan kota yang aman |

Ayat 1 dan ayat 2 adalah pasangan: ayat 1 gurun hangat keemasan (musim panas),
ayat 2 salju biru dingin (musim dingin). Dua musim yang disebut ayat 2
ditunjukkan lewat dua adegan, bukan satu gambar.

### Struktur prompt

```
[ADEGAN: subjek + apa yang terjadi + di mana],
[SUASANA: terang/gelap, hangat/dingin, tenang/berat].
No text, no letters, no brand names, no signboards anywhere in the image.
[LARANGAN KHUSUS kalau ada, contoh: plain taxi, no logo, no license plate.]
Cinematic dark gold painting like the reference image, vertical 9:16,
no watermark.
Clear layered depth: a distinct foreground, middle ground, and background,
separable layers for parallax motion.
```

Sertakan satu gambar Quraish di atas sebagai referensi gaya di tiap generate,
pilih yang suasananya paling dekat dengan adegan baru.

### Cara ganti surah

1. Baca surah baru dari Kemenag, catat arti tiap ayat dalam satu kalimat.
2. Tentukan satu adegan per ayat, tulis dulu daftar adegannya.
3. Tulis prompt per ayat pakai struktur di atas, generate satu per satu.
4. Cek tiap gambar: sesuai arti ayat, tanpa teks terbaca, gaya konsisten,
   parallax-ready, ukuran 1152x2048 WebP.
5. Simpan dengan nama yang sama di `assets/images/` (`bismillah.webp`, `ayat1.webp`,
   dst), sesuaikan jumlah file dengan jumlah ayat.
6. Perbarui teks, timing, dan data karaoke dari audio murrotal surah baru.
7. Verifikasi md5 dan ukuran tiap file dari disk sebelum diserahkan.

Panduan lengkap: `PANDUAN-GENERATE-GAMBAR.md`.
```

---

## LAMPIRAN: FILE REFERENSI

Folder: `~/workspace/murrotal-quraish-v2-motlab/assets/`

| File | Ukuran | md5 | Dimensi |
|---|---|---|---|
| `bismillah.webp` | 424.386 byte | f54b6aba | 1152x2048 |
| `ayat1.webp` | 446.806 byte | 49ec0208 | 1152x2048 |
| `ayat2.webp` | 500.576 byte | 714c5893 | 1152x2048 |
| `ayat3.webp` | 333.516 byte | c0942475 | 1152x2048 |
| `ayat4.webp` | 874.814 byte | 647362a6 | 1152x2048 |

md5 di atas dihitung dari disk saat panduan ini ditulis. Kalau file referensi diganti, hitung ulang md5-nya, jangan kutip angka lama.

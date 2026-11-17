# Audio: ISI SENDIRI, TIDAK ADA DI REPO

Folder ini SENGAJA KOSONG di repo. File audio murrotal (recitation) TIDAK ikut
masuk repo karena hak cipta qari. `project.json` mengharapkan satu file di sini:

```
audio/audio.wav
```

## Cara isi audio sendiri

1. Cari rekaman murrotal surah yang kamu mau (misal dari YouTube).
2. Unduh audionya saja:

```
yt-dlp -x --audio-format wav -o audio/audio.wav "<URL video>"
```

3. Kalau rekaman masih ada intro/outro atau noise di ujung, potong dengan ffmpeg.
   Ukur dulu durasi dan cari batas bacaan (misal dengan `ffprobe` + dengarkan):

```
ffmpeg -i audio/audio.wav -ss 0 -to 47.717 -c copy audio/audio-trim.wav
mv audio/audio-trim.wav audio/audio.wav
```

   Ganti `47.717` dengan detik akhir bacaan yang sebenarnya. Jangan potong di
   tengah kata. Jangan percepat, jangan tambah BGM.

4. Cek hasil: `ffprobe audio/audio.wav` (durasi + sample rate), lalu dengarkan
   5 detik awal dan 5 detik akhir.

## Aturan

- Audio dipakai UTUH di video, tanpa potong di tengah, tanpa dipercepat,
  tanpa BGM/musik/SFX.
- Durasi audio = durasi video. Semua waktu di `timing-ayat.md` dan
  `karaoke-table.md` diukur dari audio ini; kalau kamu ganti audio dengan
  qari lain, UKUR ULANG semua batas ayat dan kata (lihat
  `templates/SUTRADARA-TEMPLATE.md` §5).
- Jangan commit audio ke repo ini (sudah di `.gitignore`). Jangan
  redistribusikan rekaman qari tanpa izin pemegang haknya.

## Contoh yang dipakai template ini

QS. Quraish (106), Ridjaal Ahmed, 47,717 detik, 48 kHz stereo, md5
`7efb314b917618acc3103bf5eba56797` (file asli TIDAK disertakan, cuma angka
acuan buat verifikasi kalau kamu pakai rekaman yang sama).

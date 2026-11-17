# Timing Ayat — Murrotal QS. Quraish (106)

- Sumber: `audio.wav` (9.161.746 byte, md5 `7efb314b917618acc3103bf5eba56797`, 47,717 dtk, 48 kHz stereo, PCM s16le)
- Qari: Ridjaal Ahmed
- File dipakai utuh, tanpa diubah.
- Metode: faster-whisper small, bahasa `ar`, word timestamps. Batas tiap segmen = timestamp kata pertama dan terakhir, dicek silang dengan silencedetect + volumedetect per jendela 0,2 dtk.
- Koreksi dari timestamp mentah Whisper: start Basmalah 0,00 -> 0,31 (0-0,31 dtk hening, mean -69,9 dB); end Ayat 4 44,30 -> 45,19 (suara masih jalan sampai 45,19, hening mulai 45,19, mean -68,1 dB sesudahnya).

| Segmen | Arab | Start (dtk) | End (dtk) | Durasi (dtk) |
|---|---|---|---|---|
| Basmalah | بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ | 0,31 | 6,16 | 5,85 |
| Ayat 1 | لِإِيلَافِ قُرَيْشٍ | 7,56 | 11,58 | 4,02 |
| Ayat 2 | إِيلَافِهِمْ رِحْلَةَ الشِّتَاءِ وَالصَّيْفِ | 12,20 | 21,46 | 9,26 |
| Ayat 3 | فَلْيَعْبُدُوا رَبَّ هَٰذَا الْبَيْتِ | 22,00 | 28,44 | 6,44 |
| Ayat 4 | الَّذِي أَطْعَمَهُم مِّن جُوعٍ وَآمَنَهُم مِّنْ خَوْفٍ | 29,44 | 45,19 | 15,75 |

## Catatan

- Transkrip lengkap Whisper (kata per kata + timestamp): `transcript.json`. Skrip transkrip: `transcribe.py`.
- Jeda antar ayat (hening): Basmalah-Ayat 1: 6,16-7,56 (1,40 dtk); Ayat 1-Ayat 2: 11,58-12,20 (0,62 dtk); Ayat 2-Ayat 3: 21,46-22,00 (0,54 dtk); Ayat 3-Ayat 4: 28,44-29,44 (1,00 dtk).
- Ayat 4 punya jeda napas di tengah (38,48-40,36, 1,88 dtk) antara "مِّن جُوعٍ" dan "وَآمَنَهُم مِّنْ خَوْفٍ". Itu satu ayat, jadi jeda ini tetap di dalam rentang Ayat 4, bukan batas segmen.
- Ekor file 45,19-47,717 hening (2,53 dtk). Awal file 0-0,31 hening.
- Whisper menulis beberapa kata dengan ejaan berbeda tapi bunyi sama (mis. "قرش" untuk قُرَيْشٍ, "جور" untuk جُوعٍ, "خور" untuk خَوْفٍ); pemetaan ke ayat tetap jelas dari urutan dan konteks.

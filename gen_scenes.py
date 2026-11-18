#!/usr/bin/env python3
# Generator adegan murrotal Quraish v2 (motlab + motion-cut).
# Baca karaoke-data.json (dari build.py), tulis scenes/*.html + project.json.
# Teks Arab + transliterasi + terjemahan dari teks-quraish.md (programmatic, bukan retype).
# Peta karaoke 21 kata dari tabel §5 SUTRADARA (programmatic, bukan retype).
# MERGE TEMPLATE (Bos 2026-11-18 ~00:48-00:55 WIB, spec VideoStory TEKNIK-DOT-PARALLAX.md):
# DOT (§1: titik putih 3 px, jarak 24 px, stagger 12 px, opacity 0.06, ikut gambar),
# PARALLAX (§2: gambar zoom 1.3 + pan 20 px, partikel drift 30 px berlawanan,
# teks drift sinusoidal +-15 px berlawanan).
# NO-KABUR (perintah Bos 2026-11-18, Dewa): efek kabur latar DIHAPUS total,
# background tajam; transisi D1 + D4 yang dulu pakai efek kabur jadi
# cross-dissolve biasa (fade).
# Zoom 1.3 SEMUA adegan (perintah Bos 00:55, dulu 1.03-1.05). Di zoom maks, area
# kelihatan 831x1477 px (~11,5% per sisi terpotong); cek framing di preview.
# Koreksi CEO (pakai yang benar ini, bukan catatan §11 yang salah):
#   - Stills Basmalah 2,63: kata aktif kata 3 الرَّحْمَٰنِ (bukan kata 2).
#   - Stills Ayat 2 17,00: kata aktif kata 9 الشِّتَاۤءِ (bukan kata 10).
#   - Batas Ayat 3 رَبَّ/هٰذَا 25.12 (f 602): verifikasi telinga di preview.
# 0 em dash di file ini dan di file hasil.
#
# PELAJARAN WAJIB (template jadi-reciter, baca sebelum ubah file ini):
#
# 1. FRAME-SNAP karaoke, mekanisme yang BENAR-BENAR ada di kode ini:
#    - Kata aktif diputuskan di drawTextBlock: videoFrame = Math.floor(videoTime * 24),
#      videoTime = SCENE_START + t, kata aktif kalau f_start <= videoFrame < f_end.
#    - f_start = floor(start kata x 24), f_end = floor(end kata SENDIRI x 24)
#      (bukan f_start kata berikut, lihat BUG 3 di build.py: jeda napas Ayat 4
#      38.48-40.36 harus kosong, kata 18 f_end 923 bukan 968).
#    - grep VT_OFFSET di file sumber ASLI hasilnya KOSONG (0): nama VT_OFFSET TIDAK ADA
#      di generator ini. Jangan klaim sebaliknya.
#
# 2. VT_OFFSET (pelajaran dari varian motlab + herwanto, TERBUKTI di sana):
#    - Motlab render memanggil renderAt(t) dengan t terkuantisasi dari scene start
#      yang sudah snap ke grid frame (ceil(SCENE_START*24)/24). Akibatnya videoTime
#      mentah (SCENE_START + t) bisa ketinggalan sampai 1 frame (41,67 ms) dari waktu
#      frame global yang benar.
#    - Koreksinya: VT_OFFSET = ceil(SCENE_START*24)/24 - SCENE_START (0 sampai 0,0417 dtk),
#      ditambahkan ke videoTime SEBELUM frame-snap dan SEBELUM pembacaan waktu apa pun.
#    - Di varian herwanto, VT_OFFSET dipakai buat timestamp + progress bar (pembacaan
#      waktu); karaoke di sana tetap pakai floor snap polos dan switch-nya terverifikasi
#      tepat di frame (contoh f592). Di generator motion-cut ini TIDAK ADA timestamp
#      atau progress bar, jadi VT_OFFSET tidak dipakai di jalur mana pun.
#    - Kalau kamu TAMBAH timestamp / progress bar ke template ini, pakai VT_OFFSET di
#      sana, atau pembacaan waktunya ketinggalan sampai 1 frame (di detik bulat bisa
#      terbaca 1 detik lebih rendah). Karaoke di file ini biarkan seperti aslinya.
#
# 3. ARAB_LINES Ayat 4 WAJIB [[0, 1, 2, 3, 4], [5, 6, 7, 8]] (9 run, lihat bawah):
#    - Split LAMA yang SALAH: [[0,1,2,3],[4,5,6]] (cuma 7 run). Akibatnya kata 21
#      خَوْفٍ + tanda ࣖ TIDAK PERNAH tampil, dan ەۙ salah posisi di awal baris 2.
#      Bug ini lolos build pertama dan baru ketahuan dari cek frame jendela kata
#      terakhir (f1035-1084). Perbaikan (RENDER-FIX.md): re-render 4 versi motlab.
#    - Aturan: SETIAP kali generate ulang, grep خَوْفٍ di scenes/05-ayat4.html HARUS = 1.
#      Kalau 0, JANGAN render. Generator ini assert jumlah run terpakai = jumlah run
#      di karaoke-data.json, tapi grep kata terakhir tetap jadi gerbang terakhir.
#    - Ayat lain 1 baris semua; Ayat 4 2 baris: baris 1 = kata 15,16,17,18 + ەۙ di
#      AKHIR, baris 2 = kata 19,20,21 + ࣖ di AKHIR. Tanda akhir ayat selalu emas.
import json
from pathlib import Path

PROJ = Path(__file__).parent
DATA = json.loads((PROJ / "karaoke-data.json").read_text(encoding="utf-8"))

# Konfigurasi adegan (SUTRADARA §7). sceneStart = awal adegan di waktu video.
# textStart/textEnd = rentang teks di waktu video. Lokal = video - sceneStart.
# MERGE TEMPLATE (Bos 2026-11-18 ~00:55 WIB): kb_end SEMUA 1.3 (dulu 1.04/1.04/1.03/1.04/1.05
# di spec VideoStory). Pan per adegan ikut spec §2.3 (arah cahaya / arah gerak subjek).
SCENES = [
    {"file": "01-basmalah.html", "verse": "Basmalah", "pill": "QS. Quraish (106) - Basmalah",
     "img": "bismillah.webp", "total": 7.11, "start": 0.0,
     "text_start": 0.31, "text_end": 6.16, "kb_end": 1.3, "kind": "rays", "pan": [0, -1]},
    {"file": "02-ayat1.html", "verse": "Ayat 1", "pill": "QS. Quraish (106) - Ayat 1 / 4",
     "img": "ayat1.webp", "total": 5.53, "start": 6.61,
     "text_start": 7.56, "text_end": 11.58, "kb_end": 1.3, "kind": "dusk", "pan": [1, 0]},
    {"file": "03-ayat2.html", "verse": "Ayat 2", "pill": "QS. Quraish (106) - Ayat 2 / 4",
     "img": "ayat2.webp", "total": 10.34, "start": 11.64,
     "text_start": 12.20, "text_end": 21.46, "kb_end": 1.3, "kind": "snow", "pan": [-1, 0]},
    {"file": "04-ayat3.html", "verse": "Ayat 3", "pill": "QS. Quraish (106) - Ayat 3 / 4",
     "img": "ayat3.webp", "total": 7.71, "start": 21.48,
     "text_start": 22.00, "text_end": 28.44, "kb_end": 1.3, "kind": "night", "pan": [1, 0]},
    {"file": "05-ayat4.html", "verse": "Ayat 4", "pill": "QS. Quraish (106) - Ayat 4 / 4",
     "img": "ayat4.webp", "total": 19.03, "start": 28.69,
     "text_start": 29.44, "text_end": 45.19, "kb_end": 1.3, "kind": "oasis", "pan": [0, -1]},
]
# Gambar default (Bos 2026-11-18 ~00:52 WIB): kalau gambar satu ayat belum ada di assets/images/,
# adegan itu pakai gambar ini (Ka'bah, generik) + peringatan jelas di log. Build TETAP JALAN,
# video tidak kosong. Ini MENGGANTIKAN aturan berhenti keras sebelumnya.
DEFAULT_IMG = "default.webp"

# Baris Arab per ayat (SUTRADARA §5: Ayat 4 2 baris, sisanya 1 baris).
# Diisi dari runs (kata + tanda) karaoke-data.json, dipotong per baris.
ARAB_LINES = {
    "Basmalah": [[0, 1, 2, 3]],
    "Ayat 1": [[0, 1]],
    "Ayat 2": [[0, 1, 2, 3]],
    "Ayat 3": [[0, 1, 2, 3]],
    "Ayat 4": [[0, 1, 2, 3, 4], [5, 6, 7, 8]],
}

def verse_runs(verse):
    """Susun runs per baris Arab: tiap run {text, mark, word} (word = nomor kata global 1-21, -1 = tanda saja)."""
    words = [w for w in DATA["words"] if w["verse"] == verse]
    raw = DATA["verses"][verse]["runs"]  # list [kata, tanda] per token
    # Petakan token ke nomor kata: token yang punya kata = kata tampil berurutan.
    runs = []
    wi = 0
    for kata, tanda in raw:
        if kata:
            runs.append({"text": kata, "mark": tanda, "word": words[wi]["no"]})
            wi += 1
        else:
            runs.append({"text": tanda, "mark": "", "word": -1})
    assert wi == len(words), f"{verse}: {wi} kata, tabel {len(words)}"
    lines = []
    for line_idx in ARAB_LINES[verse]:
        line = []
        for k in line_idx:
            line.append(runs[k])
        lines.append(line)
    return lines

JS_TEMPLATE = r"""<!doctype html><html><head><meta charset="utf-8"><title>__TITLE__</title>
<style>
  @font-face { font-family: 'Noto Naskh Arabic'; src: url("../assets/fonts/NotoNaskhArabic-SemiBold.ttf") format("truetype"); font-weight: 600; }
  @font-face { font-family: 'Noto Sans'; src: url("../assets/fonts/NotoSans-Regular.ttf") format("truetype"); font-weight: 400; }
  @font-face { font-family: 'Noto Sans'; src: url("../assets/fonts/NotoSans-SemiBold.ttf") format("truetype"); font-weight: 600; }
  html, body { margin: 0; background: #000; }
  canvas { display: block; }
</style></head><body><canvas id="c"></canvas>
<script>
// Murrotal QS. Quraish v2, adegan __VERSE__ (motlab + motion-cut).
// Teks dari teks-quraish.md, peta karaoke dari tabel §5 SUTRADARA. Tanpa footer.
const W = 1080, H = 1920, TOTAL = __TOTAL__, SCENE_START = __START__;
const GOLD = '#E8C766', WHITE = '#FFFFFF';
const PILL = __PILL__;
const IMG_SRC = '../assets/images/__IMG__';
const KIND = '__KIND__';
const PAN = __PAN__;  // arah pan gambar [x, y], ikut spec §2.3 (cahaya / arah gerak subjek)
const TEXT_START = __TEXT_START__, TEXT_END = __TEXT_END__;   // waktu video
const KB_END = __KB_END__;
const FADE_BLACK = __FADE_BLACK__;  // [lokal mulai, lokal selesai] atau null
const WORDS = __WORDS__;            // [{no, f_start, f_end}] waktu video (frame 24fps)
const ARAB_LINES = __ARAB_LINES__;  // per baris: [{text, mark, word}] word = nomor kata, -1 = tanda saja
const TRANSLIT = __TRANSLIT__;
const TRANSL = __TRANSL__;
const TL_LINES = __TL_LINES__;  // target baris terjemahan (SUTRADARA §6)

const params = new URLSearchParams(location.search), SCALE = parseFloat(params.get('scale') || '1');
const cv = document.getElementById('c'), ctx = cv.getContext('2d');
cv.width = Math.round(W * SCALE); cv.height = Math.round(H * SCALE);
const TAU = Math.PI * 2;
const clamp = (v, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, v));
const hash = n => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };

const img = new Image();
let LAYOUT = null;

async function loadAssets() {
  await Promise.all([
    document.fonts.load('600 72px "Noto Naskh Arabic"', 'ب'),
    document.fonts.load('400 36px "Noto Sans"', 'B'),
    document.fonts.load('600 28px "Noto Sans"', 'Q'),
    new Promise((res, rej) => { img.onload = res; img.onerror = rej; img.src = IMG_SRC; }),
  ]);
  await img.decode();
}

function wrapText(text, size, maxW, maxLines) {
  // Bungkus teks Latin jadi maks maxLines baris dalam maxW. Kembalikan {lines, size}.
  // Target baris per ayat (SUTRADARA §6): Basmalah 1, Ayat 1 1, Ayat 2-4 2.
  let s = size;
  while (s > 28) {
    ctx.font = `400 ${s}px "Noto Sans"`;
    const words = text.split(' ');
    const lines = [''];
    for (const w of words) {
      const trial = lines[lines.length - 1] ? lines[lines.length - 1] + ' ' + w : w;
      if (ctx.measureText(trial).width <= maxW) lines[lines.length - 1] = trial;
      else lines.push(w);
    }
    if (lines.length <= maxLines) return { lines, size: s };
    s -= 2;
  }
  ctx.font = `400 ${s}px "Noto Sans"`;
  const words = text.split(' ');
  const lines = [''];
  for (const w of words) {
    const trial = lines[lines.length - 1] ? lines[lines.length - 1] + ' ' + w : w;
    if (ctx.measureText(trial).width <= maxW) lines[lines.length - 1] = trial;
    else lines.push(w);
  }
  return { lines, size: s };
}

function layoutText() {
  // Hitung ukuran font + tinggi kotak dari metrik font aktual. Lebar dalam kotak 880 px.
  const INNER = 880;
  // Arab: mulai 72 px, kecilkan sampai baris terpanjang muat.
  let arabSize = 72;
  const spaceW = () => ctx.measureText(' ').width;
  function lineW(runs, size) {
    ctx.font = `600 ${size}px "Noto Naskh Arabic"`;
    let w = 0;
    runs.forEach((r, i) => { w += ctx.measureText(r.text + (r.mark || '')).width; if (i) w += spaceW(); });
    return w;
  }
  while (arabSize > 40 && Math.max(...ARAB_LINES.map(l => lineW(l, arabSize))) > INNER) arabSize -= 2;
  // Transliterasi: 1 baris, mulai 36 px.
  let trSize = 36;
  ctx.font = `400 ${trSize}px "Noto Sans"`;
  while (trSize > 24 && ctx.measureText(TRANSLIT).width > INNER) { trSize -= 1; ctx.font = `400 ${trSize}px "Noto Sans"`; }
  // Terjemahan: target baris per ayat (SUTRADARA §6), mulai 40 px.
  const tr = wrapText(TRANSL, 40, INNER, TL_LINES);
  const arabLH = 1.3 * arabSize, trLH = 1.2 * trSize, tlLH = 1.35 * tr.size;
  const textH = ARAB_LINES.length * arabLH + 24 + trLH + 24 + tr.lines.length * tlLH;
  const boxH = textH + 72, boxTop = 1731 - boxH;
  LAYOUT = { arabSize, trSize, tlSize: tr.size, tlLines: tr.lines,
    arabLH, trLH, tlLH, textH, boxH, boxTop, innerTop: boxTop + 36 };
}

function activeWord(videoFrame) {
  for (const w of WORDS) if (videoFrame >= w.f_start && videoFrame < w.f_end) return w.no;
  return -1;
}

function drawArabicLine(runs, centerX, centerY, videoFrame) {
  // Susun RTL: kata 1 paling kanan. Tanda akhir ayat selalu emas.
  const size = LAYOUT.arabSize;
  ctx.font = `600 ${size}px "Noto Naskh Arabic"`;
  ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
  const spaceW = ctx.measureText(' ').width;
  let total = 0;
  runs.forEach((r, i) => { total += ctx.measureText(r.text + (r.mark || '')).width; if (i) total += spaceW; });
  let xRight = centerX + total / 2;
  const active = activeWord(videoFrame);
  for (const r of runs) {
    const full = r.text + (r.mark || '');
    const w = ctx.measureText(full).width;
    if (r.word > 0) {
      ctx.fillStyle = GOLD;
      ctx.fillText(full, xRight, centerY);
      if (r.word === active) { ctx.fillStyle = WHITE; ctx.fillText(r.text, xRight, centerY); }
    } else {
      ctx.fillStyle = GOLD;
      ctx.fillText(full, xRight, centerY);
    }
    xRight -= w + spaceW;
  }
  ctx.textAlign = 'left';
}

function textOp(t) {
  // Opacity teks (pill + blok teks): fade 0,2 dtk di awal + akhir rentang teks.
  // Pill ikut blok teks (ikut v1: pill hilang bersama teks ayat di ekor + jeda antar ayat).
  const lt0 = TEXT_START - SCENE_START, lt1 = TEXT_END - SCENE_START;
  if (t < lt0 || t > lt1) return 0;
  return Math.min(clamp((t - lt0) / 0.2), clamp((lt1 - t) / 0.2));
}

function drawPill(op) {
  if (op <= 0) return;
  ctx.save(); ctx.globalAlpha = op;
  ctx.font = '600 28px "Noto Sans"';
  const tw = ctx.measureText(PILL).width, pw = tw + 72, px = (W - pw) / 2;
  ctx.beginPath(); ctx.roundRect(px, 60, pw, 52, 26);
  ctx.fillStyle = 'rgba(0,0,0,0.55)'; ctx.fill();
  ctx.lineWidth = 1.5; ctx.strokeStyle = GOLD; ctx.stroke();
  ctx.fillStyle = GOLD; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText(PILL, W / 2, 86);
  ctx.textAlign = 'left';
  ctx.restore();
}

function drawTextBlock(t, videoTime, op) {
  if (op <= 0) return;
  const L = LAYOUT, videoFrame = Math.floor(videoTime * 24);
  ctx.save(); ctx.globalAlpha = op;
  // Shadow box.
  ctx.beginPath(); ctx.roundRect(60, L.boxTop, 960, L.boxH, 24);
  ctx.fillStyle = 'rgba(0,0,0,0.55)'; ctx.fill();
  ctx.lineWidth = 2; ctx.strokeStyle = 'rgba(255,255,255,0.35)'; ctx.stroke();
  // Arab.
  let y = L.innerTop;
  ARAB_LINES.forEach((runs, i) => {
    drawArabicLine(runs, W / 2, y + (i + 0.5) * L.arabLH, videoFrame);
  });
  y += ARAB_LINES.length * L.arabLH + 24;
  // Transliterasi.
  ctx.font = `400 ${L.trSize}px "Noto Sans"`;
  ctx.fillStyle = 'rgba(255,255,255,0.85)'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText(TRANSLIT, W / 2, y + L.trLH / 2);
  y += L.trLH + 24;
  // Terjemahan.
  ctx.font = `400 ${L.tlSize}px "Noto Sans"`;
  ctx.fillStyle = WHITE;
  L.tlLines.forEach((ln, i) => ctx.fillText(ln, W / 2, y + (i + 0.5) * L.tlLH));
  ctx.textAlign = 'left';
  ctx.restore();
}

function drawLight(t, dX, dY) {
  // Cahaya + partikel per adegan, deterministik (hanya t + hash, tanpa Math.random).
  // dX/dY = drift parallax lapis 2 (spec §2.2): -1,5 x pan gambar, berlawanan arah.
  if (KIND === 'rays') {
    let g = ctx.createRadialGradient(W * 0.5, 120, 0, W * 0.5, 120, 700);
    g.addColorStop(0, 'rgba(255,214,130,0.30)'); g.addColorStop(1, 'rgba(255,214,130,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    g = ctx.createRadialGradient(W * 0.5, 1150, 0, W * 0.5, 1150, 500);
    g.addColorStop(0, 'rgba(255,200,110,0.20)'); g.addColorStop(1, 'rgba(255,200,110,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    motes(t, 40, 0.35, -1, dX, dY);
  } else if (KIND === 'dusk') {
    let g = ctx.createRadialGradient(W * 0.5, 900, 0, W * 0.5, 900, 650);
    g.addColorStop(0, 'rgba(255,170,80,0.28)'); g.addColorStop(1, 'rgba(255,170,80,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    motes(t, 40, 0.3, 0, dX, dY);
  } else if (KIND === 'snow') {
    let g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, 'rgba(210,225,245,0.14)'); g.addColorStop(1, 'rgba(210,225,245,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    snow(t, 60, dX, dY);
  } else if (KIND === 'night') {
    let g = ctx.createRadialGradient(W * 0.78, 260, 0, W * 0.78, 260, 420);
    g.addColorStop(0, 'rgba(220,230,255,0.22)'); g.addColorStop(1, 'rgba(220,230,255,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    g = ctx.createRadialGradient(W * 0.5, 1250, 0, W * 0.5, 1250, 450);
    g.addColorStop(0, 'rgba(255,205,120,0.20)'); g.addColorStop(1, 'rgba(255,205,120,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    sparkles(t, 50, dX, dY);
  } else if (KIND === 'oasis') {
    let g = ctx.createRadialGradient(W * 0.72, 300, 0, W * 0.72, 300, 600);
    g.addColorStop(0, 'rgba(255,200,110,0.26)'); g.addColorStop(1, 'rgba(255,200,110,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    g = ctx.createRadialGradient(W * 0.5, 1350, 0, W * 0.5, 1350, 500);
    g.addColorStop(0, 'rgba(255,215,140,0.18)'); g.addColorStop(1, 'rgba(255,215,140,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    motes(t, 40, 0.3, -1, dX, dY);
    shimmer(t, dX, dY);
  }
}

function motes(t, n, baseA, dir, dX, dY) {
  // Debu cahaya / serbuk sari melayang. dir -1 = naik, 0 = horizontal.
  for (let i = 0; i < n; i++) {
    const x0 = hash(i) * W, y0 = hash(i + 100) * H, r = 2 + hash(i + 200) * 3.5;
    const ph = hash(i + 400) * TAU, sp = 8 + hash(i + 300) * 22;
    let x, y;
    if (dir < 0) { x = x0 + Math.sin(t * 0.3 + ph) * 24 + dX; y = ((y0 - t * sp) % H + H) % H + dY; }
    else { x = ((x0 + t * sp) % W + W) % W + dX; y = y0 + Math.sin(t * 0.4 + ph) * 16 + dY; }
    const a = baseA * (0.6 + 0.4 * Math.sin(t * 0.8 + ph));
    ctx.globalAlpha = Math.max(0, a);
    ctx.fillStyle = '#FFE9B0';
    ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
  }
  ctx.globalAlpha = 1;
}

function snow(t, n, dX, dY) {
  for (let i = 0; i < n; i++) {
    const x0 = hash(i) * W, sp = 30 + hash(i + 300) * 45, ph = hash(i + 400) * TAU;
    const y = ((hash(i + 100) * H + t * sp) % H + H) % H + dY;
    const x = x0 + Math.sin(t * 0.5 + ph) * 12 + dX;
    ctx.globalAlpha = 0.35 + 0.45 * hash(i + 200);
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath(); ctx.arc(x, y, 2 + hash(i + 200) * 3, 0, TAU); ctx.fill();
  }
  ctx.globalAlpha = 1;
}

function sparkles(t, n, dX, dY) {
  for (let i = 0; i < n; i++) {
    const x = hash(i) * W + dX, y = hash(i + 100) * H * 0.55 + dY, ph = hash(i + 400) * TAU;
    const a = 0.25 + 0.65 * Math.abs(Math.sin(t * 1.4 + ph));
    ctx.globalAlpha = a;
    ctx.fillStyle = i % 3 ? '#FFFFFF' : '#FFE9B0';
    const r = 1.5 + hash(i + 200) * 2.5;
    ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
  }
  ctx.globalAlpha = 1;
}

function shimmer(t, dX, dY) {
  // Kilau air: garis tipis horizontal di area sungai, berkedip pelan.
  for (let i = 0; i < 12; i++) {
    const y = 1150 + hash(i) * 450 + dY, x = 200 + hash(i + 50) * 680 + dX, len = 30 + hash(i + 100) * 90;
    const a = 0.10 + 0.14 * Math.abs(Math.sin(t * 1.1 + hash(i + 400) * TAU));
    ctx.globalAlpha = a; ctx.fillStyle = '#FFE9B0';
    ctx.fillRect(x, y, len, 2);
  }
  ctx.globalAlpha = 1;
}

function drawDots() {
  // DOT (spec §1): grid titik putih 3 px, jarak 24 px, baris ganjil geser 12 px,
  // opacity 0.06. ~3.600 titik (45 kolom x 80 baris). Digambar DI DALAM transform
  // Ken Burns gambar (ikut zoom + pan, lapis 1), sesudah gambar, sebelum partikel.
  // Titik tidak pernah menyentuh teks: shadow box + pill menutupinya di area teks.
  ctx.save();
  ctx.fillStyle = 'rgba(255,255,255,0.06)';
  for (let gy = 0; gy < 80; gy++) {
    const y = gy * 24 + 12;
    const off = (gy % 2) ? 12 : 0;
    for (let gx = 0; gx < 45; gx++) {
      const x = gx * 24 + 12 + off;
      ctx.beginPath(); ctx.arc(x, y, 1.5, 0, TAU); ctx.fill();
    }
  }
  ctx.restore();
}

function render(t) {
  ctx.setTransform(SCALE, 0, 0, SCALE, 0, 0);
  ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, H);
  // Parallax lapis 1 (spec §2): Ken Burns zoom-in + pan linear 20 px sepanjang adegan.
  const k = clamp(t / TOTAL);
  const z = 1 + (KB_END - 1) * k;
  const panX = PAN[0] * 20 * k, panY = PAN[1] * 20 * k;
  // Lapis 2 drift (spec §2.2): partikel -1,5 x pan, berlawanan arah gambar.
  const dX = -1.5 * panX, dY = -1.5 * panY;
  // Lapis 3 drift (spec §2.2): teks sinusoidal +-15 px, berlawanan arah gambar,
  // satu siklus penuh per adegan (0 di awal + akhir, puncak di tengah).
  // Drift teks TIDAK pakai VT_OFFSET (gerak visual, bukan penanda waktu).
  const s = Math.sin(TAU * k);
  const tdx = -15 * s * PAN[0], tdy = -15 * s * PAN[1];
  // (1) Gambar tajam + Ken Burns + pan.
  ctx.save();
  ctx.translate(W / 2 + panX, H / 2 + panY); ctx.scale(z, z); ctx.translate(-W / 2, -H / 2);
  ctx.drawImage(img, 0, 0, W, H);
  ctx.restore();
  // (2) DOT, ikut transform gambar (spec §1.3).
  ctx.save();
  ctx.translate(W / 2 + panX, H / 2 + panY); ctx.scale(z, z); ctx.translate(-W / 2, -H / 2);
  drawDots();
  ctx.restore();
  // (3) Partikel + cahaya (drift lapis 2).
  drawLight(t, dX, dY);
  // (4) Pill + blok teks, drift sinusoidal sebagai SATU lapis (spec §2.2).
  const op = textOp(t);
  ctx.save();
  ctx.translate(tdx, tdy);
  drawPill(op);
  drawTextBlock(t, SCENE_START + t, op);
  ctx.restore();
  if (FADE_BLACK) {
    const fk = clamp((t - FADE_BLACK[0]) / (FADE_BLACK[1] - FADE_BLACK[0]));
    if (fk > 0) { ctx.fillStyle = `rgba(0,0,0,${fk})`; ctx.fillRect(0, 0, W, H); }
  }
}

window.TOTAL = TOTAL;
window.renderAt = render;
window.ready = (async () => {
  await loadAssets();
  layoutText();
  render(parseFloat(params.get('t') || '0'));
})();
</script></body></html>
"""

def scene_words(verse):
    ws = [w for w in DATA["words"] if w["verse"] == verse]
    return [{"no": w["no"], "f_start": w["f_start"], "f_end": w["f_end"]} for w in ws]

def main():
    out_scenes = PROJ / "scenes"
    for sc in SCENES:
        verse = sc["verse"]
        v = DATA["verses"][verse]
        lines = verse_runs(verse)
        # Gambar default (Bos 2026-11-18 ~00:52 WIB): kalau gambar ayat ini belum ada
        # di assets/images/, adegan pakai default.webp + peringatan jelas di log. Build
        # TETAP JALAN, video tidak kosong. Jangan render video tanpa gambar.
        img = sc["img"]
        if not (PROJ / "assets" / "images" / img).exists():
            print(f"PERINGATAN: gambar {verse} tidak ada (assets/images/{img}), pakai gambar default {DEFAULT_IMG}")
            img = DEFAULT_IMG
        fade = None
        if verse == "Ayat 4":
            # Fade hitam video 47.217-47.717, lokal = video - 28.69 = 18.527-19.027
            fade = [47.217 - 28.69, 47.717 - 28.69]
        html = (JS_TEMPLATE
            .replace("__TITLE__", sc["file"].replace(".html", ""))
            .replace("__VERSE__", verse)
            .replace("__TOTAL__", repr(sc["total"]))
            .replace("__START__", repr(sc["start"]))
            .replace("__PILL__", json.dumps(sc["pill"], ensure_ascii=False))
            .replace("__IMG__", img)
            .replace("__PAN__", json.dumps(sc["pan"]))
            .replace("__KIND__", sc["kind"])
            .replace("__TEXT_START__", repr(sc["text_start"]))
            .replace("__TEXT_END__", repr(sc["text_end"]))
            .replace("__KB_END__", repr(sc["kb_end"]))
            .replace("__FADE_BLACK__", json.dumps(fade))
            .replace("__WORDS__", json.dumps(scene_words(verse), ensure_ascii=False))
            .replace("__ARAB_LINES__", json.dumps(lines, ensure_ascii=False))
            .replace("__TRANSLIT__", json.dumps(v["translit"], ensure_ascii=False))
            .replace("__TRANSL__", json.dumps(v["transl"], ensure_ascii=False))
            .replace("__TL_LINES__", "1" if verse in ("Basmalah", "Ayat 1") else "2"))
        assert "—" not in html, f"em dash di {sc['file']}"
        (out_scenes / sc["file"]).write_text(html, encoding="utf-8")
        print(f"OK {sc['file']}: TOTAL {sc['total']} dtk, {len(lines)} baris Arab, {len(scene_words(verse))} kata")
    # project.json persis §10 SUTRADARA
    pj = {
        "fps": 24,
        "scenes": [
            "scenes/01-basmalah.html",
            {"file": "scenes/02-ayat1.html", "transition": {"type": "fade", "duration": 0.5, "ease": "inOutCubic"}},
            {"file": "scenes/03-ayat2.html", "transition": {"type": "directionalwarp", "duration": 0.5, "ease": "inOutCubic", "params": {"direction": [-1, 1]}}},
            {"file": "scenes/04-ayat3.html", "transition": {"type": "fadecolor", "duration": 0.5, "ease": "inOutCubic", "params": {"color": [0, 0, 0], "colorPhase": 0.4}}},
            {"file": "scenes/05-ayat4.html", "transition": {"type": "fade", "duration": 0.5, "ease": "inOutCubic"}},
        ],
        "audio": [{"file": "audio/audio.wav", "start": 0, "volume": 1.0}],
    }
    (PROJ / "project.json").write_text(json.dumps(pj, indent=2), encoding="utf-8")
    print("OK project.json ditulis")

if __name__ == "__main__":
    main()

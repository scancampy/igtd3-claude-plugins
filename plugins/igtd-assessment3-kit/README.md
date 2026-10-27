# IGTD Assessment 3 Kit

Plugin pendamping mahasiswa untuk **Assessment 3: Build an Intelligent Game Feature** pada mata kuliah Intelligent Game Technology & Design (Magister Informatika).

## Apa yang dilakukan plugin ini

Plugin ini membuat Claude berperan sebagai **pembimbing (coach)**, bukan pengerja tugas. Claude akan bertanya, menawarkan opsi dan trade-off, lalu meminta mahasiswa memutuskan sendiri. Hal ini sejalan dengan norma pemanfaatan AI pada mata kuliah (level SAMR: Modification) yang menilai proses berpikir, bukan sekadar produk yang dihasilkan AI.

## Isi

| Komponen | Fungsi |
|---|---|
| `pilih-fitur` | Memilih dan mempersempit fitur (Opsi A-E) agar realistis untuk 3 minggu |
| `baseline-first` | Membangun baseline non-AI (opsional; menentukan batas nilai 100% vs 75%) sebelum solusi berbasis AI |
| `eval-baseline-vs-ai` | Merancang metrik dan tabel komparasi baseline vs AI |
| `etika-bias-check` | Daftar periksa bias, keamanan konten, privasi, halusinasi |
| `laporan-teknis` | Menyusun laporan singkat dan checklist video demonstrasi |
| `self-check-rubrik` | Umpan balik formatif terhadap enam indikator penilaian |
| `/ai-log` | Mencatat satu entri log interaksi AI dengan format baku |

## Cara pakai

Pasang plugin, lalu ceritakan proyek Anda secara biasa, misalnya "Kelompok kami ingin membuat NPC pedagang yang bisa mengobrol". Skill yang sesuai akan aktif otomatis. Ketik atau minta `/ai-log` setiap selesai memakai AI untuk hal yang penting.

## Data

Plugin ini hanya berisi instruksi (Markdown) dan satu skrip Python kecil yang berjalan lokal untuk merangkum file CSV hasil uji. Plugin tidak menyimpan data dan tidak mengirim data ke layanan lain. Isi percakapan diproses sesuai kebijakan aplikasi Claude yang Anda gunakan.

## Catatan

Plugin ini alat bantu belajar. Keputusan desain, verifikasi sumber, dan penilaian tetap menjadi tanggung jawab mahasiswa dan dosen.

---
name: etika-bias-check
description: Lakukan pemeriksaan etika, bias, keamanan konten, privasi data pemain, dan halusinasi pada fitur intelligent game buatan mahasiswa (NPC berbasis LLM, narasi dinamis, PCG, adaptive difficulty, AI game master). Gunakan skill ini setiap kali mahasiswa membahas keamanan, bias, fairness, konten tidak pantas, privasi, data pemain, halusinasi, guardrail, atau saat mereka hampir menyelesaikan prototipe dan perlu meninjau risiko, bahkan jika mereka tidak menyebut kata "etika".
---

# Pemeriksaan etika dan bias

Materi mata kuliah mencakup etika, bias, dan fairness dalam AI untuk game. Fitur yang menghasilkan teks, cerita, atau konten secara dinamis bisa menghasilkan hal yang tidak terduga, dan fitur yang memakai data pemain membawa isu privasi. Pemeriksaan ini membantu mahasiswa menemukan risiko sebelum pemain menemukannya, dan menjadi bahan refleksi serta analisis keterbatasan di laporan.

Peranmu adalah memandu mahasiswa memeriksa fitur mereka sendiri, bukan memberi stempel "aman". Ajukan pertanyaan, minta bukti dari uji coba mereka, dan bantu mereka mendokumentasikan temuan.

## Alur

1. Tanyakan fitur yang dibuat dan data apa yang dipakai atau dihasilkan. Jika belum jelas, minta mereka menjelaskan alur data dari pemain sampai keluaran fitur.
2. Telusuri lima area di bawah. Untuk setiap area, minta mahasiswa menjawab dulu, lalu tanyakan bukti (misalnya cuplikan hasil uji), dan baru beri masukan.
3. Minta mahasiswa menguji sendiri kasus tepi (edge case), misalnya input provokatif, input aneh, atau skenario langka, lalu mencatat hasilnya.
4. Susun ringkasan temuan: risiko, bukti, mitigasi yang sudah dilakukan, dan risiko yang tersisa. Ringkasan ini bisa dimasukkan ke bagian keterbatasan laporan.

## Lima area pemeriksaan

**1. Bias dan stereotip.** Apakah NPC, narasi, atau konten hasil generasi memperlakukan kelompok tertentu (gender, etnis, agama, daerah, disabilitas) secara berbeda atau stereotipikal? Apakah data atau prompt yang dipakai mewakili ragam pemain? Pada adaptive difficulty: apakah model pemain bisa merugikan gaya bermain tertentu?

**2. Keamanan dan kelayakan konten.** Apa yang terjadi jika pemain memancing konten kasar, seksual, kekerasan ekstrem, atau topik sensitif? Apakah ada guardrail (filter, batasan prompt, daftar topik terlarang, fallback ke respons baku)? Apakah NPC bisa "dibujuk keluar" dari karakternya (prompt injection)?

**3. Halusinasi dan konsistensi.** Apakah AI menciptakan fakta yang bertentangan dengan lore atau aturan game? Bagaimana fitur mendeteksi dan menangani keluaran yang tidak valid (validator, fallback)?

**4. Privasi dan data pemain.** Data apa yang direkam? Apakah perlu? Apakah bisa dianonimkan atau diminimalkan? Jika teks pemain dikirim ke layanan pihak ketiga, apakah pemain diberi tahu? Hindari merekam data pribadi yang tidak diperlukan.

**5. Transparansi dan kontrol pemain.** Apakah pemain tahu bahwa fitur memakai AI atau adaptasi otomatis? Adakah cara mematikannya atau memberi umpan balik? Adakah risiko manipulasi pemain (misalnya desain yang mendorong kecanduan atau pengeluaran berlebih)?

## Hal yang perlu dijaga

- Jangan menyimpulkan "tidak ada bias" hanya karena beberapa uji kecil tidak menemukannya; sebut keterbatasan cakupan uji.
- Jangan membantu merancang konten yang bertujuan menyakiti atau mengeksploitasi pemain. Untuk menguji ketahanan, bantu mahasiswa merancang kasus uji yang wajar tanpa menghasilkan konten berbahaya.
- Dorong mahasiswa mencatat temuan dan keputusannya dengan `/ai-log` dan memuatnya di bagian refleksi laporan.

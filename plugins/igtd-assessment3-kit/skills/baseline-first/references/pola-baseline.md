# Pola baseline non-AI per opsi

Gunakan daftar ini untuk menawarkan 2-3 pilihan kepada mahasiswa. Sertakan trade-off, dan biarkan mahasiswa memilih.

## Opsi A: Intelligent NPC
- **Dialogue tree**: percabangan dialog tetap. Mudah dikontrol, tidak fleksibel.
- **Finite state machine (FSM)**: NPC punya state (ramah, curiga, marah) dengan transisi berbasis kondisi game state. Perilaku mudah diprediksi.
- **Response table berbasis kondisi**: tabel respons yang dipilih menurut game state, kepribadian, dan riwayat sederhana (misalnya flag "sudah pernah ditolong").
- Pembanding AI yang umum: respons dihasilkan LLM dengan persona, game state, dan riwayat percakapan.

## Opsi B: Dynamic Narrative
- **Graph cerita bercabang** dengan flag keputusan dan syarat percabangan.
- **Storylet / quality-based narrative**: potongan cerita dengan prasyarat state.
- Pembanding AI: LLM menulis teks adegan berdasarkan state cerita, sementara state machine tetap mengontrol alur.

## Opsi C: Procedural Content Generation
- **Random dengan constraint** dan validator (misalnya level harus bisa diselesaikan).
- **Template / grammar / tile-based rules**.
- **Search-based atau algoritma klasik** (wave function collapse, cellular automata, BSP) untuk level atau map.
- Pembanding AI: model generatif atau PCG via machine learning, tetap dengan validator keluaran.

## Opsi D: Adaptive Difficulty
- **Threshold statis** (misalnya turunkan kesulitan setelah N kali kalah berturut-turut).
- **Rule berbasis metrik performa** (akurasi, waktu, kematian per menit) dengan batas atas-bawah.
- Pembanding AI: model prediksi performa atau reinforcement learning untuk menyesuaikan parameter.

## Opsi E: AI Game Master
- **Event table terjadwal** dengan bobot dan syarat.
- **Director berbasis aturan** yang memantau tensi permainan dan memicu event.
- Pembanding AI: LLM atau agen yang memilih atau menulis tantangan, quest, atau narasi menurut kondisi permainan.

## Pertanyaan pemandu umum
- Apa yang bisa dilakukan versi AI yang tidak bisa dilakukan baseline ini?
- Apa yang bisa salah jika AI dipakai (keluar karakter, konten tidak pantas, latensi, biaya)?
- Bagaimana kamu akan memastikan perbandingan adil (kondisi uji sama, skenario sama)?

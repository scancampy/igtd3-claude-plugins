# Contoh metrik per fitur

Tawarkan sebagai titik awal, bukan daftar wajib. Minta mahasiswa memilih dan membenarkan pilihannya.

## Opsi A: Intelligent NPC
- Konsistensi persona (jumlah respons keluar karakter per 20 percakapan, dinilai dengan rubrik tertulis)
- Kesesuaian respons dengan game state (benar/salah per skenario)
- Variasi respons (jumlah respons unik per skenario berulang)
- Pelanggaran batas (spoiler, konten tidak pantas, informasi di luar dunia game)
- Latensi respons (detik) dan biaya per percakapan
- Skor persepsi pemain (survei 1-5: terasa hidup, terasa konsisten)

## Opsi B: Dynamic Narrative
- Koherensi cerita (kontradiksi fakta per alur, dinilai penguji)
- Responsivitas terhadap keputusan pemain (keputusan berdampak terlihat / total keputusan)
- Cakupan percabangan yang dialami pemain
- Pelanggaran kontinuitas (karakter atau fakta berubah tanpa sebab)
- Skor persepsi pemain (agency, keterlibatan)

## Opsi C: Procedural Content Generation
- Persentase konten yang valid/dapat diselesaikan
- Keragaman konten (misalnya jarak antar level, jumlah pola unik)
- Kesesuaian dengan target desain (kesulitan, panjang, kepadatan)
- Waktu generasi
- Skor persepsi pemain (variasi, kualitas)

## Opsi D: Adaptive Difficulty
- Proporsi pemain berada dalam "zona tantangan" (tidak terlalu mudah/sulit) menurut target desain
- Stabilitas penyesuaian (osilasi parameter dalam satu sesi)
- Waktu untuk mencapai kesulitan yang sesuai
- Tingkat frustrasi/bosan yang dilaporkan pemain
- Retensi dalam sesi uji (menyelesaikan atau berhenti)

## Opsi E: AI Game Master
- Kesesuaian event dengan kondisi permainan (benar/salah per skenario)
- Keseimbangan tantangan (variasi tensi sepanjang sesi)
- Keragaman event
- Pelanggaran aturan dunia game
- Persepsi pemain (kejutan, keadilan)

## Prinsip umum
- Gabungkan metrik objektif dan subjektif.
- Definisikan cara mengukur sebelum mengumpulkan data.
- Gunakan skenario dan input yang sama untuk baseline dan AI.
- Ulangi uji pada komponen yang acak atau berbasis LLM.

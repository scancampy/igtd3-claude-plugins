#!/usr/bin/env python3
"""Ringkas hasil uji baseline vs AI dari file CSV.

Format CSV (dengan header): condition,scenario,metric,value
- condition : baseline | ai (atau label lain)
- scenario  : nama skenario uji
- metric    : nama metrik
- value     : angka

Penggunaan:
    python3 ringkas_hasil.py hasil.csv
Keluaran: tabel Markdown berisi n, rata-rata, simpangan baku, min, maks per metrik dan kondisi.
"""
import csv
import statistics
import sys
from collections import defaultdict


def main(path):
    data = defaultdict(list)
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            needed = {"condition", "scenario", "metric", "value"}
            if not reader.fieldnames or not needed.issubset(set(reader.fieldnames)):
                print("Header CSV harus berisi kolom: condition,scenario,metric,value")
                return 1
            for i, row in enumerate(reader, start=2):
                try:
                    value = float(row["value"])
                except (TypeError, ValueError):
                    print(f"Peringatan: baris {i} dilewati (value bukan angka: {row['value']!r})")
                    continue
                data[(row["metric"].strip(), row["condition"].strip())].append(value)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {path}")
        return 1

    if not data:
        print("Tidak ada data yang dapat diringkas.")
        return 1

    print("| Metrik | Kondisi | n | Rata-rata | Simpangan baku | Min | Maks |")
    print("|---|---|---|---|---|---|---|")
    for (metric, cond) in sorted(data):
        v = data[(metric, cond)]
        sd = statistics.stdev(v) if len(v) > 1 else 0.0
        print(f"| {metric} | {cond} | {len(v)} | {statistics.mean(v):.2f} | {sd:.2f} | {min(v):.2f} | {max(v):.2f} |")

    print()
    print("Catatan: n kecil membuat selisih sulit disimpulkan. Sebutkan ukuran sampel dan keterbatasannya di laporan.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python3 ringkas_hasil.py hasil.csv")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))

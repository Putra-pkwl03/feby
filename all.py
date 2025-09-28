import math  # untuk ceil() dan floor()

def bucket_sort_iterasi(arr, k=None):
    if not arr:
        return []

    n = len(arr)
    k = n if k is None else k
    min_v, max_v = min(arr), max(arr)

    # Hitung 2 versi bucket_range:
    bucket_range_ceil = math.ceil((max_v - min_v + 1) / k)   # pembulatan ke atas
    bucket_range_floor = math.floor((max_v - min_v + 1) / k) # pembulatan ke bawah

    print("=== PERHITUNGAN RENTANG BUCKET ===")
    print(f"min={min_v}, max={max_v}, k={k}")
    print(f"bucket_range (ceil)  : {bucket_range_ceil}")
    print(f"bucket_range (floor) : {bucket_range_floor}\n")

    # =========================
    # PROSES DENGAN CEIL
    # =========================
    print("=== HASIL DENGAN PEMBULATAN KE ATAS (CEIL) ===")
    buckets_ceil = [[] for _ in range(k)]
    for i, v in enumerate(arr):
        idx = (v - min_v) // bucket_range_ceil
        if idx >= k:
            idx = k - 1
        buckets_ceil[idx].append(v)
        print(f"Iterasi {i+1}: {v} masuk ke bucket[{idx}] (range={bucket_range_ceil})")
        print("Status bucket:", buckets_ceil, "\n")

    # Sort setiap bucket (insertion sort)
    for b in buckets_ceil:
        b.sort()
    result_ceil = []
    for b in buckets_ceil:
        result_ceil.extend(b)

    print("Hasil akhir (ceil):", result_ceil, "\n")

    # =========================
    # PROSES DENGAN FLOOR
    # =========================
    print("=== HASIL DENGAN PEMBULATAN KE BAWAH (FLOOR) ===")
    buckets_floor = [[] for _ in range(k)]
    for i, v in enumerate(arr):
        idx = (v - min_v) // bucket_range_floor if bucket_range_floor != 0 else 0
        if idx >= k:
            idx = k - 1
        buckets_floor[idx].append(v)
        print(f"Iterasi {i+1}: {v} masuk ke bucket[{idx}] (range={bucket_range_floor})")
        print("Status bucket:", buckets_floor, "\n")

    # Sort setiap bucket (insertion sort)
    for b in buckets_floor:
        b.sort()
    result_floor = []
    for b in buckets_floor:
        result_floor.extend(b)

    print("Hasil akhir (floor):", result_floor, "\n")

    return result_ceil, result_floor

# Contoh penggunaan
data = [35, 12, 78, 45, 22, 90, 15, 68, 55, 31]
hasil_ceil, hasil_floor = bucket_sort_iterasi(data)

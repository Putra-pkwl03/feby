import math #Mengimpor modul math untuk menggunakan fungsi ceil() (pembulatan ke atas).

def bucket_sort_iterasi(arr, k=None):
    if not arr:
        return []

    # Penjelasan:
    # n: jumlah elemen dalam array
    # k: jumlah bucket (jika tidak ditentukan, gunakan n)
    # min_v & max_v: nilai terkecil dan terbesar dalam array
    # bucket_range: rentang nilai dalam 1 bucket
    #  dihitung dari (max - min + 1) / k dan dibulatkan ke atas.
    n = len(arr)
    k = n if k is None else k
    min_v, max_v = min(arr), max(arr)
    bucket_range = math.ceil((max_v - min_v + 1) / k)

    print("=== TAHAP 1: PENEMPATAN KE BUCKET ===")
    print(f"min={min_v}, max={max_v}, k={k}, bucket_range={bucket_range}\n")

    # 1 Membuat bucket kosong
    buckets = [[] for _ in range(k)]

    # 2 Iterasi: masukkan elemen ke bucket
    # idx = (v - min_v)//bucket_range: menentukan elemen masuk bucket mana.
    # Jika idx melebihi jumlah bucket (k), paksa ke k-1 agar tidak error.
    # Tambahkan elemen v ke bucket yang sesuai.
    # print() digunakan untuk menampilkan proses iterasi setiap langkah.
    for i, v in enumerate(arr):
        idx = (v - min_v) // bucket_range
        if idx >= k:  
            idx = k - 1
        buckets[idx].append(v)
        print(f"Iterasi {i+1}: {v} masuk ke bucket[{idx}]")
        print("Status bucket:", buckets, "\n")

    # 3 Iterasi: urutkan tiap bucket
    # Loop semua bucket.
    # Jika isi > 1, lakukan Insertion Sort (karena cepat untuk data kecil).
    # Proses insertion sort dijelaskan langkah demi langkah:
    # Ambil key (elemen yang akan diposisikan)
    # Bandingkan dengan elemen sebelumnya (b[k_idx] > key)
    # Jika lebih besar → geser ke kanan
    # Ulangi sampai posisi yang benar ditemukan
    print("\n=== TAHAP 2: SORTING SETIAP BUCKET ===")
    for i, b in enumerate(buckets):
        if len(b) > 1:
            print(f"Bucket[{i}] sebelum sort: {b}")
            # insertion sort detail
            for j in range(1, len(b)):
                key = b[j]
                k_idx = j - 1
                print(f"  i={j}, key={key}")
                while k_idx >= 0 and b[k_idx] > key:
                    print(f"    compare {b[k_idx]} > {key}? YES -> geser")
                    b[k_idx + 1] = b[k_idx]
                    k_idx -= 1
                b[k_idx + 1] = key
                print("    status sementara:", b)
            print(f"Bucket[{i}] setelah sort:", b, "\n")
        else:
            if b:
                print(f"Bucket[{i}] tidak perlu sort (isi 1 elemen): {b}")

    # 4 Iterasi: gabungkan hasil dari semua bucket
    # result = []: list kosong sebagai hasil akhir.
    # Loop semua bucket dari indeks 0 → k-1.
    # Gabungkan isi tiap bucket secara berurutan.
    # Cetak hasil setiap kali bucket digabungkan.
    print("\n=== TAHAP 3: PENGGABUNGAN ===")
    result = []
    for i, b in enumerate(buckets):
        print(f"Gabungkan bucket[{i}]: {b}")
        result.extend(b)
        print("Status hasil sementara:", result)

    print("\n=== HASIL AKHIR ===")
    print("Array terurut:", result)
    return result

# Contoh penggunaan
data = [35, 12, 78, 45, 22, 90, 15, 68, 55, 31]
sorted_arr = bucket_sort_iterasi(data)

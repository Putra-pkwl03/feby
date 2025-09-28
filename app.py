def bucket_sort_iterasi(arr, k=None):
    if not arr:
        return []

    # n: jumlah elemen dalam array
    # k: jumlah bucket (jika tidak ditentukan, gunakan n)
    # min_v & max_v: nilai terkecil dan terbesar dalam array
    # bucket_range: rentang nilai dalam 1 bucket
    #  dihitung dari (max - min + 1) / k dan dibulatkan ke atas.
    n = len(arr)
    k = n if k is None else k
    min_v, max_v = min(arr), max(arr)

    # ✅ Pembulatan ke atas tanpa math.ceil()
    # (max_v - min_v + 1): total rentang nilai data
    # + (k - 1): trik pembulatan ke atas secara manual
    # // k: pembagian bulat untuk mendapatkan panjang rentang tiap bucket
    bucket_range = ((max_v - min_v + 1) + (k - 1)) // k

    print("=== TAHAP 1: PENEMPATAN KE BUCKET ===")
    print(f"min={min_v}, max={max_v}, k={k}, bucket_range={bucket_range}\n")

    # 1 Membuat bucket kosong
    # Membuat list kosong sejumlah k untuk menampung data berdasarkan rentangnya
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
            # Proses sorting menggunakan Insertion Sort
            for j in range(1, len(b)):
                key = b[j]                  # key: elemen yang akan diposisikan
                k_idx = j - 1              # k_idx: posisi elemen sebelumnya
                print(f"  i={j}, key={key}")
                # Bandingkan key dengan elemen sebelumnya satu per satu
                while k_idx >= 0 and b[k_idx] > key:
                    print(f"    compare {b[k_idx]} > {key}? YES -> geser")
                    b[k_idx + 1] = b[k_idx] # geser elemen ke kanan
                    k_idx -= 1
                # Tempatkan key pada posisi yang benar
                b[k_idx + 1] = key
                print("    status sementara:", b)
            print(f"Bucket[{i}] setelah sort:", b, "\n")
        else:
            if b:
                # Jika hanya ada 1 elemen, tidak perlu sorting
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
        result.extend(b)  # extend: menggabungkan isi bucket ke hasil akhir
        print("Status hasil sementara:", result)

    # Menampilkan hasil akhir setelah semua bucket digabungkan
    print("\n=== HASIL AKHIR ===")
    print("Array terurut:", result)
    return result

# Contoh penggunaan
data = [35, 12, 78, 45, 22, 90, 15, 68, 55, 31]
sorted_arr = bucket_sort_iterasi(data)

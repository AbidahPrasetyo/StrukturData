# ==========================================
# 1. Deduplikasi
# ==========================================
def deduplikasi(data_list):
    """
    Menghapus duplikat dari list dengan mempertahankan urutan pertama kali muncul.
    Menggunakan set untuk pelacakan.
    """
    seen = set()
    result = []
    for item in data_list:
        if item not in seen:
            result.append(item)
            seen.add(item)  # Tambahkan ke set pelacakan
    return result


# ==========================================
# 2. Intersection Dua Array
# ==========================================
def intersection(list1, list2):
    """
    Mengembalikan elemen yang muncul di kedua list.
    """
    # Menggunakan set intersection (&) lebih efisien di Python
    return list(set(list1) & set(list2))


# ==========================================
# 3. Anagram Check
# ==========================================
def is_anagram(str1, str2):
    """
    Menentukan apakah dua string adalah anagram menggunakan dictionary (dict).
    """
    # Membersihkan spasi dan mengubah ke huruf kecil agar akurat
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Jika panjangnya beda, sudah pasti bukan anagram
    if len(str1) != len(str2):
        return False

    char_counts = {}
    
    # Menghitung karakter di string pertama
    for char in str1:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Mengurangi hitungan berdasarkan string kedua
    for char in str2:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True


# ==========================================
# 4. First Recurring Character
# ==========================================
def first_recurring_character(text):
    """
    Mencari karakter pertama yang muncul lebih dari sekali menggunakan set.
    """
    seen = set()
    for char in text:
        if char in seen:
            return char  # Langsung return saat menemukan duplikat pertama
        seen.add(char)
    return None # Jika tidak ada yang berulang


# ==========================================
# 5. Simulasi Buku Telepon
# ==========================================
def simulasi_buku_telepon():
    """
    Program sederhana buku telepon dengan menu CRUD dasar.
    """
    kontak = {} # Menggunakan dictionary untuk menyimpan Nama -> Nomor
    
    while True:
        print("\n=== Menu Buku Telepon ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            nomor = input("Masukkan Nomor Telepon: ")
            kontak[nama] = nomor
            print(f"✅ Kontak '{nama}' berhasil ditambahkan!")
            
        elif pilihan == '2':
            nama = input("Masukkan Nama yang dicari: ")
            if nama in kontak:
                print(f"📞 Nomor telepon {nama}: {kontak[nama]}")
            else:
                print(f"❌ Kontak '{nama}' tidak ditemukan.")
                
        elif pilihan == '3':
            if not kontak:
                print("Buku telepon masih kosong.")
            else:
                print("\n--- Daftar Kontak ---")
                for nama, nomor in kontak.items():
                    print(f"- {nama}: {nomor}")
                print("---------------------")
                
        elif pilihan == '4':
            print("Keluar dari program. Terima kasih!")
            break
            
        else:
            print("⚠️ Pilihan tidak valid, silakan coba lagi.")


# ==========================================
# BLOK PENGUJIAN (TESTING)
# ==========================================
if __name__ == "__main__":
    print("--- Test No. 1: Deduplikasi ---")
    data_awal = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
    print(f"Input : {data_awal}")
    print(f"Output: {deduplikasi(data_awal)}\n")

    print("--- Test No. 2: Intersection ---")
    array1 = [1, 2, 3, 4, 5]
    array2 = [4, 5, 6, 7, 8]
    print(f"Array 1: {array1} | Array 2: {array2}")
    print(f"Output : {intersection(array1, array2)}\n")

    print("--- Test No. 3: Anagram Check ---")
    kata1 = "Kasur Rusak"
    kata2 = "Kuasa Rusk r"
    print(f"'{kata1}' & '{kata2}' -> Anagram? {is_anagram(kata1, kata2)}")
    print(f"'Makan' & 'Minum' -> Anagram? {is_anagram('Makan', 'Minum')}\n")

    print("--- Test No. 4: First Recurring Character ---")
    teks_uji = "BCABA"
    print(f"Teks '{teks_uji}' -> Karakter berulang pertama: {first_recurring_character(teks_uji)}\n")

    print("--- Test No. 5: Simulasi Buku Telepon ---")
    print("Menjalankan simulasi buku telepon...")
    simulasi_buku_telepon()
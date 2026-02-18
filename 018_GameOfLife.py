import time
import os

# BAGIAN 1: STRUKTUR DATA (ADT ARRAY)
class Array:
    """
    Ini adalah implementasi ADT Array.
    Ukurannya TETAP setelah dibuat, tidak bisa ditambah/dikurang (append/pop).
    """
    def __init__(self, size):
        # Membuat array dengan ukuran tertentu, isinya kosong (None) dulu
        # Meskipun di dalamnya pakai list Python, kita batasi fiturnya biar kayak Array beneran
        self._items = [None] * size

    def __len__(self):
        # Mengembalikan panjang array
        return len(self._items)

    def __getitem__(self, index):
        # Mengambil isi data di posisi index
        return self._items[index]

    def __setitem__(self, index, value):
        # Mengisi data di posisi index
        self._items[index] = value

    def clear(self, value):
        # Membersihkan seluruh isi array dengan nilai tertentu
        for i in range(len(self._items)):
            self._items[i] = value

# BAGIAN 2: PAPAN PERMAINAN (GRID)
class LifeGrid:
    """
    Ini merepresentasikan papan permainan 2 Dimensi.
    Kita menggunakan ADT Array di atas untuk membuat baris dan kolom.
    """
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        
        # Membuat Array utama untuk menyimpan baris-baris
        self._grid = Array(rows)
        
        # Di setiap baris, kita buat lagi Array untuk menyimpan kolom (sel)
        for i in range(rows):
            self._grid[i] = Array(cols)
            # Isi awal dengan sel MATI (Dead)
            self._grid[i].clear(self.DEAD_CELL)

    # Konstanta untuk status sel
    DEAD_CELL = 0  # Mati
    LIVE_CELL = 1  # Hidup

    def num_rows(self):
        return self._rows

    def num_cols(self):
        return self._cols

    def configure(self, coord_list):
        # Mengaktifkan sel hidup berdasarkan daftar koordinat
        # Contoh input: [(1, 2), (2, 2), (3, 2)]
        for r, c in coord_list:
            self.set_cell(r, c)

    def is_live_cell(self, row, col):
        # Mengecek apakah sel di posisi (row, col) hidup?
        return self._grid[row][col] == self.LIVE_CELL

    def set_cell(self, row, col):
        # Menghidupkan sel
        self._grid[row][col] = self.LIVE_CELL

    def clear_cell(self, row, col):
        # Mematikan sel
        self._grid[row][col] = self.DEAD_CELL

    def num_live_neighbors(self, row, col):
        """
        Menghitung jumlah tetangga hidup di sekitar sel (row, col).
        Mengecek 8 arah mata angin.
        """
        live_neighbors = 0
        
        # Loop dari baris atasnya (-1) sampai bawahnya (+1)
        for i in range(row - 1, row + 2):
            # Loop dari kolom kirinya (-1) sampai kanannya (+1)
            for j in range(col - 1, col + 2):
                
                # Jangan hitung diri sendiri!
                if i == row and j == col:
                    continue
                
                # Pastikan koordinat valid (tidak keluar dari papan)
                if (0 <= i < self.num_rows()) and (0 <= j < self.num_cols()):
                    if self.is_live_cell(i, j):
                        live_neighbors += 1
                        
        return live_neighbors

# BAGIAN 3: LOGIKA UTAMA (SIMULASI)

def draw(grid):
    """Fungsi untuk menggambar grid ke layar terminal"""
    # Bersihkan layar terminal (cls untuk Windows, clear untuk Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- GENEASI BARU ---")
    for r in range(grid.num_rows()):
        line = ""
        for c in range(grid.num_cols()):
            if grid.is_live_cell(r, c):
                line += " O "  # Karakter untuk sel Hidup
            else:
                line += " . "  # Karakter untuk sel Mati
        print(line)
    print("\nTekan Ctrl+C untuk berhenti.")

def evolve(grid):
    """
    Fungsi untuk menciptakan Generasi Berikutnya.
    Kita TIDAK BOLEH mengubah grid secara langsung saat sedang menghitung,
    jadi kita buat grid baru untuk menampung hasilnya.
    """
    rows = grid.num_rows()
    cols = grid.num_cols()
    
    # 1. Buat grid baru yang kosong
    new_grid = LifeGrid(rows, cols)
    
    # 2. Periksa setiap sel di grid lama
    for r in range(rows):
        for c in range(cols):
            # Hitung tetangga hidup
            neighbors = grid.num_live_neighbors(r, c)
            
            # --- TERAPKAN 4 ATURAN GAME OF LIFE ---
            
            # Cek status sekarang
            if grid.is_live_cell(r, c):
                # ATURAN 1 & 2 & 3 (Untuk sel HIDUP)
                if neighbors == 2 or neighbors == 3:
                    new_grid.set_cell(r, c) # Tetap Hidup
                else:
                    new_grid.clear_cell(r, c) # Mati (Kesepian atau Kepadatan)
            else:
                # ATURAN 4 (Untuk sel MATI)
                if neighbors == 3:
                    new_grid.set_cell(r, c) # Lahir Baru (Reproduksi)
                else:
                    new_grid.clear_cell(r, c) # Tetap Mati

    return new_grid

def main():
    # 1. Tentukan ukuran papan (Contoh: 10 baris, 10 kolom)
    rows = 10
    cols = 10
    grid = LifeGrid(rows, cols)
    
    # 2. Tentukan Pola Awal
    # Kita coba pola "Blinker" (Osilator sederhana) dan "Glider" (Pesawat)
    # Blinker (Garis Vertikal)
    blinker = [(2, 1), (3, 1), (4, 1)]
    
    # Glider (Bentuk seperti pesawat kecil)
    glider = [(1, 7), (2, 8), (3, 6), (3, 7), (3, 8)]
    
    # Masukkan pola ke grid
    grid.configure(blinker)
    grid.configure(glider)
    
    # 3. Jalankan Simulasi
    try:
        while True:
            draw(grid)          # Gambar papan
            grid = evolve(grid) # Hitung generasi selanjutnya
            time.sleep(1)       # Tunggu 1 detik agar tidak terlalu cepat
            
    except KeyboardInterrupt:
        print("\nSimulasi dihentikan.")

# Menjalankan program utama
if __name__ == "__main__":

    main()

import pyodbc

server = '192.168.1.33\\SQLEXPRESS01'  # Bisa berupa alamat IP atau nama host
database = 'lol'
username = 'sa'
password = 'bejokun'
# Fungsi untuk memeriksa koneksi
def check_connection():
    try:
        # Membuat koneksi
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};'
                              f'SERVER={server};'
                              f'DATABASE={database};'
                              f'UID={username};'
                              f'PWD={password}')
        print("Koneksi berhasil ke database.")
        conn.close()  # Tutup koneksi setelah pengecekan
        return True
    except Exception as e:
        print(f"Gagal terhubung ke database: {e}")
        return False

# Memeriksa koneksi
if check_connection():
    print("Koneksi berhasil. Anda dapat melanjutkan ke operasi query.")
else:
    print("Tidak dapat melakukan koneksi. Periksa kembali kredensial atau status server.")

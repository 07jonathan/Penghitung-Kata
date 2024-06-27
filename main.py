def hitung_kata(teks):
    # Menghapus spasi di awal dan akhir teks
    teks = teks.strip()
    # Memisahkan teks menjadi daftar kata-kata
    kata_kata = teks.split()
    # Menghitung jumlah kata
    jumlah_kata = len(kata_kata)
    return jumlah_kata

# Meminta input dari pengguna
teks = input("Masukkan teks: ")
jumlah_kata = hitung_kata(teks)
print(f"Jumlah kata: {jumlah_kata}")

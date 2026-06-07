🪸 Aplikasi Deteksi Dini Pemutihan Terumbu Karang

Aplikasi berbasis Streamlit dan Convolutional Neural Network (CNN) untuk mendeteksi kondisi terumbu karang berdasarkan citra digital. Sistem akan mengklasifikasikan gambar ke dalam dua kategori:

Healthy Coral (Sehat)
Bleached Coral (Memutih/Sakit)
📋 Persyaratan Sistem

Pastikan perangkat telah terpasang:

Python 3.10 atau lebih baru
TensorFlow
Streamlit
NumPy
Pillow (PIL)
📦 Instalasi Library

Buka Command Prompt pada folder proyek kemudian jalankan:

pip install streamlit tensorflow numpy pillow

Atau gunakan file requirements.txt:

pip install -r requirements.txt
📁 Struktur Folder Proyek

Susun folder proyek seperti berikut:

Coral-app/
│
├── app.py
├── coral_model.keras
├── requirements.txt
└── README.md

Keterangan:

File	Fungsi
app.py	Program utama Streamlit
coral_model.keras	Model CNN hasil training
requirements.txt	Daftar library yang dibutuhkan
README.md	Dokumentasi penggunaan aplikasi
▶ Menjalankan Aplikasi

Masuk ke folder proyek:

cd Coral-app

Kemudian jalankan:

streamlit run app.py

Jika berhasil, terminal akan menampilkan:

Local URL: http://localhost:8501

Buka alamat tersebut pada browser.

🖼 Cara Menggunakan Aplikasi
1. Buka Halaman Utama

Setelah aplikasi berjalan, halaman utama akan menampilkan:

Judul aplikasi
Deskripsi sistem
Menu input gambar
2. Pilih Metode Input

Terdapat dua metode input:

📁 Upload Gambar

Klik:

Pilih file gambar terumbu karang

Format yang didukung:

JPG
JPEG
PNG
📷 Kamera

Klik:

Ambil Foto via Kamera

Kemudian ambil gambar langsung menggunakan webcam.

3. Jalankan Klasifikasi

Setelah gambar berhasil dimuat:

Klik tombol:

Jalankan Klasifikasi Citra

Sistem akan melakukan:

Resize gambar menjadi 224 × 224 piksel
Normalisasi citra
Prediksi menggunakan model CNN
Menampilkan hasil klasifikasi
📊 Hasil Klasifikasi

Sistem akan menampilkan salah satu hasil berikut:

Healthy Coral (Sehat)

Menunjukkan bahwa terumbu karang terdeteksi dalam kondisi sehat.

Contoh tampilan:

KONDISI AMAN
Healthy Coral (Sehat)
Bleached Coral (Memutih/Sakit)

Menunjukkan adanya indikasi pemutihan pada terumbu karang.

Contoh tampilan:

KONDISI KRITIS
Bleached Coral (Memutih/Sakit)
📈 Confidence Score

Aplikasi juga menampilkan tingkat keyakinan model terhadap hasil klasifikasi.

Contoh:

Confidence Score : 92.35%

Semakin tinggi nilai confidence, semakin yakin model terhadap hasil prediksi.

⚠ Troubleshooting
Model Tidak Ditemukan

Pesan:

File coral_model.keras tidak ditemukan

Solusi:

Pastikan file coral_model.keras berada pada folder yang sama dengan app.py.
TensorFlow Belum Terpasang

Pesan:

ModuleNotFoundError: No module named 'tensorflow'

Solusi:

pip install tensorflow
Streamlit Belum Terpasang

Pesan:

ModuleNotFoundError: No module named 'streamlit'

Solusi:

pip install streamlit
👨‍💻 Pengembang

Kelompok 5 – Teknik Informatika UMRAH

Anggota:
Meyza Zaharanie
Putri Ramadhanti
Rani Nadia Sihombing
Luvita Septiana Putri

Mata Kuliah: Pengolahan Citra Digital
Program Studi: Teknik Informatika
Universitas Maritim Raja Ali Haji (UMRAH)
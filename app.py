import streamlit as st
import numpy as np
from PIL import Image
import os
# Mengganti TensorFlow raksasa dengan runtime TFLite yang super ringan
import tflite_runtime.interpreter as tflite

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Deteksi Coral Bleaching | Kelompok 5",
    page_icon="🪸",
    layout="centered"
)

# ==========================================
# 2. LOAD MODEL TFLITE (ANTI-CRASH SERVER RAM)
# ==========================================
# Menggunakan decorator cache agar model hanya dimuat 1 kali ke RAM server Hugging Face
@st.cache_resource
def load_my_model():
    # Menunjuk langsung ke nama file model TFLite hasil download kamu dari Colab
    model_name = "model_coral_efficientnet.tflite"
    if os.path.exists(model_name):
        try:
            # Memuat model menggunakan TFLite Interpreter
            interpreter = tflite.Interpreter(model_path=model_name)
            interpreter.allocate_tensors()
            return interpreter
        except Exception as e:
            st.error(f"Eror saat membaca berkas model TFLite: {e}")
            return None
    return None

interpreter = load_my_model()

# ==========================================
# 3. PREPROCESSING GAMBAR
# ==========================================
IMG_SIZE = 224

def preprocess_image(image):
    # Memastikan gambar dalam format RGB (bukan RGBA transparan)
    image = image.convert("RGB")
    # Mengubah ukuran gambar sesuai input dataset saat training (224x224)
    image = image.resize((IMG_SIZE, IMG_SIZE))
    
    # Mengubah citra menjadi array dan melakukan normalisasi pixel (0-1)
    img_array = np.array(image)
    img_array = img_array.astype(np.float32) / 255.0
    # Menambahkan dimensi batch (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# ==========================================
# 4. HEADER TAMPILAN
# ==========================================
st.title("🪸 Aplikasi Deteksi Dini Pemutihan Terumbu Karang")
st.subheader("Metode Convolutional Neural Network Berbasis Web")
st.caption("Proyek Tugas Besar Mata Kuliah Pengolahan Citra Digital — Teknik Informatika UMRAH")
st.markdown("---")

# ==========================================
# 5. INPUT GAMBAR (UPLOAD & KAMERA)
# ==========================================
st.markdown("### 📸 Pilih Metode Input Citra")

tab1, tab2 = st.tabs([
    "📁 Unggah Berkas Gambar",
    "📷 Ambil Foto via Kamera"
])

uploaded_file = None

with tab1:
    file_input = st.file_uploader(
        "Pilih file gambar terumbu karang",
        type=["jpg", "jpeg", "png"]
    )
    if file_input is not None:
        uploaded_file = file_input

with tab2:
    camera_input = st.camera_input(
        "Posisikan objek tepat di depan kamera"
    )
    if camera_input is not None:
        uploaded_file = camera_input

# ==========================================
# 6. PROSES PREDIKSI REAL-TIME (AI ASLI TFLITE)
# ==========================================
if uploaded_file is not None:
    # Membuka berkas gambar yang dimasukkan pengguna
    image = Image.open(uploaded_file)

    # Menampilkan gambar ke layar web streamlit
    st.image(
        image,
        caption="Citra Terumbu Karang Berhasil Dimuat",
        use_container_width=True
    )

    st.success("✔ Berkas citra berhasil dimuat")

    # Tombol pemicu klasifikasi AI
    if st.button("Jalankan Klasifikasi Citra", type="primary"):
        st.markdown("---")
        st.markdown("### 📊 Hasil Analisis")

        # Cek apakah objek interpreter TFLite berhasil dimuat atau tidak
        if interpreter is None:
            st.error("⚠️ File 'model_coral_efficientnet.tflite' tidak ditemukan atau gagal dimuat di server.")
        else:
            with st.spinner("Menganalisis gambar dengan AI..."):
                try:
                    # 1. Jalankan fungsi pra-pemrosesan citra
                    img_tensor = preprocess_image(image)

                    # Get input & output details untuk TFLite
                    input_details = interpreter.get_input_details()
                    output_details = interpreter.get_output_details()

                    # 2. Prediksi menggunakan model CNN versi TFLite
                    interpreter.set_tensor(input_details[0]['index'], img_tensor)
                    interpreter.invoke()
                    prediction = interpreter.get_tensor(output_details[0]['index'])
                    
                    raw_score = float(prediction[0][0])

                    # Log Nilai Mentah untuk Keperluan Evaluasi Akurasi
                    st.info(f"Raw Score Model : {raw_score:.4f}")

                    # 3. Logika Penentuan Batas Klasifikasi (Threshold)
                    # > 0.5 = Sehat, <= 0.5 = Sakit/Memutih
                    if raw_score > 0.5:
                        hasil = "Healthy Coral (Sehat)"
                        confidence = raw_score * 100

                        st.success(f"### KONDISI AMAN: {hasil}")
                        st.markdown(
                            """
                            <div style="background-color:#e6f4ea; padding:15px; border-radius:10px; border-left:5px solid #137333; color:#1e1e1e;">
                                <strong>Hasil Analisis:</strong> Terumbu karang dinilai dalam kondisi sehat dan memiliki pigmen warna normal.
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    else:
                        hasil = "Bleached Coral (Memutih/Sakit)"
                        confidence = (1 - raw_score) * 100

                        st.error(f"### KONDISI KRITIS: {hasil}")
                        st.markdown(
                            """
                            <div style="background-color:#ffe6e6; padding:15px; border-radius:10px; border-left:5px solid #ff4b4b; color:#1e1e1e;">
                                <strong>Hasil Analisis:</strong> Terumbu karang terdeteksi mengalami bleaching (pemutihan massal). Perlu perhatian khusus.
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    # 4. Tampilan Metrik Output Akhir
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Status Klasifikasi", "Selesai ✔")
                    with col2:
                        st.metric("Confidence Score", f"{confidence:.2f}%")
                        
                except Exception as e:
                    st.error(f"Terjadi kesalahan saat memproses gambar dengan TFLite: {e}")

# ==========================================
# 7. FOOTER IDENTITAS KELOMPOK
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:#888888;font-size:0.85em;">
        <strong>Dibuat oleh Kelompok 5 - Teknik Informatika UMRAH</strong><br>
        Syawal Rizal Utama | Meyza Zaharanie | Putri Ramadhanti | Zony Fatma Mulia |<br>
        Tommy Susanto | Rusydi Ardani | Rani Nadia Sihombing | Luvita Septiana Putri
    </div>
    """,
    unsafe_allow_html=True
)
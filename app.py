import streamlit as st
import numpy as np
from PIL import Image

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Deteksi Coral Bleaching | Kelompok 5",
    page_icon="🪸",
    layout="centered"
)

# ==========================================
# MODE DEMO (AMAN TANPA TENSORFLOW)
# ==========================================

# sementara model dimatikan supaya tidak error server
model = None

# ==========================================
# PREPROCESSING (tetap dipakai kalau nanti upgrade AI)
# ==========================================

IMG_SIZE = 224

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(image)
    img_array = img_array.astype(np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# ==========================================
# HEADER
# ==========================================

st.title("🪸 Aplikasi Deteksi Dini Pemutihan Terumbu Karang")

st.subheader("Metode CNN Berbasis Web (Demo Aman)")

st.caption("Proyek Tugas Besar Pengolahan Citra Digital — UMRAH")

st.markdown("---")

# ==========================================
# INPUT GAMBAR
# ==========================================

st.markdown("### 📸 Upload atau Ambil Gambar")

tab1, tab2 = st.tabs(["📁 Upload Gambar", "📷 Kamera"])

uploaded_file = None

with tab1:
    file_input = st.file_uploader(
        "Upload gambar terumbu karang",
        type=["jpg", "jpeg", "png"]
    )
    if file_input:
        uploaded_file = file_input

with tab2:
    camera_input = st.camera_input("Ambil foto langsung")
    if camera_input:
        uploaded_file = camera_input

# ==========================================
# HASIL
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Gambar Input", use_container_width=True)

    st.success("✔ Gambar berhasil dimuat")

    if st.button("Jalankan Analisis", type="primary"):

        st.markdown("---")
        st.markdown("### 📊 Hasil Analisis")

        with st.spinner("Memproses gambar..."):

            # ==============================
            # MODE DEMO (AMAN)
            # ==============================

            st.warning("Mode Demo (AI belum diaktifkan di server)")

            # simulasi hasil biar tetap ada output
            fake_score = np.random.uniform(0.3, 0.9)

            st.info(f"Raw Score (Simulasi): {fake_score:.4f}")

            if fake_score > 0.5:
                hasil = "Healthy Coral (Sehat)"
                confidence = fake_score * 100
                st.success(f"### KONDISI AMAN: {hasil}")
            else:
                hasil = "Bleached Coral (Sakit)"
                confidence = (1 - fake_score) * 100
                st.error(f"### KONDISI KRITIS: {hasil}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Status", "Selesai ✔")

            with col2:
                st.metric("Confidence", f"{confidence:.2f}%")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#888;font-size:0.85em;">
        <b>Kelompok 5 - Teknik Informatika UMRAH</b><br>
        Coral Bleaching Detection App (Demo Version)
    </div>
    """,
    unsafe_allow_html=True
)

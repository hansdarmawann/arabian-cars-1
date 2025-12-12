# 🧭 TDSP Project Summary — Used Car Price Prediction (Syarah.com)

> **Framework:** Microsoft Team Data Science Process (TDSP)  
> **Goal:** Memprediksi harga wajar mobil bekas di Arab Saudi berdasarkan data historis listing Syarah.com  
> **Approach:** Iteratif & agile — dari business understanding hingga stakeholder validation.

---

## 🧩 TDSP Lifecycle Overview

| Step | Deskripsi Singkat |
|------|--------------------|
| **1. Business Understanding** | Mendefinisikan tujuan bisnis dan metrik keberhasilan. |
| **2. Data Acquisition & Understanding** | Mengumpulkan dan mengeksplorasi data mentah. |
| **3. Data Preparation & Feature Engineering** | Membersihkan dan membentuk fitur untuk modeling. |
| **4. Modeling** | Membangun dan mengevaluasi beberapa model prediktif. |
| **5. Deployment** | Menyimpan dan menyiapkan model untuk digunakan di sistem nyata. |
| **6. Customer Acceptance** | Memvalidasi hasil model dengan stakeholder bisnis. |

---

## 1️⃣ Business Understanding

- **Tujuan:** Memberikan estimasi harga wajar mobil bekas untuk membantu keputusan jual/beli.  
- **Pertanyaan utama:**  
  - Faktor apa yang paling memengaruhi harga mobil?  
  - Seberapa akurat prediksi dibanding harga pasar?  
- **Metrik sukses:** MAE ≤ 10% median harga, MAPE ≤ 20%.  

---

## 2️⃣ Data Acquisition & Understanding

- **Sumber data:** Listing mobil bekas dari [Syarah.com](https://syarah.com).  
- **Fitur utama:** Merk, model, tahun, region, mileage, engine size, harga, dan lainnya.  
- **Langkah utama:**  
  - Load dataset `UsedCarsSA_Unclean_EN.csv`.  
  - Data dictionary dan statistik deskriptif.  
  - Pemeriksaan nilai unik per kolom.  
- **Outcome:** Pemahaman kualitas data dan identifikasi fitur penting (`Year`, `Mileage`, `Engine_Size`, dll).

---

## 3️⃣ Data Preparation & Feature Engineering

- **Pembersihan data:**  
  - Imputasi `Engine_Size` (modus per `(Type, Year)`), `Gear_Type` (modus global).  
  - Hapus kolom non-informatif: `Link`, `Condition`, `Negotiable`.  
  - Filter outlier harga (1–99% kuantil).  
- **Fitur tambahan:**  
  - `Car_Age = 2025 - Year`.  
- **Outcome:** Dataset bersih `UsedCarsSA_Clean.csv` siap modeling.

---

## 4️⃣ Modeling

- **Setup:**  
  - Target: `Price`  
  - Train/test: 80/20 split  
- **Preprocessing pipeline:**  
  - Numerik → imputasi median + scaling  
  - Kategorikal → imputasi modus + one-hot encoding  
- **Model yang diuji:**  
  - Linear Regression (baseline)  
  - Random Forest  
  - Gradient Boosting  
  - XGBoost  
- **Evaluasi:** MAE, MAPE, RMSE, R²  
- **Hasil:**  
  - Model tree-based (Random Forest / XGBoost) memberikan performa terbaik.

---

## 5️⃣ Deployment

- **Langkah:**  
  - Melatih model terbaik dan menyimpannya: `used_car_price_model_rf.joblib`.  
  - Menyediakan fungsi `predict_price(record)` untuk inferensi cepat.  
- **Integrasi:**  
  - API (FastAPI/Flask) → prediksi real-time.  
  - Batch scoring → analisis berkala.  
  - Output → rekomendasi harga dan rentang harga wajar di UI.

---

## 6️⃣ Customer / Stakeholder Acceptance

- **Validasi metrik:** MAE, MAPE, RMSE, R² dihitung ulang di data uji.  
- **Analisis error:**  
  - `error_df` berisi harga aktual vs prediksi, Absolute Error, APE.  
  - Analisis per `Type` dan `Region` untuk deteksi segmen rawan error.  
- **Kesimpulan:**  
  - Model cukup stabil untuk segmen umum.  
  - Error tinggi pada segmen langka → kandidat iterasi berikutnya.  
- **Dokumentasi hand-off:**  
  - File model, notebook TDSP, dan panduan retraining.

---

## ⚙️ Agile & TDSP Alignment

- **Iteratif:** hasil evaluasi dapat memicu perbaikan dari tahap mana pun.  
- **Kolaboratif:** stakeholder dilibatkan di awal & akhir proyek.  
- **Adaptif:** mudah menyesuaikan perubahan kebutuhan bisnis.

---

## ⚠️ Limitasi & Rekomendasi

**Limitasi:**
- Tidak mempertimbangkan kondisi visual mobil (tidak ada data gambar/teks).
- Error tinggi pada segmen dengan data sedikit.
- Harga pasar bisa berubah cepat (perlu retraining berkala).

**Next Steps:**
- Tambah fitur deskriptif (NLP / inspeksi).  
- Lakukan hyperparameter tuning lanjut (GridSearch, Optuna).  
- Bangun monitoring pipeline untuk deteksi data drift.  
- Gunakan feedback pengguna untuk iterasi model berikutnya.

---

## ✅ Kesimpulan Akhir

Proyek ini menunjukkan implementasi **TDSP end-to-end** untuk problem nyata:  
membangun, mengevaluasi, dan mendeliver model prediksi harga mobil bekas.

Model ini:
- **Siap di-deploy** dan digunakan untuk estimasi harga otomatis.  
- **Dapat ditingkatkan** seiring pertambahan data dan kebutuhan bisnis baru.  
- **Memberikan blueprint TDSP** bagi proyek data science berikutnya.

---

Terima kasih kepada teman-teman saya: Kirana, Adrian, dan Satrio yang telah membuat proyek ini sangat bermanfaat untuk tujuan pembelajaran saya dalam regresi ML! Anda dapat merujuk ke sumber aslinya di sini: https://github.com/PurwadhikaDev/BetaGroup\_JC\_DS\_FT\_BSD\_26\_FinalProject


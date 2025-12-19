# Used Cars Price Prediction – Saudi Arabia
---
arabian-cars-1/
│
├── Dataset/
│   ├── UsedCarsSA_Unclean_Ar.xlsx        # Dataset mentah (Bahasa Arab)
│   ├── UsedCarsSA_Unclean_EN.csv         # Dataset mentah (terjemahan Inggris)
│   ├── UsedCarsSA_Clean.csv              # Dataset bersih (versi final)
│   └── UsedCarsSA_Clean_EN.csv           # Dataset bersih (English version)
│
├── Environment/
│   └── environment.yml                   # Environment Conda/Mamba untuk reproduktibilitas
│
├── Model/
│   └── xgb_tuned_mae11198_20251218.joblib
│       # Model XGBoost terbaik hasil tuning (MAE ≈ 11,198)
│
├── Notebook/
│   ├── 01_Business Understanding.ipynb
│   ├── 02_Data Acquisition And Understanding.ipynb
│   ├── 03_Modeling.ipynb
│   ├── 04_Deployment.ipynb
│   └── 05_Customer or Stakeholder Acceptance.ipynb
│
├── README.md                             # Dokumentasi utama proyek
├── lst.txt                               # Catatan/utility tambahan (opsional)
---
Proyek ini bertujuan membangun **model machine learning regresi** untuk memprediksi **harga wajar mobil bekas di Arab Saudi** menggunakan dataset *Saudi Arabia Used Cars* (±8.000 data) dari Kaggle. Model dirancang untuk membantu **penjual, pembeli, dan platform** dalam pengambilan keputusan harga yang objektif, dengan fitur utama seperti merek, tipe, tahun produksi, ukuran mesin, jarak tempuh, region, dan opsi kendaraan. Keberhasilan model diukur menggunakan **MAE dan MAPE**, dengan target akurasi yang relevan secara bisnis.

Data diproses melalui tahapan **EDA, pembersihan, imputasi, penanganan outlier (IQR), konversi tipe data, dan feature engineering** seperti *Car_Age* dan *Mileage_per_Year*. Proses modeling dilakukan secara end-to-end menggunakan **pipeline preprocessing** untuk mencegah data leakage, dengan evaluasi beberapa algoritma regresi. **XGBoost** terpilih sebagai model terbaik setelah **cross-validation dan hyperparameter tuning**, menghasilkan performa paling stabil dan akurat. **SHAP analysis** menunjukkan bahwa *Engine_Size, Year, Mileage,* dan *Car_Age* merupakan faktor dominan penentu harga.

Model akhir diimplementasikan dalam bentuk **pipeline terintegrasi** yang siap digunakan secara operasional, mampu menerima input kendaraan baru dan menghasilkan estimasi **harga wajar pasar** secara konsisten. Artefak model disimpan dan dapat digunakan untuk integrasi sistem maupun deployment lebih lanjut.

---

Terima kasih kepada teman-teman saya: Kirana, Adrian, dan Satrio yang telah membuat proyek ini sangat bermanfaat untuk tujuan pembelajaran saya dalam regresi ML! Anda dapat merujuk ke sumber aslinya di sini: https://github.com/PurwadhikaDev/BetaGroup_JC_DS_FT_BSD_26_FinalProject


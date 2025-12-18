# Used Cars Price Prediction – Saudi Arabia

## Executive Summary

Proyek ini bertujuan untuk membangun **model machine learning** yang mampu memprediksi **harga wajar mobil bekas di Arab Saudi** berdasarkan karakteristik kendaraan yang tercantum pada platform jual beli daring. Permasalahan utama yang diangkat adalah ketidakpastian dalam penentuan harga mobil bekas, yang dapat merugikan penjual, pembeli, maupun platform marketplace akibat harga yang terlalu tinggi atau terlalu rendah dibandingkan kondisi pasar.

Pendekatan proyek mengikuti kerangka **Team Data Science Process (TDSP)**, dimulai dari pemahaman masalah bisnis, eksplorasi dan pemrosesan data, pengembangan model, hingga kesiapan deployment. Dataset diperoleh dari Kaggle dan merepresentasikan listing mobil bekas dengan kombinasi fitur numerik dan kategorikal, seperti merek, tipe, tahun produksi, ukuran mesin, jarak tempuh, jenis transmisi, wilayah penjualan, serta harga kendaraan. Pada tahap awal dilakukan analisis kualitas data untuk mengidentifikasi missing values, inkonsistensi tipe data, duplikasi, dan outlier yang berpotensi memengaruhi performa model.

Pada tahap modeling, beberapa algoritma regresi dikembangkan dan dievaluasi menggunakan pipeline yang konsisten untuk preprocessing dan pelatihan model. Evaluasi performa difokuskan pada metrik yang relevan secara bisnis, terutama **Mean Absolute Error (MAE)** dan **Mean Absolute Percentage Error (MAPE)**, karena keduanya mudah diinterpretasikan oleh stakeholder non-teknis dan secara langsung merepresentasikan selisih harga prediksi terhadap harga aktual. Model terbaik dipilih berdasarkan keseimbangan antara akurasi, stabilitas performa pada data uji, dan kompleksitas model.

Model final kemudian disiapkan untuk tahap deployment dengan memastikan konsistensi struktur input dan preprocessing antara fase training dan inferensi. Pada tahap Customer / Stakeholder Acceptance, model divalidasi dari sisi nilai bisnis dengan mereferensikan performa yang telah dicapai pada fase modeling. Model dinilai mampu memberikan estimasi harga yang cukup akurat untuk digunakan sebagai **alat bantu pengambilan keputusan**, baik bagi penjual, pembeli, maupun platform marketplace.

Secara keseluruhan, proyek ini menghasilkan solusi prediktif yang **reproducible**, **berorientasi bisnis**, dan **siap dikembangkan lebih lanjut**, misalnya melalui integrasi ke dashboard analitik atau API. Proyek ini menunjukkan penerapan end-to-end data science workflow yang tidak hanya berfokus pada akurasi model, tetapi juga pada relevansi bisnis dan kesiapan implementasi di dunia nyata.

---

Terima kasih kepada teman-teman saya: Kirana, Adrian, dan Satrio yang telah membuat proyek ini sangat bermanfaat untuk tujuan pembelajaran saya dalam regresi ML! Anda dapat merujuk ke sumber aslinya di sini: https://github.com/PurwadhikaDev/BetaGroup_JC_DS_FT_BSD_26_FinalProject


# Diabetes Pipeline
- Nama : Aldi Akbar Alimi
- Username Dicoding: alldinosaur

| Menu | Deskripsi |
| ----------- | ----------- |
| Dataset | [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) |
| Masalah | Diabetes merupakan salah satu penyakit kronis yang disebabkan oleh tingginya kadar gula darah. Seringkali disebabkan oleh pola makan, mengkonsumsi makanan yang tidak sehat, dll. Meskipun tidak ada obat untuk diabetes, strategi seperti menurunkan berat badan, makan dengan sehat, dan menerima perawatan medis dapat mengurangi bahaya penyakit ini.|
| Solusi machine learning | Model machine learning yang dibangun ini dapat digunakan untuk mengukur resiko diabetes sesorang, sehingga diagnosa diabetes bisa dilakukan lebih dini. Karena diagnosa bisa dilakukan lebih dini, pasien bisa mengubah gaya hidup dan mendapat penanganan lebih cepat. |
| Metode pengolahan | Data yang digunakan pada dataset yaitu data numerik dengan jumlah 20 kolom yang semua datanya memiliki tipe data float. Metode yang digunakan untuk mengolah data tersebut yaitu dengan mengisi data yang kosong dengan data rata - rata serta melakukan normalisasikan data menjadi ukuran yang sama |
| Arsitektur model | Model yang dibuat menggunakan Dense layer dan juga Dropout layer sebagai hidden layer serta diantaranya terdapat satu layer input dan satu layer output. |
| Metrik evaluasi | Metrik yang digunakan pada model yaitu Metric yang digunakan pada model yaitu AUC, Precision, Recall, BinaryAccuracy, TruePositive, FalsePositive, TrueNegative, FalseNegative untuk mengevaluasi performa model sebuah klasifikasi dua kelas |
| Performa model | Model yang dibuat menghasilkan performa yang cukup baik dalam memberikan prediksi diabetes pada seseorang, dan dari proses training yang dilakukan, model menghasilkan binary_accuracy dan val_binary_accuracy sebesar 91%.  |
| Opsi Deployment | Proyek machine learning ini dideploy menggunakan salah satu platfrom deployment yaitu Railway yang menyediakan layanan gratis untuk mendeploy sebuah proyek di cloud server. |
| Web App | https://diabetes-pipeline.up.railway.app |
| Monitoring | Monitoring pada proyek ini menggunakan layanan open-source yaitu prometheus. Monitoring dapat dilihat dari setiap perubahan jumlah request yang dilakukan kepada sistem dan sistem akan menampilkan status dari setiap request yang diterima |

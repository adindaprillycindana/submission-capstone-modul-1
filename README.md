# 🛡️ Insurance Product CRUD Program

## 📌 Deskripsi
Program ini dibuat untuk membantu **karyawan produk asuransi** dalam menyimpan, mengelola, dan memantau data produk-produk asuransi beserta **track product details** (status, jumlah polis yang diterbitkan, dan detail lainnya).

Program ini berbasis **Python** dan berjalan di terminal/command line, dengan menu interaktif untuk melakukan operasi **CRUD** (*Create, Read, Update, Delete*) pada data produk.

---

## 🎯 Manfaat Program
- Menyimpan data produk asuransi secara terstruktur.
- Melacak informasi penting seperti status produk, jumlah polis yang diterbitkan, tarif, dan nilai pertanggungan.
- Memudahkan pencarian dan pengurutan data.
- Memungkinkan penambahan kolom baru sesuai kebutuhan.

---

## 📊 Struktur Data
Program menyimpan data dengan kolom sebagai berikut:

| No  | Kolom                       | Tipe Data   | Keterangan                              |
| --- | --------------------------- | ----------- | --------------------------------------- |
| 1   | **Product Code**            | String      | Nilai unik (tidak boleh duplikat)       |
| 2   | Product Name                | String      | Nama produk                             |
| 3   | Class of Business           | String      | Kelas bisnis                            |
| 4   | Customer Group              | String      | Grup pelanggan                          |
| 5   | Sum Insured (IDR)           | Integer     | > 0, nilai pertanggungan                 |
| 6   | Net Rate (%)                 | Float       | > 0, tarif bersih                        |
| 7   | Gross Rate (%)               | Float       | > 0, tarif kotor                         |
| 8   | Reinsurance Treaty           | String      | Perjanjian reasuransi                    |
| 9   | Status                       | String      | Status produk (aktif/tidak aktif/dll.)   |
| 10  | Number of Policies Issued    | Integer     | >= 0, jumlah polis yang diterbitkan      |

---

## 📜 Fitur Program

### 1. **Main Menu**
1. **Display Data**  
2. **Add Data Baru**  
3. **Update Data**  
4. **Delete Data**  
5. **Exit Program**  

---

### 2. **Display Data Menu**
- Menampilkan seluruh data.  
  *(Fitur lanjutan: dapat mengurutkan (ASC/DESC) berdasarkan kolom yang diinput user)*  
- Menampilkan sebagian data berdasarkan kolom yang diinput user.  
- Kembali ke Main Menu.

---

### 3. **Create Data Menu**
- Menambah produk baru.  
- Menambah kolom baru.  
- Kembali ke Main Menu.

---

### 4. **Update Data Menu**
- Mengedit data berdasarkan nama kolom.  
- Kembali ke Main Menu.

---

### 5. **Delete Data Menu**
- Menghapus data berdasarkan **Product Code** (nilai unik).  
- Kembali ke Main Menu.

---
   git clone https://github.com/username/repository-name.git
   cd repository-name

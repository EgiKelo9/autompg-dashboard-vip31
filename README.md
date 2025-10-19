# Auto MPG Dashboard

Dashboard interaktif untuk visualisasi dan analisis dataset Auto MPG dari UCI Machine Learning Repository menggunakan Panel dan HvPlot.

## 📊 Fitur

- **Interactive Filters**: Filter data berdasarkan origin (All, USA, Europe, Japan), model year range, dan cylinders range
- **Real-time Indicators**: Menampilkan Total Cars, Average MPG, Average Horsepower, dan Average Weight
- **Visualisasi Data**:
  - MPG Distribution (Histogram)
  - Average MPG by Cylinders (Bar Chart)
  - Weight vs MPG (Scatter Plot)
  - Average MPG per Year (Line Chart)
- **Data Table**: Tabel interaktif dengan pagination untuk melihat data detail

## 🛠️ Teknologi

- **Panel**: Framework untuk membuat dashboard interaktif
- **HvPlot**: Library untuk visualisasi data yang terintegrasi dengan Pandas
- **Pandas**: Library untuk manipulasi dan analisis data
- **Bokeh**: Backend untuk visualisasi interaktif
- **HoloViews**: Library untuk visualisasi data deklaratif
- **Scikit-learn**: Library untuk machine learning (data preprocessing)
- **ucimlrepo**: Library untuk mengakses dataset dari UCI ML Repository

## 📦 Installation

1. Clone repository ini:
```bash
git clone <repository-url>
cd tugas-7-dashboard
```

2. Buat virtual environment:
```bash
python -m venv .venv
```

3. Aktifkan virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Jalankan dashboard dengan perintah:

```bash
panel serve src/app.py --show
```

Dashboard akan terbuka di browser pada `http://localhost:5006/app`

Atau jalankan dengan auto-reload untuk development:

```bash
panel serve src/app.py --show --autoreload
```

## 📁 Struktur Project

```
tugas-7-dashboard/
├── src/
│   ├── app.py          # Main dashboard application
│   └── dataset.py      # Data loading and cleaning
├── .venv/              # Virtual environment
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 📊 Dataset

Dataset yang digunakan adalah **Auto MPG** dari UCI Machine Learning Repository:
- **ID**: 9
- **Total Records**: 398 (setelah cleaning)
- **Features**: displacement, cylinders, horsepower, weight, acceleration, model_year, origin
- **Target**: mpg (miles per gallon)

### Data Cleaning

1. Menghapus missing values pada kolom `horsepower`
2. Menghapus kolom `car_name` (ID)
3. Konversi tipe data integer untuk kolom `cylinders`, `model_year`, dan `origin`

## 🎨 Customization

### Mengubah Accent Color

Edit variabel `ACCENT` di `src/app.py`:
```python
ACCENT = "teal"  # Ubah ke warna lain: "blue", "red", "green", dll
```

### Mengubah Font

Custom CSS untuk font sudah menggunakan **Poppins** dari Google Fonts. Untuk mengubah font, edit bagian `pn.extension()` di `src/app.py`.

## 📝 Requirements

```
panel==1.5.4
hvplot==0.11.1
pandas==2.2.3
scikit-learn==1.5.2
ucimlrepo==0.0.7
bokeh==3.6.2
holoviews==1.19.1
param==2.1.1
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**SEMESTER 5 (MSIB) - Tugas 7**

## 🔗 Links

- [Panel Documentation](https://panel.holoviz.org/)
- [HvPlot Documentation](https://hvplot.holoviz.org/)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [Auto MPG Dataset](https://archive.ics.uci.edu/ml/datasets/auto+mpg)
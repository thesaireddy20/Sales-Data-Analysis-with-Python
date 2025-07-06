# 🛒 Sales Data Analysis — Setup Guide

This document will guide you through setting up the **Sales Data Analysis** project on your local machine. The project helps analyze customer spending behavior using Python and a sales dataset.

---

## 📁 Project Structure

```
sales-data-analysis/
│
├── sales_analysis.py        # Main Python script
├── sales_data(1).csv        # Dataset file (update path if needed)
├── docs/
│   └── setup.md             # This setup guide
├── README.md                # Project description
└── requirements.txt         # Optional: list of dependencies
```

---

## 🧰 Prerequisites

Ensure you have **Python 3.7+** installed. You’ll also need the following Python packages:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`

---

## 💾 Step-by-Step Setup

### 1. 🔽 Clone the Repository

```bash
git clone https://github.com/thesaireddy20/Sales-Data-Analysis-with-Python.git
cd Sales-Data-Analysis-with-Python
```

### 2. 📦 Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. 📥 Install Required Packages

You can install required packages manually or using `requirements.txt` if provided:

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. 📁 Place the Dataset

Make sure your CSV file `sales_data(1).csv` is placed in the correct path.
Update the file path in the script if needed:

```python
df = pd.read_csv('C:/Users/Shashi Reddy/OneDrive/Desktop/pyspiders/python_libraries/sales_data(1).csv', encoding='ISO-8859-1')
```

🛠 Tip: You can move the CSV into the project folder and update it like:

```python
df = pd.read_csv('sales_data(1).csv', encoding='ISO-8859-1')
```

---

## ▶️ Run the Script

Simply run the script using:

```bash
python sales_analysis.py
```

You’ll see multiple visualizations showing trends in spending based on:

* Gender
* Age Group
* State
* Occupation
* Product Category
* Marital Status

---

## 📌 Notes

* The script uses **seaborn bar plots** with `bar_label()` to show counts.
* All null values and unwanted columns are removed during preprocessing.
* Gender and marital status are converted to readable categories.

---

## ❓ Troubleshooting

* **Encoding error?** Make sure to use `encoding='ISO-8859-1'` when reading the CSV.
* **File not found?** Double-check the path to your CSV file.
* **No graph displayed?** Ensure `matplotlib.pyplot.show()` is called at the end of each plot.

---

## 📬 Questions or Contributions?

Feel free to [open an issue](https://github.com/thesaireddy20) or create a pull request if you'd like to contribute!


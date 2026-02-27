# 📂 Smart CSV Splitter – Clean Edition

A powerful and optimized CSV/Excel file splitter designed to handle both small and very large files efficiently.

Automatically detects large files and processes them in chunks to avoid memory issues.

---

## 🚀 Features

- ✅ Split by number of output files
- ✅ Split by number of rows per file
- ✅ Supports CSV, XLS, XLSX
- ✅ Automatic large file handling (500MB+)
- ✅ Chunk processing for huge CSV files
- ✅ Automatic output folder creation
- ✅ Logging system for error tracking
- ✅ Clean terminal interface + file picker
- ✅ Fully offline

---

## 📦 Requirements

- Python 3.8+
- pandas
- openpyxl (for Excel support)

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

```bash
python smart_csv_splitter.py
```

---

## 📝 How It Works

1. Select a CSV or Excel file.
2. Choose split method:
   - Option 1 → Split into number of files
   - Option 2 → Split by number of lines
3. Enter the required value.
4. Files are generated automatically.

---

## 📂 Output

A new folder will be created automatically:

```
<inputfilename>_split/
```

Inside this folder:

```
filename_part_1.csv
filename_part_2.csv
filename_part_3.csv
...
```

---

## 🧠 Large File Handling

- Files larger than 500MB are processed in chunks.
- Prevents memory overload.
- Optimized for high-volume datasets.

---

## 📄 Log File

A log file is generated:

```
smart_csv_splitter.log
```

Contains:
- Processing information
- Errors (if any)
- Split confirmations

---

## 💡 Use Cases

- Splitting large export files
- Preparing data for upload limits
- Batch processing
- Managing massive datasets
- Data distribution across systems

---

## 🛡️ Privacy

Runs completely offline.  
No data is sent externally.

---

## 📜 License

MIT License

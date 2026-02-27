"""
SmartCSVSplitter.py
Clean & Optimized CSV/Excel File Splitter
"""

import os
import math
import logging
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# ======================================================
# Configuration
# ======================================================

LOG_FILE = "smart_csv_splitter.log"
LARGE_FILE_THRESHOLD = 500 * 1024 * 1024  # 500MB

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ======================================================
# Utility Functions
# ======================================================

def print_banner():
    print("""
    ==========================================
              Smart CSV Splitter
              Clean Edition
    ==========================================
    """)


def create_output_folder(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = os.path.join(os.path.dirname(file_path), f"{base_name}_split")
    os.makedirs(output_folder, exist_ok=True)
    return base_name, output_folder


def read_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type.")


# ======================================================
# Splitting Functions
# ======================================================

def split_by_number_of_files(df, num_files, base_name, output_folder):
    chunk_size = math.ceil(len(df) / num_files)

    for i in range(num_files):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        chunk = df.iloc[start:end]

        if chunk.empty:
            break

        filename = os.path.join(output_folder, f"{base_name}_part_{i+1}.csv")
        chunk.to_csv(filename, index=False)
        print(f"Saved: {filename}")

    logging.info(f"Split into {num_files} files successfully.")


def split_by_lines(df, lines_per_file, base_name, output_folder):
    total_parts = math.ceil(len(df) / lines_per_file)

    for i in range(total_parts):
        start = i * lines_per_file
        end = (i + 1) * lines_per_file
        chunk = df.iloc[start:end]

        filename = os.path.join(output_folder, f"{base_name}_part_{i+1}.csv")
        chunk.to_csv(filename, index=False)
        print(f"Saved part {i+1}/{total_parts}: {filename}")

    logging.info(f"Split into chunks of {lines_per_file} lines successfully.")


def split_large_csv(file_path, lines_per_file, base_name, output_folder):
    print("Processing large file in chunks...")

    chunk_iter = pd.read_csv(file_path, chunksize=lines_per_file, low_memory=False)

    for i, chunk in enumerate(chunk_iter, start=1):
        filename = os.path.join(output_folder, f"{base_name}_part_{i}.csv")
        chunk.to_csv(filename, index=False)
        print(f"Saved: {filename}")

    logging.info("Large CSV split successfully.")


# ======================================================
# Main Split Logic
# ======================================================

def process_file(file_path, option, value):
    base_name, output_folder = create_output_folder(file_path)
    file_size = os.path.getsize(file_path)

    try:
        if option == 1:  # Split into number of files
            if file_path.endswith(".csv") and file_size > LARGE_FILE_THRESHOLD:
                # Count rows for large file
                total_rows = sum(1 for _ in open(file_path, encoding="utf-8", errors="ignore")) - 1
                lines_per_file = math.ceil(total_rows / value)
                split_large_csv(file_path, lines_per_file, base_name, output_folder)
            else:
                df = read_file(file_path)
                split_by_number_of_files(df, value, base_name, output_folder)

        elif option == 2:  # Split by lines
            if file_path.endswith(".csv") and file_size > LARGE_FILE_THRESHOLD:
                split_large_csv(file_path, value, base_name, output_folder)
            else:
                df = read_file(file_path)
                split_by_lines(df, value, base_name, output_folder)

        else:
            print("Invalid option selected.")
            return

        print(f"\n✅ Files saved in: {output_folder}")

    except Exception as e:
        logging.error(f"Error processing file: {e}")
        print(f"Error: {e}")


# ======================================================
# CLI + File Dialog
# ======================================================

def main():
    print_banner()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select CSV or Excel file")
    if not file_path:
        print("No file selected. Exiting...")
        return

    print("\nChoose split option:")
    print("1 → Split into number of files")
    print("2 → Split by number of lines")

    try:
        option = int(input("Enter option (1 or 2): ").strip())
        value = int(input("Enter value: ").strip())

        if option not in [1, 2] or value <= 0:
            print("Invalid input.")
            return

    except ValueError:
        print("Invalid numeric input.")
        return

    process_file(file_path, option, value)


# ======================================================

if __name__ == "__main__":
    main()

from tkinter import filedialog
import tkinter as tk

def load_file():
    password = []

    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename()

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if "PASS:" in line:
                parts = line.split("PASS:", 1)
                if len(parts) > 1:
                    content = parts[1].strip()
                    password.append(content)

    return password
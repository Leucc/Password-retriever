from tkinter import filedialog
import tkinter as tk

def load_file():
    password = []

    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename()

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            password.append(line)

    print(password)

if __name__ == '__main__':
    load_file()
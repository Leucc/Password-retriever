from tkinter import filedialog
import tkinter as tk

def load_file():
    global filename
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

def load_full_password():
    """
    从全局变量 filename 指定的文件中加载内容到列表。

    :return: 包含文件每一行内容的列表，去掉空行和多余空格。
    """
    password = []
    try:
        # 确保文件能够被正确打开
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                # 去掉前后空白并跳过空行
                stripped_line = line.strip()
                if stripped_line:  # 跳过空行
                    password.append(stripped_line)
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 未找到！")
    except IOError as e:
        print(f"错误：无法读取文件 '{filename}'，错误详情: {e}")

    return password
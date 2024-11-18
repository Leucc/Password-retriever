import datetime

def save_password(data, data2):
    """
    保存密码到文件中，支持字符串和列表。
    """
    import datetime
    today = datetime.datetime.now()
    formatted_time = today.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{formatted_time}_password.txt"

    try:
        # 确保 data 是列表
        if isinstance(data, str):
            data = [data]
        if isinstance(data2, str):
            data2 = [data2]

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines("出现次数多的密码: \n")

        # 写入第一个数据集
        with open(filename, 'a', encoding='utf-8') as f:
            for key, value in data:
                f.write(f"{key}: {value}\n")

        with open(filename, 'a', encoding='utf-8') as f:
            f.writelines("\nGoogle常用密码: \n")
            f.writelines("\n")

        # 追加写入第二个数据集
        with open(filename, 'a', encoding='utf-8') as f:
            for item in set(data2):
                f.write(f"{item}\n")

        print(f"Password saved successfully in {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
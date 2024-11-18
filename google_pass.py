from collections import Counter

def most_popular(password):
    count_dict = Counter(password)
    # 按出现次数排序
    sorted_counts = count_dict.most_common()

    # 返回排序后的统计结果（列表形式）
    return [(key, value) for key, value in sorted_counts]

def accounts_password(data):
    """
    从列表数据中提取所有与目标 URL 匹配的密码。

    :param data: 包含多个记录的列表
    :param target_url: 要匹配的目标 URL（例如 'accounts.google.com'）
    :return: 包含所有匹配密码的列表
    """
    passwords = []  # 用于存储匹配的密码

    target_url = "accounts.google.com"

    for i in range(len(data)):
        if data[i].startswith("URL:") and target_url in data[i]:
            # 检查是否有 'PASS:' 行
            if i + 2 < len(data) and data[i + 2].startswith("PASS:"):
                password = data[i + 2].split("PASS:", 1)[1].strip()
                passwords.append(password)

    return passwords


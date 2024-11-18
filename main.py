from file_diglog import load_file
from save_password import save_password
from unique_password import filter_password


def main():
    # 读取密码
    password = load_file()
    # 过滤重复的密码
    result = filter_password(password)
    # 保存密码
    save_password(result)


if __name__ == '__main__':
    main()
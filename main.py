import file_diglog
import google_pass
from file_diglog import load_file
from save_password import save_password

def main():
    # 读取密码
    password = load_file()
    # 完整数据
    full_data = file_diglog.load_full_password()
    # 过滤重复的密码
    # filtered = filter_password(password)
    # 出现最多的密码
    most_exist = google_pass.most_popular(password)
    # google accounts的密码
    accounts_password_google = google_pass.accounts_password(full_data)
    # 保存密码
    save_password(most_exist, accounts_password_google)


if __name__ == '__main__':
    main()
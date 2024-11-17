import datetime

def save_password(data):
    today = datetime.datetime.now()
    formatted_time = today.strftime("%Y-%m-%d %H:%M:%S")

    with open(f"{formatted_time}_password.txt",'w', encoding='utf-8') as f:
        for i in range(len(data)):
            f.write(str(f"{data[i]}\n"))
    print("Password saved")
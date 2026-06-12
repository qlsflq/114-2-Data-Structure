users = {}

while True:
    choice = input("請選擇操作選項 (a 註冊, b 登入, c 退出) ? ")

    if choice == "a":
        account = input("\n請輸入帳號 : ")

        if account in users:
            print("帳號已存在，請重新輸入!\n")
            continue

        password = input("請輸入密碼 : ")
        users[account] = password
        print("註冊成功!\n")

    elif choice == "b":
        account = input("\n請輸入帳號 : ")

        if account not in users:
            print("帳號不存在，無法登入!\n")
            continue

        password = input("請輸入密碼 : ")

        if users[account] == password:
            print("登入成功!\n")
        else:
            print("密碼錯誤，無法登入!\n")

    elif choice == "c":
        print("系統已退出")
        break

    else:
        print("選項錯誤，請重新輸入!\n")
frist = input("是否创建新的用户？Y/N:")
i = 0
users = {}
def user_sys():
    while True:
        i += 1
        users['user_name',i] = user_name
        print(users)
        break
if frist == "Y":
    user_name = input("请输入用户名:")
    user_sys()
elif frist == "N":
    print("再见。")
else:
    print("请输入Y或者N。")

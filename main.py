from else_sys import else_sys
frist = input("是否创建新的用户？Y/N:")
i = 0
users = {}
if frist == "Y":
    user_name = input("请输入用户名:")
    user_code = input("请输入密码：")
    while True:
        i += 1
        users[user_name,i] = user_code
        break
    nest_q = input("你是否要新建一个记账档案？Y/N")
    if nest_q == Y:
        #如果是的话
        
elif frist == "N":
    print("再见。")
else:
    print("请输入Y或者N。")
    else_sys()

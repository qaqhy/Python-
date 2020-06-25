# 根据你身上带的钱，来决定你今天中午能吃什么。
money = int(input("请输入你带的钱："))
if money < 1:  # 如果money小于1，就说明你没有带钱
    print("你的钱不够")
elif (money >= 1) and (money <= 5):  # 判断money是否在1到5之间
    print("你可以吃包子")
elif (money > 5) and (money <= 10):  # 判断money是否在6到10之间
    print("你可以吃面条")
else:
    print("你可以吃大餐")
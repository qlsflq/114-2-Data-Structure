from collections import deque

# 測試資料，可依題目提供的 orders 替換
orders = [
    {"name": "劍士", "cost": 70},
    {"name": "弓手", "cost": 30},
    {"name": "騎士", "cost": 50},
    {},{},{},{},
    {"name": "法師", "cost": 80},
    {"name": "槍兵", "cost": 40},
    {"name": "巨人", "cost": 999}
]

player_gold = 200

queue_a = deque()
queue_b = deque()

MAX_QUEUE_SIZE = 2

for round_num, order in enumerate(orders):
    print(f"--- 第 {round_num} 回合 ---")

    # Dequeue：每當偶數回合，系統自動觸發雙廠 Dequeue
    if round_num % 2 == 0:
        if len(queue_a) > 0:
            unit = queue_a.popleft()
            print(f"A 廠生產完成：{unit} 出列！")
        else:
            print("A 廠沒東西可做 (Underflow 防護成功)")

        if len(queue_b) > 0:
            unit = queue_b.popleft()
            print(f"B 廠生產完成：{unit} 出列！")
        else:
            print("B 廠沒東西可做 (Underflow 防護成功)")

    # 允許空單 {} 存在
    if order == {}:
        print("玩家本回合無動作，單純推進時間")
        print(f"A: {list(queue_a)} | B: {list(queue_b)}")
        print()
        continue

    unit_name = order["name"]
    cost = order["cost"]

    # 資源檢核
    if player_gold < cost:
        print(f"黃金不足，無法生產 {unit_name}")
        print(f"A: {list(queue_a)} | B: {list(queue_b)}")
        print()
        continue

    # Overflow 防禦
    if len(queue_a) >= MAX_QUEUE_SIZE and len(queue_b) >= MAX_QUEUE_SIZE:
        print(f"產線全滿！{unit_name} 訂單拒絕")
        print(f"A: {list(queue_a)} | B: {list(queue_b)}")
        print()
        continue

    # 負載平衡：放進排隊人數較少的 Queue，一樣長優先放 A
    if len(queue_a) <= len(queue_b):
        if len(queue_a) < MAX_QUEUE_SIZE:
            queue_a.append(unit_name)
            player_gold -= cost
            print(f"{unit_name} 分派至 A 廠 (剩餘黃金: {player_gold})")
        else:
            queue_b.append(unit_name)
            player_gold -= cost
            print(f"{unit_name} 分派至 B 廠 (剩餘黃金: {player_gold})")
    else:
        if len(queue_b) < MAX_QUEUE_SIZE:
            queue_b.append(unit_name)
            player_gold -= cost
            print(f"{unit_name} 分派至 B 廠 (剩餘黃金: {player_gold})")
        else:
            queue_a.append(unit_name)
            player_gold -= cost
            print(f"{unit_name} 分派至 A 廠 (剩餘黃金: {player_gold})")

    print(f"A: {list(queue_a)} | B: {list(queue_b)}")
    print()
import time
from collections import deque

# --- 作業準備：建立 30 萬筆排隊資料 ---
print("正在建立 30 萬人的排隊系統，請稍候...")
queue_size = 300000
python_list_queue = list(range(queue_size))
linked_list_queue = deque(range(queue_size))
print("系統建立完畢！\n" + "-"*30)

# ==========================================
# 測試 4：VIP 頭部插隊 (平移地獄 vs. 指標牽手)
# ==========================================
print("【測試 1：1000 位 VIP 進入隊伍最前面】")
insert_count = 1000

# 4-1. Python List (Array) 的頭部插隊
start_time = time.time()

for i in range(insert_count):
    # TODO 4-1: 請使用 .insert() 方法，將字串 "VIP" 插入到 python_list_queue 的最前面 (index 0)
    python_list_queue.insert(0, "VIP")

end_time = time.time()
print(f"Python List (O(N) 平移) 耗時: {end_time - start_time:.5f} 秒")

# 4-2. Deque (Linked List) 的頭部插隊
start_time = time.time()

for i in range(insert_count):
    # TODO 4-2: 請使用 deque 專屬的頭部方法，將字串 "VIP" 放入 linked_list_queue 最前面
    linked_list_queue.appendleft("VIP")

end_time = time.time()
print(f"Deque (O(1) 瞬間牽手) 耗時: {end_time - start_time:.5f} 秒")
print("-"  * 30)

# ==========================================
# 測試 5：行銷部抽獎 (Random Access 隨機存取)
# ==========================================
print("【測試 2：行銷部隨機查詢第 15 萬號排隊者 1000 次】")
target_index = 150000
query_count = 1000

# 5-1. Python List 找特定位置
start_time = time.time()

for _ in range(query_count):
    # TODO 5-1: 請直接用中括號 [] 取出 python_list_queue 第 target_index 個位置的資料，存入變數 lucky_guy
    lucky_guy = python_list_queue[target_index]

end_time = time.time()
print(f"Python List (O(1)) 耗時: {end_time - start_time:.5f} 秒")

# 5-2. Deque 找特定位置
start_time = time.time()

for _ in range(query_count):
    # TODO 5-2: 請直接用中括號 [] 取出 linked_list_queue 第 target_index 個位置的資料，存入變數 lucky_guy
    lucky_guy = linked_list_queue[target_index]

end_time = time.time()
print(f"Deque (O(N) 從頭慢慢找) 耗時: {end_time - start_time:.5f} 秒")

# 6. 最後用註解解釋以下

# 6-1.
# 4-1 和 4-2 差很多，是因為 Python List 底層比較像 Array，也就是連續記憶體空間。
# 當使用 python_list_queue.insert(0, "VIP") 在最前面插入資料時，
# 原本所有元素都必須往後平移一格，資料越多，搬移成本越高。
# 所以 List 頭部插入的時間複雜度是 O(N)。
#
# Deque 則是雙端佇列，適合在頭尾兩端新增或刪除資料。
# 使用 linked_list_queue.appendleft("VIP") 時，不需要把全部資料平移，
# 只需要調整頭部位置或連結關係，因此頭部插入通常是 O(1)。
# 所以在「VIP 從隊伍最前面插隊」這種情境下，deque 會明顯比 list 快。

# 6-2.
# 5-1 和 5-2 差很多，是因為 Python List 支援 Random Access 隨機存取。
# List 的資料放在連續記憶體中，所以 python_list_queue[target_index]
# 可以直接透過 index 計算位置，馬上找到第 target_index 個元素。
# 因此 List 的索引查詢時間複雜度是 O(1)。
#
# Deque 雖然可以使用 linked_list_queue[target_index] 這種寫法，
# 但它不是為了中間位置的隨機存取設計的。
# 查詢中間元素時，deque 需要從某一端開始逐步尋找目標位置，
# 因此查詢中間資料的時間複雜度接近 O(N)。
# 所以在「隨機抽查第 15 萬號排隊者」這種情境下，list 會明顯比 deque 快。
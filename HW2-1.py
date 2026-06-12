import time
import numpy as np

# --- 作業準備：建立 500 萬筆測試資料 ---
print("正在產生 500 萬筆測試資料，請稍候...")
num_elements = 5000000
python_list = [1.5] * num_elements       # 傳統 Python List
numpy_array = np.array(python_list)      # 連續記憶體的 Numpy Array
print("資料產生完畢！\n" + "-"*30)

# ==========================================
# 測試 1：計算總和
# ==========================================
print("【測試 1：500萬筆資料加總計算】")

# 1-1. Python List 總和
start_time = time.time()

# TODO 1-1: 請使用 Python for loop 語法，計算 python_list 的總和，並存入 list_sum 變數
list_sum = 0
for number in python_list:
    list_sum += number

end_time = time.time()
print(f"Python List 加總耗時: {end_time - start_time:.5f} 秒")

# 1-2. Numpy Array 總和
start_time = time.time()

# TODO 1-2: 請使用 Numpy 的 .sum() 方法，計算 numpy_array 的總和，並存入 np_sum 變數
np_sum = numpy_array.sum()

end_time = time.time()
print(f"Numpy Array 加總耗時: {end_time - start_time:.5f} 秒")
print("-"  * 30)

# ==========================================
# 測試 2：新增資料 (彈性空間的代價)
# ==========================================
print("【測試 2：新增 100 萬筆新客戶資料】")
new_customers = [2.0] * 1000000

# 2-1. Python List 新增資料 (動態擴容)
start_time = time.time()

# TODO 2-1: 請使用 Python list 的 .append() 搭配 for loop，將 new_customers 加入 python_list 中
for customer in new_customers:
    python_list.append(customer)

end_time = time.time()
print(f"Python List 新增資料耗時: {end_time - start_time:.5f} 秒")

# 2-2. Numpy Array 新增資料 (強迫搬家)
start_time = time.time()

# TODO 2-2: Numpy 預設大小固定，無法直接 append。
#     - 請使用 np.append(舊陣列, 新資料) 來產生一個「全新」的陣列，並重新指派給 numpy_array 變數。
numpy_array = np.append(numpy_array, new_customers)

end_time = time.time()
print(f"Numpy Array 新增資料(強迫搬家)耗時: {end_time - start_time:.5f} 秒")

print("-" * 30)

# ==========================================
# 觀察與回答
# ==========================================

# 3-1:
# 在「加總計算」中，Numpy Array 通常會比 Python List 快很多。
# 原因是 Numpy 的 .sum() 底層主要用 C 語言實作，可以直接對連續記憶體做批次運算；
# Python for loop 則需要一筆一筆透過 Python 直譯器處理，所以額外成本較高。

# 3-2:
# 在「新增資料」中，Python List 通常會比 Numpy Array 有彈性。
# Python List 的 append() 支援動態擴容，平均時間複雜度接近 O(1)。
# 但 np.append() 不是真的在原陣列後面直接加資料，而是建立一個新的陣列，
# 再把舊資料與新資料複製過去，所以資料量大時成本較高。

# 3-3:
# 如果資料已經固定，且主要需求是大量數值運算，應該使用 Numpy Array。
# 如果資料會頻繁新增、刪除，Python List 會比較適合。
# 實務上常見做法是：先用 Python List 收集資料，等資料量穩定後，再轉成 Numpy Array 做大量運算。
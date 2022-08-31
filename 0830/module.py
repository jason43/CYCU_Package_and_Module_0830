import math

# 目標: 定義並呼叫函式
# 餐廳服務生，用顧客的姓名回傳歡迎詞的函數
def welcome_responed_by_waiter(customer_name=""):
    if customer_name:
        print(f"Welcome, {customer_name}!")
        return True
    else:
        print("Hi, Can you tell me your name, please!")
        return False

# 給定兩邊，計算第三邊，假定為直角且計算長邊
def calculate_triangle_third_edge(edge1, edge2, is_third_edge_long_edge=True):
    if is_third_edge_long_edge:
        long_edge = math.sqrt(edge1**2 + edge2**2)
        # print the result and limit the number of digits to the second decimal place 
        print(format(long_edge, ".2f"))
    else:
        short_edge = math.sqrt(abs(edge1**2 - edge2**2))
        # print the result and limit the number of digits to the second decimal place 
        print(format(short_edge, ".2f"))
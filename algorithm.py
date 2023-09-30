# 変数と演算子:
# 変数 x に整数値 5 を割り当て、変数 y に整数値 3 を割り当て、
# これらの変数を使用して x と y の和、差、積、および商を計算してください。

def result(num):
  x: int = 5
  y: int = 3
  
  if num == 0:
    return x + y
  elif num == 1:
    return x - y
  elif num == 2:
    return x * y
  elif num == 3:
    return x / y
  else:
    return "有効な数字を入力してください"

# 和: 0 差: 1 積: 2 商: 3
print("和: 0, 差: 1, 積: 2, 商: 3")
num = int(input("入力してください:"))
print(str(result(num)))
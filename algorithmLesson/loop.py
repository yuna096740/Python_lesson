import random

# リストとループ:
# 整数のリストを受け取り、そのリスト内のすべての要素の合計を計算するPython関数を作成してください。

array = [random.randint(0, 1000) for _ in range(1000000)] 

result: int = 0 
for i in array:
  result += i

print(array)
print(result)
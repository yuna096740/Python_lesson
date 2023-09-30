# 条件文:
# 整数値を入力として受け取り、その値が偶数か奇数かを判定するPythonプログラムを作成してください。

def judge(num):
  if num % 2 == 0:
    return "答えは偶数です"
  else:
    return "答えは奇数です"

print("値が偶数か奇数かを判定します")
num = int(input("数字を入力してください:"))
print(judge(num))
import math

# 関数:
# 2つの整数を引数として受け取り、それらの整数の最大公約数（GCD）を計算するPython関数を作成してください。

def fun(num1, num2):
  return math.gcd(num1, num2)

print("最大公約数を計算します")
num1 = int(input("1つ目の数字を入力してください:"))
num2 = int(input("2つ目の数字を入力してください:"))
print("最大公約数は" + str(fun(num1, num2)) + "です")
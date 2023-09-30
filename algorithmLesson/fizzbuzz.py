def fizzbuzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return num

print("FizzBuzzゲーム")
num: int = int(input("入力してください:"))
print("答えは" + str(fizzbuzz(num)) + "です")
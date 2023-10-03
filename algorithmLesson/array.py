# 1から100までの数字が格納された List の作成をして下さい。

list = [i + 1 for i in range(100)]
print(list)


# 次の連想配列(images)のheightだけを取得し、新しい配列(heights)を作成して下さい。
images = [
    {"Height": "20px", "Width": "40px"},
    {"Height": "34px", "Width": "56px"},
    {"Height": "28px", "Width": "64px"},
]

heights = [{"height": i["Height"]} for i in images]
print(heights)


# 次の連想配列(member)の中から名前(name)の値だけを抜き取った配列が返るような関数getNameを作成して下さい。
members = [
    {"Name": "松井", "Age": 39, "Gender": "male"},
    {"Name": "今田", "Age": 34, "Gender": "female"},
    {"Name": "鈴木", "Age": 24, "Gender": "male"},
    {"Name": "山田", "Age": 56, "Gender": "male"},
    {"Name": "田中", "Age": 89, "Gender": "female"},
]

getName = [i["Name"] for i in members]
print(getName)


# 以下の連想配列(users)の中から、管理者権限(admin)を持っている(true)ユーザーに絞り込み、filteredUsersという変数に格納して下さい。
users = [
    {"Id": 1, "Admin": True},
    {"Id": 2, "Admin": True},
    {"Id": 3, "Admin": False},
    {"Id": 4, "Admin": True},
    {"Id": 5, "Admin": False},
]
fillterUsers = [user for user in users if user["Admin"]]
print(fillterUsers)


# 次の多次元配列のインデックス0番目のみを取り出した配列を作成して下さい。
array = [
    ["Ruffy", "captain"],
    ["Zoro", "combatant"],
    ["Nami", "navigator"],
]

arrayIndex0 = [i[0] for i in array]
arrayIndex1 = [i[1] for i in array]
print(arrayIndex0)
print(arrayIndex1)

# 次の連想配列(member)の中から35歳以上の名前(name)の値だけを抜き取った配列が
# 返るような関数getNameOver35を作成して下さい。

members = [
    {"Name": "松井", "Age": 39, "Gender": "male"},
    {"Name": "今田", "Age": 34, "Gender": "female"},
    {"Name": "鈴木", "Age": 24, "Gender": "male"},
    {"Name": "山田", "Age": 56, "Gender": "male"},
    {"Name": "田中", "Age": 89, "Gender": "female"},
]

getNameOver35 = [member["Name"] for member in members if member["Age"] >= 35]
print(getNameOver35)
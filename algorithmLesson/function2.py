def get_cart_items(cart_items):
    if len(cart_items) == 0:
        return "カートに商品がない"
    else:
        return "カートに商品がある"

cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]

message = get_cart_items(cart_items)
cart_items = []

print('入力1:カートに商品がある場合')
print(message)

print('-----------------------------')

message = get_cart_items(cart_items)
print('入力1:カートに商品がない場合')
print(message)
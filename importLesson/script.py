import random
import tmp

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if tmp.validate(player_hand):
    computer_hand = random.randint(0, 2)
    
    if player_name == '':
        tmp.print_hand(player_hand)
    else:
        tmp.print_hand(player_hand, player_name)

    tmp.print_hand(computer_hand, 'コンピューター')
    
    result = tmp.judge(player_hand, computer_hand)

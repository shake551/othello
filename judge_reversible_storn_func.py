# direction
"""     7 0 1
         \|/
       6 -.-2
         /|\
        5 4 3
"""

"""
[[0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1]]でやる
"""


def judge_reversible_storn(direction, x, y, start_x, start_y, board, turn, count):
    # 0~7の数字で検索する方向を管理
    while True:
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
            y -= 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            x += 1
            y += 1
        elif direction == 4:
            y += 1
        elif direction == 5:
            x -= 1
            y += 1
        elif direction == 6:
            x -= 1
        elif direction == 7:
            x -= 1
            y -= 1
        else:
            print("out of range")

        # 検索途中に8*8のマスの外に出たら終わり
        if x < 1 or 8 < x:
            break
        elif y < 1 or 8 < y:
            break
        else:
            pass

        # 検索している地点がの石が反対の色なら1カウントする
        if board[y][x] == -turn:
            count += 1
        # それ以外なら終了
        else:
            break
    return count

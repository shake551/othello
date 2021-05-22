# direction
"""     7 0 1
         \|/
       6 -.-2
         /|\
        5 4 3
"""

import make_move_point


def judge_reversible_storn(direction, x, y, board, turn, count):
    # 0~7の数字で検索する方向を管理

    # 移動方向ごとに動く座標を二次元配列化
    move_point = make_move_point.make_move_point(0)
    while True:
        x += move_point[direction][0]
        y += move_point[direction][1]

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

import make_move_point


def reverse_storn_func(direction, start_x, start_y, board, turn, count):
    # 挟まれている石を裏返す
    change_storn_num = 0

    # 移動方向ごとに動く座標を二次元配列化(countごとに)
    move_point_count = make_move_point.make_move_point(count)

    # judge_reversible_stornでカウントした回数だけループし、その方向にある石を裏返す
    for j in range(count):
        # 移動方向ごとに動く座標を二次元配列化(jごとに)
        move_point_j = make_move_point.make_move_point(j)

        # +1や-1は付けないと想像通りに動かない
        """ex)j=0の時、石を置いたマスに対する処理になる。
        """
        if board[start_y + move_point_count[direction][1]][start_x + move_point_count[direction][0]] == turn:
            board[start_y + move_point_j[direction][1]
                  ][start_x + move_point_j[direction][0]] *= -1
            change_storn_num += 1

    if change_storn_num == 0:
        return False
    else:
        return True

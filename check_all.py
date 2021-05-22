import judge_reversible_storn_func
import make_move_point

judge_reversible_storn = judge_reversible_storn_func.judge_reversible_storn


def check_all_place(board, turn):

    # 石を返した回数
    change_storn_num = 0
    # check all place
    # 全ての座標を確認
    for i in range(1, 9):
        for j in range(1, 9):
            # except the place that already put storn
            # すでに置かれている座標は除く
            if board[j][i] == 0:
                x = i
                y = j
                for k in range(8):
                    count_num = 0
                    count = judge_reversible_storn(
                        k, x, y, board, turn, count_num)
                    if count == 0:
                        continue
                    else:
                        # 移動方向ごとに動く座標を二次元配列化(countごとに)
                        move_point_count = make_move_point.make_move_point(
                            count)

                    if board[j + move_point_count[k][1]][i + move_point_count[k][0]] == turn:
                        change_storn_num += 1

    if change_storn_num != 0:
        return True
    else:
        return False

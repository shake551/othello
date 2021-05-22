# 移動方向ごとに動く座標の二次元配列を生成
def make_move_point(flag):
    move_point = [[0, -1 - flag], [1 + flag, -1 - flag], [1 + flag, 0], [1 + flag, 1 + flag],
                  [0, 1 + flag], [-1 - flag, 1 + flag], [-1 - flag, 0], [-1 - flag, -1 - flag]]
    return move_point

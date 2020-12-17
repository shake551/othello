def reverse_storn_func(direction, start_x, start_y, board, turn, count):
    #挟まれている石を裏返す
    change_storn_num = 0
    #judge_reversible_stornでカウントした回数だけループし、その方向にある石を裏返す
    for j in range(count):
        #+1や-1は付けないと想像通りに動かない
        """ex)j=0の時、石を置いたマスに対する処理になる。
        """
        if direction == 0:
            if board[start_y - count - 1][start_x] == turn:
                board[start_y - j - 1][start_x] *= -1
                change_storn_num += 1
        elif direction == 1:
            if board[start_y - count - 1][start_x + count + 1] == turn:
                board[start_y - j - 1][start_x + j + 1] *= -1
                change_storn_num += 1
        elif direction == 2:
            if board[start_y][start_x + count + 1] == turn:
                board[start_y][start_x + j + 1] *= -1
                change_storn_num += 1
        elif direction == 3:
            if board[start_y + count + 1][start_x + count + 1] == turn:
                board[start_y + j + 1][start_x + j + 1] *= -1
                change_storn_num += 1
        elif direction == 4:
            if board[start_y + count + 1][start_x] == turn:
                board[start_y + j + 1][start_x] *= -1
                change_storn_num += 1
        elif direction == 5:
            if board[start_y + count + 1][start_x - count - 1] == turn:
                board[start_y + j + 1][start_x - j - 1] *= -1
                change_storn_num += 1
        elif direction == 6:
            if board[start_y][start_x - count - 1] == turn:
                board[start_y][start_x - j - 1] *= -1
                change_storn_num += 1
        elif direction == 7:
            if board[start_y - count - 1][start_x - count- 1] == turn:
                board[start_y - j - 1][start_x - j - 1] *= -1
                change_storn_num += 1
    
    if change_storn_num == 0:
        return False
    else:
        return True
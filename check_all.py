import judge_reversible_storn_func

judge_reversible_storn = judge_reversible_storn_func.judge_reversible_storn

def check_all_place(board, turn):
    change_storn_num = 0
    #check all place
    for i in range(1, 9):
        for j in range(1, 9):
            #except the place that already put storn
            if board[j][i] == 0:
                x = i
                y = j
                for k in range(8):
                    count_num = 0
                    count = judge_reversible_storn(k, x, y, i, j, board, turn, count_num)
                    if count == 0:
                        continue

                    if k == 0:
                        if board[j - count - 1][i] == turn:
                            change_storn_num += 1
                    elif k == 1:
                        if board[j - count - 1][i + count + 1] == turn:
                            change_storn_num += 1
                    elif k == 2:
                        if board[j][i + count + 1] == turn:
                            change_storn_num += 1
                    elif k == 3:
                        if board[j + count + 1][i + count + 1] == turn:
                            change_storn_num += 1
                    elif k == 4:
                        if board[j + count + 1][i] == turn:
                            change_storn_num += 1
                    elif k == 5:
                        if board[j + count + 1][i - count - 1] == turn:
                            change_storn_num += 1
                    elif k == 6:
                        if board[j][i - count - 1] == turn:
                            change_storn_num += 1
                    elif k == 7:
                        if board[j - count - 1][i - count- 1] == turn:
                            change_storn_num += 1

    if change_storn_num != 0:
        return True
    else:
        return False
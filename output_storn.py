import put_storn

puts_storn = put_storn.PutsStorn()

def outputs_storn(board):
    for y in range(10):
        for x in range(10):
            if board[y][x] == 1:
                print("◎ ", end = '')
                #print('{:^3}'.format(puts_storn.board[y][x]), end = '')
            elif board[y][x] == -1:
                print("● ", end = '')
            elif board[y][x] == 0:
                print("□ ", end = '')
            else:
                print(board[y][x], end = '')
                print(' ', end = '')
        print()
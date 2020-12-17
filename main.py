import put_storn
import output_storn

puts_storn = put_storn.PutsStorn()
output_storn = output_storn.outputs_storn

START_BOARD = [[2,2,2,2,2,2,2,2,2,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,-1,1,0,0,0,2],
               [2,0,0,0,1,-1,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,2,2,2,2,2,2,2,2,2]]

output_storn(puts_storn.board)

while True:
    print('石を置く座標を入力してください')
    print('ex).x,y')
    if puts_storn.turn == 1:
        which = "black"
    elif puts_storn.turn == -1:
        which = "white"
    print(which + "のターン-->")
    x, y = map(int, input().split(","))

    judge = puts_storn.judge_place(x, y)
    if judge == True:
        puts_storn.reverse_storn(x, y)
        output_storn(puts_storn.board)
            
    elif judge == False:
        print("その位置に石は置けません")

    judge_end_or_continue = puts_storn.judge_end(puts_storn.board, puts_storn.turn)
    if judge_end_or_continue == False:
        black = 0
        white = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if puts_storn.board[j][i] == 1:
                    black += 1
                elif puts_storn.board[j][i] == -1:
                    white += 1
        if black > white:
            print('黒の勝利')
        elif black < white:
            print('白の勝利')
        print('end')
        break
    
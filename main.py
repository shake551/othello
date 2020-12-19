import put_storn
import output_storn
import make_csv

puts_storn = put_storn.PutsStorn()
output_storn = output_storn.outputs_storn

put_place = [["x", "y"]]

output_storn(puts_storn.board)

while True:
    print('石を置く座標を入力してください')
    print('ex).x,y')
    if puts_storn.turn == 1:
        which = "black"
    elif puts_storn.turn == -1:
        which = "white"
    print(which + "のターン-->")
    
    while True:
        try:
            x, y = map(int, input().split(","))
            temporary_place = [x, y]
            put_place.append(temporary_place)
            break
        except ValueError:
            print("指定された形で入力してください-->")

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
        print(put_place)
        make_csv.make_csv(put_place)
        break
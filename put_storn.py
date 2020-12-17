import judge_reversible_storn_func
import reverse_storn_func
import check_all

judge_reversible_storn = judge_reversible_storn_func.judge_reversible_storn
reverse_storn_func = reverse_storn_func.reverse_storn_func
check_all_place = check_all.check_all_place

class PutsStorn:
    def __init__(self):
        self.board = [[2,2,2,2,2,2,2,2,2,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,0,0,0,-1,1,0,0,0,2],
                      [2,0,0,0,1,-1,0,0,0,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,0,0,0,0,0,0,0,0,2],
                      [2,2,2,2,2,2,2,2,2,2]]
        #turn is 1 or -1
        self.turn = 1
        self.count = 0
        self.judge_change_storn = []
    
    def reverse_storn(self, x, y):
        #石を置いた位置を保存
        start_x = x
        start_y = y
        #全ての方向に対してjudge_reversible_stornを実行
        for i in range(8):
            count = judge_reversible_storn(i, x, y, start_x, start_y, self.board, self.turn, self.count)
            self.judge_change_storn.append(reverse_storn_func(i, start_x, start_y, self.board, self.turn, count))
            print(reverse_storn_func(i, start_x, start_y, self.board, self.turn, count))
            self.count = 0
        if any(self.judge_change_storn):
            print('OK')
            self.board[start_y][start_x] = self.turn
            self.turn *= -1
        else:
            print("その位置には石は置けません//")

    def judge_place(self, x, y):
        if x < 1 or 8 < x:
            return False
        elif y < 1 or 8 < y:
            return False
        elif self.board[y][x] != 0:
            return False
        else:
            return True

    def judge_end(self, board, turn):
        ans = check_all_place(self.board, self.turn)
        return ans
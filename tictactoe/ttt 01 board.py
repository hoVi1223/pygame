# ttt 01 board.py

#보드 출력 함수 : def prt_board(board)

def prn_board(board):
    for row in range(3):
        print("{}|{}|{}".format(board[row][0], board[row][1], board[row][2]))
        print("-"*5)

#보드 초기화
board = [['','',''],
         ['','',''],
         ['','','']]

#보드 출력
prn_board(board)
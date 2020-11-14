#ttt 02 input.py

#틱텍토 입력 받기

# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe
# tic tac toe

#보드 출력 함수 선언
def prn_board(tb):
    for row in range(3):
        print("{}|{}|{}".format(tb[row][0], tb[row][1], tb[row][2]))
        print("-"*5)

#변수 초기화
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#보드 출력
prn_board(board)

#입력 받기
for cut in range(9):
    while True:
        y, x = map(int, input("좌표 (y, x): ").split(","))
        #y, x에 돌을 놓을 수 있는지 확인 후 가능하면 break
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요,")

    board[y][x] = "X"
    prn_board(board)
#ttt 03 turn.py

#틱텍토 돌 별로 입력 받기

#보드 출력 함수
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-"*5)

#변수 초기화
turn = 'X'
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

#보드 출력
prn_board(board)

#9회 동안 입력하기
for cut in range(9):
    while True:
        y, x = map(int, input("y, x: ").split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")

    #좌표에 돌 놓기
    board[y][x] = turn
    prn_board(board)

    #돌 모양 바꾸기
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
#tictactoe.text

#틱ㅌㄴ텍토 게임

board = [
    ['','',''],
    ['','',''],
    ['','','']
]

b=[[1,2,3],[4,5,6],[7,8,9]]

#보드 출력하기

for row in range(3):
    print("{}|{}|{}".format(b[row][0], b[row][1], b[row][2]))
    print("-"*5)
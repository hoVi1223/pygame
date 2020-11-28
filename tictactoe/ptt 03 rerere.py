import pygame

pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 450
CELL_SIZE = 150
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#화면 설정
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("파이틱텍토")

#보드 데이터
TTTData = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
turn = 'X'

#돌 모양 설정하기
pygame.font.init()
turn_font = pygame.font.SysFont('', 100)
result_font = pygame.font.SysFont('', 70)
turn_x = turn_font.render('X', True, YELLOW)
turn_o = turn_font.render('O', True, YELLOW)
win_x = result_font.render('Winner X', True, WHITE)
win_o = result_font.render('Winner O', True, WHITE)


def draw_grid():
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            one_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 3)


def cell_to_board(m_pos):
    for x in range(3):
        if CELL_SIZE * x < m_pos[0] <= CELL_SIZE * x + CELL_SIZE:
            ct_col = x
    for y in range(3):
        if CELL_SIZE * y < m_pos[1] <= CELL_SIZE * y + CELL_SIZE:
            ct_row = y
    return ct_row, ct_col

#돌 모양 바꾸기
def change_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


#보드 그리기 함수
def print_mark(p_row, p_col):
    turn_mark_rect = turn_o.get_rect().size
    p_x = p_col * CELL_SIZE + CELL_SIZE // 2 - turn_mark_rect[0] // 2
    p_y = p_row * CELL_SIZE + CELL_SIZE // 2 - turn_mark_rect[1] // 2
    if turn == 'X':
        screen.blit(turn_x, (p_x, p_y))
    else:
        screen.blit(turn_o, (p_x, p_y))


def check_winner(cw_row, cw_col):
    global running
    winner = False
    if TTTData[cw_row][0] == TTTData[cw_row][1] == TTTData[cw_row][2] == turn:
        winner = True
    if TTTData[0][cw_col] == TTTData[1][cw_col] == TTTData[2][cw_col] == turn:
        winner = True
    if cw_row - cw_col == 0:
        if TTTData[0][0] == TTTData[1][1] == TTTData[2][2] == turn:
            winner = True
    if cw_row - cw_col == 0 or abs(cw_row - cw_col) == 2:
        if TTTData[0][2] == TTTData[1][1] == TTTData[2][0] == turn:
            winner = True
    if winner:
        print_winner()
        running = False


def reset_data():
    global TTTData, turn
    TTTData = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    turn = 'X'
    screen.fill(BLACK)
    pygame.display.update()


def print_winner():
    # 파이게임은 RGBA를 지원하지 않는다 Red, Green, Blue, Alpha(투명도)
    # 레이어를 하나 맘ㄴ들어서 이ㅈ미지 출력

    result_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    result_surface.set_alpha(200)
    result_surface.fill(BLACK)
    screen.blit(result_surface, (0, 0))

    win_rect = win_o.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    if turn == 'O':
        screen.blit(win_o, win_rect)
    else:
        screen.blit(win_x, win_rect)
    pygame.display.update()
    pygame.time.delay(2000)


    reset_data()
    py_main()

running = True


#게임 루프
def py_main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = cell_to_board(mouse_pos)
                if TTTData[row][col] == 0:
                    TTTData[row][col] = turn
                    print(TTTData)
                    print_mark(row, col)
                    check_winner(row, col)
                    change_turn()

        draw_grid()

        pygame.display.update()


    #파이 게임 종료
    pygame.quit()


py_main()

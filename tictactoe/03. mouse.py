#03 mouse

import pygame

pygame.init()

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WHITE = (255, 255, 255)

#화면
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

#게임 변수 설정
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE


#격자 그리기 draw_grid()
def draw_grid():
    for gy in range(ROW_COUNT):
        for gx in range(COL_COUNT):
            one_rect = pygame.Rect(gx*CELL_SIZE, gy*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 1)


#클릭할 셀의 좌효표를 보드라ㅡ이 닺화표로 변경
def cell_to_board(tm_pos):
    row = col = -1
    for y in range(3):
        if y * CELL_SIZE <= tm_pos[1] < y * CELL_SIZE + CELL_SIZE:
            row = y
    for x in range(3):
        if x * CELL_SIZE <= tm_pos[0] < x * CELL_SIZE + CELL_SIZE:
            col = x
    return row, col


#게임 루프 설정
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()

            r, c = cell_to_board(m_pos)
            print("행: {}, 열: {}".format(r, c))

            # 마우스 오른쪽 버튼 클릭하면 게임 종료하기
            if event.button == 3:
                running = False

    #사각형 그리기
    draw_grid()

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()

#파이게임 종료
pygame.quit()
#ptt 02 grid
#02. 격자 그리기

import pygame

pygame.init()

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WHITE = (255, 255, 255)

#파이게임 화면 초기화
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

#게임 변수 설정
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // 3
COL_COUNT = SCREEN_WIDTH // 3

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #사각형 그리기
    for y in range(3):
        for x in range(3):
            one_rect = (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 1)

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()
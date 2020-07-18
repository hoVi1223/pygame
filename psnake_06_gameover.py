# psnake_06_gameover.py

import pygame
import random

# 화면 초기화
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 색상
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)

# 셀
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 이동방향
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction = DOWN

# 점수
score = 0

# 글꼴 설정
score_font = pygame.font.SysFont("comicsans", 40)

# 뱀 좌표 리스트 만들기 (화면 중앙)
s_pos = (COL_COUNT // 2, ROW_COUNT // 2)
bodies = [s_pos]

# 먹이 생성 함수


# 먹이  10개 좌표 리스트


# 게임 루프


    # 키 입력 처리


    # 뱀 머리 추출하고 다음 방향으로 이동


    # 먹이 충돌 체크


    # 꼬리 지우기


    # 화면 초기화


    # 격자 그리기


    # 먹이 그리기


    # 뱀 그리기


    # 점수 출력


    # 화면 업데이트


# 게임 종료



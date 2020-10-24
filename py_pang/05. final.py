#05. final.py

#파이팡 게임 만들기
import pygame
import os

# 01. 파이 게임 초기화
# 02. 게임 환경 초기화
# 03. 캐릭터 이동
# 04. 무기 발사
# 05. 공 추가
# 06. 충돌 처리
# 07. 공 나누기
# 08. 메시지 출력

#파이 게임 초기화
pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!")

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #화면 업데이트
    pygame.display.update()

#파이 게임 종료
pygame.quit()
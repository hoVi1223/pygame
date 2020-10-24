# 05. final.py

# 01. 파이 게임 초기화
# 02. 게임 환경 초기화
# 03. 캐릭터 이동
# 04. 무기 발사
# 05. 공 추가
# 06. 충돌 처리
# 07. 공 나누기
# 08. 메시지 출력

# 파이팡 게임 만들기
import pygame
import os

# 파이 게임 초기화
pygame.init()

# FPS (Frame Per Second)
clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!")

# 이미지 불러오기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "images")

background_img = pygame.image.load(os.path.join(img_path, "background.png"))

stage_img = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_height = stage_img.get_rect().size[1]

character_img = pygame.image.load(os.path.join(img_path, "character.png"))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_pos_x = screen_width // 2 - character_width // 2
character_pos_y = screen_height - stage_height - character_height
character_speed = 0

# 게임 루프
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_speed -= 5
            elif event.key == pygame.K_RIGHT:
                character_speed += 5
        if event.type == pygame.KEYUP:
            character_speed = 0
    character_pos_x += character_speed

    if character_pos_x < 0: character_pos_x = 0
    if character_pos_x > screen_width - character_width:
        character_pos_x = screen_width - character_width

    # 화면 출력
    screen.blit(background_img, (0, 0))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_pos_x, character_pos_y))
    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
import pygame

pygame.init()

screen_width = 200
screen_height = 3000
# Создаем окно
screen = pygame.display.set_mode((screen_width, screen_height))
black_strip = pygame.Surface((screen_width, screen_height))
black_strip.fill((0, 0, 0))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Проверяем, находится ли курсор мыши над черной полоской
            if black_strip.get_rect().collidepoint(event.pos):
                pygame.mouse.set_visible(False)  # Скрываем указатель мыши
            else:
                pygame.mouse.set_visible(True)  # Показываем указатель мыши2
    # Отрисовка
    screen.fill((255, 255, 255))
    screen.blit(black_strip, (0, 0))
    pygame.display.flip()
pygame.quit()

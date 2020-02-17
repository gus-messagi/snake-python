import pygame, random
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def apple_xyrandom():
    x = random.randint(0, 630)
    y = random.randint(0, 470)
    return (x//10 * 10, y//10 * 10)

def pause(isPaused):
    return not isPaused

def apple_collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def self_snake_collission(body):
    for i in range(1, len(body) - 1):
        if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
            return True

def wall_collision(body, direction):
    if body[0][0] >= SCREEN_WIDTH and direction == 1:
        body[0] = (0, body[0][1])
    if body[0][0] <= -10 and direction == 3:
        body[0] = (640, body[0][1])
    if body[0][1] >= SCREEN_HEIGHT and direction == 2:
        body[0] = (body[0][0], 0)
    if body[0][1] <= -10 and direction == 0:
        body[0] = (body[0][0], 480)


def init_snake():
    return [((SCREEN_WIDTH / 2) + 10, (SCREEN_HEIGHT / 2)), ((SCREEN_WIDTH / 2) + 10, (SCREEN_HEIGHT / 2))]
    
def main():
    snake = init_snake()
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    isPaused = False

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((255, 255, 255))
    snake_direction = LEFT

    apple = apple_xyrandom()
    apple_skin = pygame.Surface((10, 10))
    apple_skin.fill((255, 0, 0))

    clock = pygame.time.Clock()

    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    isPaused = pause(isPaused)

                if not isPaused:
                    if event.key == K_UP:
                        if snake_direction != DOWN:
                            snake_direction = UP
                    if event.key == K_RIGHT:
                        if snake_direction != LEFT:
                            snake_direction = RIGHT
                    if event.key == K_DOWN:
                        if snake_direction != UP:
                            snake_direction = DOWN
                    if event.key == K_LEFT:
                        if snake_direction != RIGHT:
                            snake_direction = LEFT

        if not isPaused:
            
            for i in range(len(snake) -1, 0, -1):
                snake[i] = (snake[i-1][0], snake[i-1][1])

            if snake_direction == UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if snake_direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if snake_direction == RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if snake_direction == LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])

            if apple_collision(snake[0], apple):
                apple = apple_xyrandom()
                snake.append((0, 0))

            if self_snake_collission(snake):
                snake = init_snake()

            wall_collision(snake, snake_direction)

            screen.fill((0, 0, 0))
            screen.blit(apple_skin, apple)

            for pos in snake:
                screen.blit(snake_skin, pos)

            pygame.display.update()

if __name__ == '__main__' : main()
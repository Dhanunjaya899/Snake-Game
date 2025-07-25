import pygame
import random
import sys

pygame.init()

width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_x, snake_y = width/2, height/2
change_x, change_y = 0, 0

food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

clock = pygame.time.Clock()
snake_body = [(snake_x, snake_y)]

# Score
score = 0
font = pygame.font.SysFont(None, 35)
game_over_font = pygame.font.SysFont(None, 60)

def show_score():
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    game_screen.blit(score_surface, (10, 10))

def show_game_over():
    game_screen.fill((0, 0, 0))
    over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    game_screen.blit(over_text, (width//2 - over_text.get_width()//2, height//2 - 50))
    game_screen.blit(score_text, (width//2 - score_text.get_width()//2, height//2 + 10))
    pygame.display.update()
    pygame.time.delay(3000)  # Wait 3 seconds before quitting
    pygame.quit()
    sys.exit()

def display_snake():
    global snake_x, snake_y, food_x, food_y, score

    # Move snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check self collision
    if (snake_x, snake_y) in snake_body[1:]:
        show_game_over()

    snake_body.append((snake_x, snake_y))

    # Food collision
    if food_x == snake_x and food_y == snake_y:
        score += 1
        food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
    else:
        del snake_body[0]

    # Draw everything
    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for i, (x, y) in enumerate(snake_body):
        if i == len(snake_body) - 1:
            # Head (last segment in the list) as a circle
            pygame.draw.circle(game_screen, (255, 0, 0), (int(x) + 5, int(y) + 5), 5)
        else:
            # Body as rectangles
            pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    show_score()
    pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = 10

    display_snake()
    clock.tick(8)

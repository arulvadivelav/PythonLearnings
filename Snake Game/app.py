import pygame, random

pygame.init()

# Game window setting
window_width = 800
window_height = 600

# Game Display
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Snake starting point
x1 = window_width / 2
y1 = window_width / 2

# Food position
foodx = round(random.randrange(0, window_width - 10)/10) * 10
foody = round(random.randrange(0, window_height - 10)/10) * 10
        
# Points to know the snake movement
x1_change = 0
y1_change = 0

# Snake body
snake_body = []
length_of_snake = 1

white = (255, 255, 255) # Snake color
red = (255, 0, 0) # Food color
black = (0, 0, 0)


# Set frame rate to control the snake speed
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # Key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
    
    x1 = x1 + x1_change
    y1 = y1 + y1_change

    # Set bountry block for the snake
    if x1<0 or x1>window_width or y1<0 or y1>window_height:
        game_over = True

    window.fill(black)

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)

    # Changing the food position when the snake eat the food
    if x1 == foodx and y1 == foody:
        # Food position
        foodx = round(random.randrange(0, window_width - 10)/10) * 10
        foody = round(random.randrange(0, window_height - 10)/10) * 10
        length_of_snake += 1

    if len(snake_body)>length_of_snake:
        del snake_body[0]

    # If snake hit itself
    for segment in snake_body[:-1]:
        if snake_head == segment:
            game_over = True

    # Snake body
    # pygame.draw.rect(window, white, [x1, y1, 10, 10])
    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], 10, 10])

    # Food
    pygame.draw.rect(window, red, [foodx, foody, 10, 10])
    pygame.display.update()
    # Frame rate(Snake speed)
    clock.tick(30)
import pygame

# Screen dimensions
WIDTH = 800
HEIGHT = 640
FONT_SIZE = 36

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

font = pygame.font.Font(None, FONT_SIZE)

running = True

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Rect players
rect_x, rect_y, rect_w, rect_h = 20, int(HEIGHT / 2) - 50, 50, 100
rect2_x, rect2_y, rect2_w, rect2_h = WIDTH - 60, int(HEIGHT / 2) - 50, 50, 100

# Load images
player1_image = pygame.image.load('images/player1.png')
player2_image = pygame.image.load('images/player2.png')
table = pygame.image.load('images/table.png')

# Resize images to match paddle sizes
player1_image = pygame.transform.scale(player1_image, (rect_w, rect_h))
player2_image = pygame.transform.scale(player2_image, (rect2_w, rect2_h))

# Square gameplay area
paddle_speed = 0.5

play_area_left = 10
play_area_right = 790
play_area_top = 10
play_area_bottom = 550

# Ball variables
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_x_speed = 1
ball_y_speed = 1

# Player Score
player1_score = 0
player2_score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Controls player1
    if keys[pygame.K_w] and rect_y > play_area_top:
        rect_y -= paddle_speed
    if keys[pygame.K_s] and rect_y < play_area_bottom - rect_h:
        rect_y += paddle_speed

    # Controls player2
    if keys[pygame.K_UP] and rect2_y > play_area_top:
        rect2_y -= paddle_speed
    if keys[pygame.K_DOWN] and rect2_y < play_area_bottom - rect2_h:
        rect2_y += paddle_speed

    # Ball movement
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Ball collision with top and bottom
    if ball_y <= play_area_top or ball_y >= play_area_bottom - ball_size:
        ball_y_speed = -ball_y_speed

    # Ball collision with paddles
    if (ball_x <= rect_x + rect_w and
        rect_y < ball_y + ball_size and
        ball_y < rect_y + rect_h):
        ball_x_speed = -ball_x_speed

    if (ball_x + ball_size >= rect2_x and
        rect2_y < ball_y + ball_size and
        ball_y < rect2_y + rect2_h):
        ball_x_speed = -ball_x_speed

    # Ball out of bounds
    if ball_x < play_area_left:
        player2_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_x_speed = -ball_x_speed
    
    if ball_x > play_area_right:
        player1_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_x_speed = -ball_x_speed

    screen.blit(table, (0,0))

    # Draw play area
    pygame.draw.line(screen, white, (play_area_left, play_area_top), (play_area_left, play_area_bottom), 5) 
    pygame.draw.line(screen, white, (play_area_left, play_area_top), (play_area_right, play_area_top), 5) 
    pygame.draw.line(screen, white, (play_area_right, play_area_top), (play_area_right, play_area_bottom), 5) 
    pygame.draw.line(screen, white, (play_area_left, play_area_bottom), (play_area_right, play_area_bottom), 5) 

    # Draw paddles as images
    screen.blit(player1_image, (rect_x, rect_y))
    screen.blit(player2_image, (rect2_x, rect2_y))

    # Draw ball
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Draw score
    score_text1 = font.render(str(player1_score), True, white)
    screen.blit(score_text1, (WIDTH // 5 - score_text1.get_width(), 600))

    player1_text = font.render("Player 1", True, white)
    screen.blit(player1_text, (WIDTH // 5 - player1_text.get_width() // 2, 570))

    score_text2 = font.render(str(player2_score), True, white)
    screen.blit(score_text2, (640, 600))

    player2_text = font.render("Player 2", True, white)
    screen.blit(player2_text, (640 - player2_text.get_width() // 2, 570))

    pygame.display.flip()

pygame.quit()

import pygame
import sys
from pygame.locals import *


# game display
pygame.init()
WIDTH, HEIGHT = 825, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Breakout Game")
clock = pygame.time.Clock()

BG_COLOR = pygame.Color("#000000")
COLOR = pygame.Color("#ff1239")
score = 0

paddle = pygame.Rect(WIDTH//2-150//2, HEIGHT-20, 150, 10)
paddle_x_change = 0

ball = pygame.Rect(WIDTH//2-10,HEIGHT-40,20,20)
ball_x_change = 5
ball_y_change = -5

# blocks design
rows = 4
columns = 6
padding_right = 6
padding_top = 6
block_width = 130
block_height = 35
all_blocks = []

next_Game_time = None
timer_font = pygame.font.SysFont("monospace", 70)
score_font = pygame.font.SysFont("monospace", 40)


def create_blocks():
	for row in range(rows):
		for col in range(columns):
			x = ((padding_right * col) + padding_right) + (block_width * col)
			y = ((padding_top * row) + padding_top) + (block_height * row)
			block = pygame.Rect(x,y,block_width,block_height)
			all_blocks.append(block)

def draw_blocks(blocks):
	for block in blocks:
		pygame.draw.rect(screen, COLOR, block)

def ball_movement():
	global ball_y_change, ball_x_change, next_Game_time, score
	ball.x += ball_x_change
	ball.y += ball_y_change

	if ball.right <= 0 or ball.right >= WIDTH:
		ball_x_change = - ball_x_change

	if ball.top <= 0:
		ball_y_change = - ball_y_change

	if ball.bottom >= HEIGHT:
		next_Game_time = pygame.time.get_ticks()

	if ball.colliderect(paddle):
		ball_y_change = - ball_y_change

	for block in all_blocks:
		if ball.colliderect(block):
			ball_y_change = - ball_y_change
			all_blocks.remove(block)
			score += 1

# new game after losing match 
def start_again():
	global ball_x_change, ball_y_change, next_Game_time, score
	ball.x = WIDTH//2-10
	ball.y = HEIGHT-40
	paddle.x = WIDTH//2-150//2
	paddle.y = HEIGHT-20
	all_blocks.clear()
	create_blocks()
	score = 0
	

	current_time = pygame.time.get_ticks()

	if current_time - next_Game_time < 1000:
		num_three = timer_font.render("Ready", True, COLOR)
		num_three_rect = num_three.get_rect(center=(WIDTH//2, HEIGHT//2+10))
		screen.blit(num_three, num_three_rect)

	elif 1000 < current_time - next_Game_time < 2000:
		num_two = timer_font.render("Set", True, COLOR)
		num_two_rect = num_two.get_rect(center=(WIDTH//2, HEIGHT//2+10))
		screen.blit(num_two, num_two_rect)

	elif 2000 <current_time - next_Game_time < 3000:
		num_one = timer_font.render("GO", True, COLOR)
		num_one_rect = num_one.get_rect(center=(WIDTH//2, HEIGHT//2+10))
		screen.blit(num_one, num_one_rect)

	if current_time - next_Game_time >= 3000:
		ball_x_change = - ball_x_change
		ball_y_change = - ball_y_change
		next_Game_time= None

def draw_score():
	score_text = score_font.render(f"{score}",True,COLOR)
	score_rect = score_text.get_rect(center= (20,HEIGHT-20))
	screen.blit(score_text, score_rect)


# after winning game, display this 
def win():
	if len(all_blocks) == 0:
		screen.fill(BG_COLOR)
		ball_y_change, ball_x_change = 0,0
		won_text = timer_font.render("You Won, WOHOO!!!",True,COLOR)
		won_rect = won_text.get_rect(center = (WIDTH//2, HEIGHT//2))
		screen.blit(won_text, won_rect)

create_blocks()


while True:
	clock.tick(85)
	for event in pygame.event.get():
		if event.type == QUIT:
			print(score)
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				paddle_x_change = -5

			if event.key == K_RIGHT:
				paddle_x_change = 5

		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				paddle_x_change = 0

	screen.fill(BG_COLOR)

	paddle.x += paddle_x_change

	if paddle.left <= 0:
		paddle.left = 0

	if paddle.right >= WIDTH:
		paddle.right = WIDTH

	if next_Game_time:
		start_again()

	
	ball_movement()
	draw_blocks(all_blocks)
	draw_score()
	pygame.draw.rect(screen, COLOR, paddle)
	pygame.draw.ellipse(screen, COLOR, ball)
	win()
	pygame.display.update()
import pygame
from sys import exit
import random

pygame.init()

# screen variables
height = 600
width = height
size = 25

# surface
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# text
font = pygame.font.Font("LCD Light.ttf", 40)
text_surface = font.render("Game over.. press space to reset", "LCD Light.ttf", "red")


# class definitions

class Snake:
	def __init__(self):
		self.body = [[height//(2*size),width//(2*size)],[height//(2*size),width//(2*size)]]
	def draw(self, surface):
		for i in range(len(self.body)):
			if i == 0:
				pygame.draw.rect(surface, 'purple', pygame.Rect((self.body[i][0]) * size, (self.body[i][1]) * size, size, size))
			else:
				pygame.draw.rect(surface, 'sky blue', pygame.Rect((self.body[i][0]) * size, (self.body[i][1]) * size, size, size))
	def check(self):
		for i in range(1,len(self.body)):
			if self.body[i] == self.body[0]:
				return False
		return True
	def change_position(self, increment):
		
			self.body = self.body[:-1]
			self.body = [[(self.body[0][0] + increment[0]) % (width//size), (self.body[0][1] + increment[1]) % (height//size)]] + self.body

class  Food:
	def __init__(self):
		self.pos = [height//(2*size)+1,width//(2*size)]
	def randomize(self):
		self.pos = [random.randint(0,(width//size)-1), random.randint(0,(height//size)-1)]
	def draw(self, surface):
		pygame.draw.rect(surface, 'blue', pygame.Rect(self.pos[0]*size, self.pos[1]*size, size, size))

# snake
snake = Snake()
pos_inc = [-1,0]
run = True
reset = False

# food
food = Food()

score_font = pygame.font.Font("LCD Light.ttf", 50)
score_surface = score_font.render(f"{len(snake.body)}", "LCD Light.ttf", "green")

# main game loop
while True:
	
	if run:
		# event manager
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					increment = [0,-1]
					if len(snake.body) == 1 or [(snake.body[0][0] + increment[0]) % width, (snake.body[0][1] + increment[1]) % height] != snake.body[1]:
						pos_inc = [0,-1]
				elif event.key == pygame.K_DOWN:
					increment=[0,1]
					if len(snake.body) == 1 or [(snake.body[0][0] + increment[0]) % width, (snake.body[0][1] + increment[1]) % height] != snake.body[1]:
						pos_inc = [0,1]
				elif event.key == pygame.K_RIGHT:
					increment=[1,0]
					if len(snake.body) == 1 or [(snake.body[0][0] + increment[0]) % width, (snake.body[0][1] + increment[1]) % height] != snake.body[1]:				
						pos_inc = [1,0]
				elif event.key == pygame.K_LEFT:
					increment=[-1,0]
					if len(snake.body) == 1 or [(snake.body[0][0] + increment[0]) % width, (snake.body[0][1] + increment[1]) % height] != snake.body[1]:
						pos_inc = [-1, 0]

		snake.change_position(pos_inc)
		run = snake.check()

		if snake.body[0] == food.pos:
			snake.body += [[(snake.body[-1][0]+1)%(width//size), snake.body[-1][1]]]
			food.randomize()


		# update screen
		pygame.Surface.fill(screen, 'black')
		for i in range(width//size):
			for j in range(height//size):
				if (i+j)%2 == 0:
					pygame.draw.rect(screen, (255,200,255),pygame.Rect(size*i, size*j, size, size))
				else:
					pygame.draw.rect(screen, (255,150,255),pygame.Rect(size*i, size*j, size, size))

		food.draw(screen)
		snake.draw(screen)
		score_surface = score_font.render(f"{len(snake.body)-2}", "LCD Light.ttf", "red")
		screen.blit(score_surface, (0,0))

	else:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					reset = True

		pygame.Surface.fill(screen, 'black')
		screen.blit(text_surface, (35, 200))

	if reset:
		snake = Snake()
		pos_inc = [-1,0]
		run = True
		reset = False

	pygame.display.update()
	clock.tick(10)
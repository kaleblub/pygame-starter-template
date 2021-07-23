import pygame
# ----------- Game Initialization -------------------
pygame.init()

displayWidth, displayHeight = 700, 800

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Basic Pygame Template')

# ----------- Constants ---------------


# ----------- Main Game Function ---------------
def runGame():
	# Game Variables
	gameRunning = True
	gameOver = False

# ----------- Start Of Game Loop ---------------
	while gameRunning:

# ----------- Game Over Menu -------------------
		while gameOver == True:
			gameDisplay.fill(white)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameRunning = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameRunning = False
						gameOver = False
					if event.key == pygame.K_c:
						runGame()

# ----------- Gameplay Handling -------------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameRunning = False
			if event.type == pygame.MOUSEBUTTONUP:
				pass
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					print('left')
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					print('right')
				if event.key == pygame.K_UP or event.key == ord('w'):
					print('jump')
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					print('down')

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					print('left stop')
				 if event.key == pygame.K_RIGHT or event.key == ord('d'):
					print('right stop')
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					print('down stop')
				if event.key == ord('q'):
					pygame.quit()
					sys.exit()
					gameRunning = False

#  ----------- Game Code -------------------
		# Update
		pygame.display.update()

		# Draw

		
if __name__ == "__main__":
	runGame()
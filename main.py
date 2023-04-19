import pygame
import random

# define the game colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (160, 32, 240)

# initialize pygame
pygame.init()

# set the game display dimensions
display_width = 800
display_height = 600
SCREEN_WIDTH = display_width
SCREEN_HEIGHT = display_height

# create the game display
game_display = pygame.display.set_mode((display_width, display_height))

# set the game display caption
pygame.display.set_caption("Multiplayer Snake by Chase Galloway")

# define the game clock
clock = pygame.time.Clock()

# define the game font
font = pygame.font.SysFont(None, 25)

# define game_exit
game_exit = False

# define the Snake class

class Snake:
    def __init__(self, color, position):
        self.color = color
        self.body = [position]
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif direction == 'right' and self.direction != 'left':
            self.direction = 'right'

    def move(self):
        if self.direction == 'up':
            new_position = (self.body[0][0], self.body[0][1] - 10)
        elif self.direction == 'down':
            new_position = (self.body[0][0], self.body[0][1] + 10)
        elif self.direction == 'left':
            new_position = (self.body[0][0] - 10, self.body[0][1])
        elif self.direction == 'right':
            new_position = (self.body[0][0] + 10, self.body[0][1])

        self.body.insert(0, new_position)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for position in self.body:
            pygame.draw.rect(game_display, self.color, [position[0], position[1], 10, 10])

    def is_self_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        return False

    def is_collision(self, other_snake):
        if self.body[0] in other_snake.body[1:]:
            return True
        return False

# define the Apple class

class Apple:
    def __init__(self):
        self.position = (random.randrange(0, display_width, 10), random.randrange(0, display_height, 10))

    def generate_position(self):
        self.position = (random.randrange(0, display_width, 10), random.randrange(0, display_height, 10))

    def draw(self):
        pygame.draw.rect(game_display, RED, [self.position[0], self.position[1], 10, 10])

# define the game over function
def game_over():
    # display the game over text
    game_over_text = font.render('Game Over!', True, WHITE)
    game_display.blit(game_over_text, [350, 260])

    # update the display
    pygame.display.update()

    # pause for 2 seconds before quitting
    pygame.time.wait(3000)

# create the player snake and apple
    global player_snake
    global apple


player_snake = Snake(GREEN, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
apple = Apple()

# define computer snake


# global computer_snake

computer_snake = Snake(PURPLE, (3*display_width/4, display_height/2))

# game loop function


def game_loop():
    game_exit = False

# set the initial score
score = 0
computer_score = 0

# loop until the user quits or the snake collides with itself or the other snake
while not game_exit:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_snake.change_direction('up')
            elif event.key == pygame.K_s:
                player_snake.change_direction('down')
            elif event.key == pygame.K_a:
                player_snake.change_direction('left')
            elif event.key == pygame.K_d:
                player_snake.change_direction('right')
            elif event.key == pygame.K_UP:
                player_snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                player_snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                player_snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                player_snake.change_direction('right')
            #elif event.key == pygame.K_SPACE:
            #    player_snake.grow()
    # move the player snake
    player_snake.move()

    # check if the player snake has collided with itself
    if player_snake.is_self_collision():
        game_over()
        game_exit = True

    # check if the player snake has collided with the computer snake
    if player_snake.is_collision(computer_snake):
        game_over()
        game_exit = True

    # check if the computer snake has collided with the player snake
        if computer_snake.is_collision(player_snake):
            game_over()
            game_exit = True

# check if the player snake has hit a wall
    if player_snake.body[0][0] < 0 or player_snake.body[0][0] > display_width - 10 or player_snake.body[0][
        1] < 0 or player_snake.body[0][1] > display_height - 10:
        game_over()
        game_exit = True

# check if the computer snake has hit a wall
    if computer_snake.body[0][0] < 0 or computer_snake.body[0][0] > display_width - 10 or computer_snake.body[0][1] \
            < 0 or computer_snake.body[0][1] > display_height - 10:

        # turn the snake around
        if computer_snake.direction == 'left':
            computer_snake.direction = 'right'
        elif computer_snake.direction == 'right':
            computer_snake.direction = 'left'
        elif computer_snake.direction == 'up':
            computer_snake.direction = 'down'
        elif computer_snake.direction == 'down':
            computer_snake.direction = 'up'

    # check if the player snake has eaten the apple
    if player_snake.body[0] == apple.position:
        player_snake.grow()
        score += 1
        apple.generate_position()

    # move the computer snake
    if computer_snake.body[0][1] < apple.position[1]:
        computer_snake.change_direction('down')
    elif computer_snake.body[0][1] > apple.position[1]:
        computer_snake.change_direction('up')
    elif computer_snake.body[0][0] < apple.position[0]:
        computer_snake.change_direction('right')
    elif computer_snake.body[0][0] > apple.position[0]:
        computer_snake.change_direction('left')
    computer_snake.move()


#  check if the computer snake has eaten the apple
    if computer_snake.body[0] == apple.position:
        computer_snake.grow()
        computer_score += 1
        apple.generate_position()

    # draw the game objects
    game_display.fill(BLACK)
    player_snake.draw()
    computer_snake.draw()
    apple.draw()

    # draw the scores
    score_text = font.render('Player Score: ' + str(score), True, WHITE)
    computer_score_text = font.render('Computer Score: ' + str(computer_score), True, WHITE)
    game_display.blit(score_text, [0, 0])
    game_display.blit(computer_score_text, [150, 0])


# update the display
    pygame.display.update()

    # set the game clock tick rate
    clock.tick(10)

# quit pygame and exit the program
pygame.quit()
quit()
game_loop()

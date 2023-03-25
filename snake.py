import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [(100, 100)]
        self.radius = 10
        self.dx = 5
        self.dy = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, GREEN, element, self.radius)

    def add_element(self):
        self.size += 1
        self.elements.append((0, 0))

    def move(self):
        for i in range(self.size - 1, 0, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[0] = (self.elements[0][0] + self.dx, self.elements[0][1] + self.dy)

    def eat_food(self, food_pos):
        distance = ((self.elements[0][0] - food_pos[0]) ** 2 + (self.elements[0][1] - food_pos[1]) ** 2) ** 0.5
        if distance < self.radius:
            return True
        else:
            return False

    def collide(self):
        if self.elements[0][0] > SCREEN_WIDTH or self.elements[0][0] < 0:
            return True
        if self.elements[0][1] > SCREEN_HEIGHT or self.elements[0][1] < 0:
            return True
        for element in self.elements[1:]:
            distance = ((self.elements[0][0] - element[0]) ** 2 + (self.elements[0][1] - element[1]) ** 2) ** 0.5
            if distance < self.radius:
                return True
        return False
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.radius = 10
        self.color = RED

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def generate_position(self):
        self.position = (random.randint(self.radius, SCREEN_WIDTH - self.radius),
                         random.randint(self.radius, SCREEN_HEIGHT - self.radius))
# Create snake and food objects
snake = Snake()
food = Food()
food.generate_position()

# Set game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -5
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 5

    # Update snake and food
    snake.move()
    if snake.eat_food(food.position):
        snake.add_element()
        food.generate_position()
    if snake.collide():
        pygame.quit()
        quit()

    # Draw objects on the screen
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Set game speed
    clock.tick(20)

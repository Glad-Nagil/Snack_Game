# Import the Turtle Graphics and random modules
import turtle
import random


# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 300  # Milliseconds
FOOD_SIZE = 10  # The food square dimension


snake=[[0, 0], [20, 0], [40, 0], [60, 0]]
snake_size =20

# Cell dimensions to navigate in the serpent matrix
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Snake movements
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

 # The main loop to run the gaim
def game_loop():
     # Cleaning the environment for a new start
    stamper.clearstamps()  # Remove existing stamps made by stamper.
    global snake_direction
    
    new_head = snake[-1].copy()  # save the snake head
    new_head[0] += offsets[snake_direction][0]  # Transition action
    new_head[1] += offsets[snake_direction][1]
        
    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
                    
        reset()
    else:
        # Add new head to snake body.
        snake.append(new_head)
        
        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

    if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
    elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
    elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
    elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT
            
    stamper.clearstamps()
        # Draw snake for the first time.
    for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        # Refresh screen
    screen.title(f"Snake Game. Score: {score}, high_score : {high_score} ")
    screen.update()

        # Rinse and repeat
    turtle.ontimer(game_loop, DELAY)

 # Returns true if the snake eats the food, false otherwise
def food_collision():
    
    global food_position, score, high_score
    if get_distance(snake[-1], food_position) < 20:
        score+=1
        high_score+=1
        food_position = get_random_food_pos()
        food.goto(food_position)
        return True
    
    return False

 # Create a random position of food.
  # Returns (x,y) the food position. Do not forget to consider FOOD_SIZE
        
def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

 # Calculate the distance between the two positions and returns the distance
def get_distance(pos1, pos2):
   x1, y1 = pos1
   x2, y2 = pos2
   distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
   return distance

 # Initialize all parameters to restart the game
 # The initial snake positions parameters are snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
def reset():
    global snake, snake_direction, food_position, stamper,score,high_score
    score=0
    high_score=score
    snake = [[0, 0], [0, 20], [0, 40], [0, 60]]
    snake_direction = "up"
    food_position = get_random_food_pos()
    food.goto(food_position)
    game_loop()


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("sky blue")
screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.penup()
stamper.shapesize(snake_size / 21.5)
stamper.color("dark red")

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Set animation in motion
reset()

# Finish nicely
turtle.done()

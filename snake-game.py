import turtle
import time
import random

delay=0.1

# Score variables
score = 0
high_score = 0

# setup the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off the screen updates for better performance

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "right"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Create the snake body
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260) 
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
# Keyboard bindings
screen.listen()

# Up
screen.onkey(go_up, "w")
screen.onkey(go_up, "Up")

# Down
screen.onkey(go_down, "s")
screen.onkey(go_down, "Down")

# Left
screen.onkey(go_left, "a")
screen.onkey(go_left, "Left")

# Right
screen.onkey(go_right, "d")
screen.onkey(go_right, "Right")

# Exit the game
screen.onkey(screen.bye, "Escape")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# main game loop
while True:
    screen.update()  # Update the screen

    # Check for collision with the border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(2)  # Pause for a second
        head.goto(0, 0)
        head.direction = "stop"  # Stop the snake
        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()  # Clear the segments list
        # reset the delay
        delay=0.1
        
        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    
    # Check for collision with food
    if head.distance(food) < 20:    
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        # add a segment to the snake
        new_segment = turtle.Turtle()   
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # shorten the delay
        delay = max(0.05, delay - 0.002) # Ensure delay does not go below 0.05 seconds

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    # check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(2) # Pause for a second
            head.goto(0, 0)
            head.direction = "stop"
            # hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            # clear the segment list
            segments.clear()

            # reset the delay
            delay=0.1

            # reset the score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Control the speed of the game



screen.mainloop()# Create the snake


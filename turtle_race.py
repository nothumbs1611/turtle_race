from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles=[]

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_selection = screen.textinput(title = "Turtle Race!", prompt= "which turtle will win the race?  Enter a color: ").lower()
print(user_selection)

if user_selection:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_selection:
                print(f"You've won!  The {winning_color} is the winner!")
            else:
                print(f"You've lost!  {winning_color} came in first place")

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)











screen.exitonclick()
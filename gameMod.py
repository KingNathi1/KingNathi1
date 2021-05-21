import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("snake game by kingnathi")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

segments = []
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 Higth Score: 0", align="center", font=("Courier",24,"normal"))
#Score
score =0
high_score =0

#functions
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
        
#keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#main loop
while True:
    wn.update()
    
    # Check for a collision with the borders
    if head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        for x in segments:
            x.goto(1000, 1000)
        segments.clear()
        
        #reset the score
        score = 0
        pen.clear()
        pen.write("score {} High Score {}".format(score, high_score),align="center", font=("Courier",24,"normal"))
    
    if  head.xcor() < -290 :
        head.goto(290,head.ycor() )
        
    if  head.xcor() > 290 :
        head.goto(-290,head.ycor() )
        
    
    if head.distance(food) < 20:
        #move food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        
        #add segment
        new_seg =turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("pink")
        new_seg.penup()
        segments.append(new_seg)
        
        #increase score
        score += 10
        
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score {} High Score {}".format(score, high_score),align="center", font=("Courier",24,"normal"))
    #move the Snake body with the head
    for index in range(len(segments)-1,0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x,y)
        
    #move the 0 segment where the head is
    if len(segments)> 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #check for collision with the segments
    for x in segments:
        if x.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #hide body segments
            for x in segments:
                x.goto(1000, 1000)
            segments.clear()
            #reset the score
            score = 0
            pen.clear()
            pen.write("score {} High Score {}".format(score, high_score),align="center", font=("Courier",24,"normal"))
    
    time.sleep(delay)

wn.mainloop()

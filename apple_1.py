import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

writer = trtl.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

#-----apple.setup-----
t1 = trtl.Turtle()
t2 = trtl.Turtle()
t3 = trtl.Turtle()
t4 = trtl.Turtle()
t5 = trtl.Turtle()
tlist = [t1,t2,t3,t4,t5]
for turtles in tlist:
  turtles.showturtle()
  turtles.shape(apple_image)
  turtles.penup()

#-----writer setup-----
w1 = trtl.Turtle()
w2 = trtl.Turtle()
w3 = trtl.Turtle()
w4 = trtl.Turtle()
w5 = trtl.Turtle()
wlist = [w1,w2,w3,w4,w5]
for writers in wlist:
  writers.hideturtle()
  writers.speed(0)
  writers.pencolor("white")

letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = ""
assigned_letter = []
falling = False
dropped = 5



#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  if dropped == 5:
    active_apple.shape(apple_image)
    active_apple.setposition(rand.randint(-180, 180), rand.randint(0, 200))
    wn.update()

def drop_apple1():
  global letter
  global dropped
  global falling
  wn.onkeypress(None, assigned_letter[0])
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    tlist[0].setposition(tlist[0].xcor(), -200)
    wn.tracer(False)
    falling = False
    dropped += 1

    
def drop_apple2():
  global letter
  global dropped
  global falling
  wn.onkeypress(None, assigned_letter[1])
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    tlist[1].setposition(tlist[1].xcor(), -200)
    wn.tracer(False)
    falling = False
    dropped += 1


def drop_apple3():
  global letter
  global dropped
  global falling
  wn.onkeypress(None, assigned_letter[2])
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    tlist[2].setposition(tlist[2].xcor(), -200)
    wn.tracer(False)
    falling = False
    dropped += 1


def drop_apple4():
  global letter
  global dropped
  global falling
  wn.onkeypress(None, assigned_letter[3])
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    tlist[3].setposition(tlist[3].xcor(), -200)
    wn.tracer(False)
    falling = False
    dropped += 1
    

def drop_apple5():
  global letter
  global dropped
  global falling
  wn.onkeypress(None, assigned_letter[4])
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    tlist[4].setposition(tlist[4].xcor(), -200)
    wn.tracer(False)
    falling = False
    dropped += 1


def letter_write(temp_apple):
  global letter
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  print(assigned_letter)
  writer.setposition(temp_apple.xcor()-18, temp_apple.ycor()-40)
  writer.write(letter, font=("Arial", 55))

def listen():
  for i in range(5):
    draw_apple(tlist[i])
    letter_write(tlist[i])
    
#-----function calls-----
listen()
dropped = 0
wn.onkeypress(drop_apple1, assigned_letter[0])
wn.onkeypress(drop_apple2, assigned_letter[1])
wn.onkeypress(drop_apple3, assigned_letter[2])
wn.onkeypress(drop_apple4, assigned_letter[3])
wn.onkeypress(drop_apple5, assigned_letter[4])
wn.listen()
wn.mainloop()
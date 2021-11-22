import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

#-----apple setup-----
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
  writers.penup()

#-----letter setup-----
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = ""
assigned_letter = []
falling1 = False
falling2 = False
falling3 = False
falling4 = False
falling5 = False
dropped = 0

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.setposition(rand.randint(-180, 180), rand.randint(0, 200))
  wn.update()

# functions to drop an apple, for apples 1-5
def drop_apple1():
  wn.update()
  global dropped
  global falling1
  wn.onkeypress(None, assigned_letter[0])
  if falling1 == False: 
    falling1 = True
    wn.tracer(True)
    w1.clear()
    tlist[0].setposition(tlist[0].xcor(), -200)
    wn.tracer(False)
    falling1 = False
    dropped += 1
    if dropped == 5:
      reset()
    
def drop_apple2():
  wn.update()
  global dropped
  global falling2
  wn.onkeypress(None, assigned_letter[1])
  if falling2 == False: 
    falling2 = True
    wn.tracer(True)
    w2.clear()
    tlist[1].setposition(tlist[1].xcor(), -200)
    wn.tracer(False)
    falling2 = False
    dropped += 1
    if dropped == 5:
      reset()

def drop_apple3():
  wn.update()
  global dropped
  global falling3
  wn.onkeypress(None, assigned_letter[2])
  if falling3 == False: 
    falling3 = True
    wn.tracer(True)
    w3.clear()
    tlist[2].setposition(tlist[2].xcor(), -200)
    wn.tracer(False)
    falling3 = False
    dropped += 1
    if dropped == 5:
      reset()

def drop_apple4():
  wn.update()
  global dropped
  global falling4
  wn.onkeypress(None, assigned_letter[3])
  if falling4 == False: 
    falling4 = True
    wn.tracer(True)
    w4.clear()
    tlist[3].setposition(tlist[3].xcor(), -200)
    wn.tracer(False)
    falling4 = False
    dropped += 1
    if dropped == 5:
      reset()

def drop_apple5():
  wn.update()
  global dropped
  global falling5
  wn.onkeypress(None, assigned_letter[4])
  if falling5 == False: 
    falling5 = True
    wn.tracer(True)
    w5.clear()
    tlist[4].setposition(tlist[4].xcor(), -200)
    wn.tracer(False)
    falling5 = False
    dropped += 1
    if dropped == 5:
      reset()

# functions to write a letter on the apples 1 - 5
def letter_write1():
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  w1.setposition(t1.xcor()-18, t1.ycor()-40)
  w1.write(letter, font=("Arial", 55))

def letter_write2():
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  w2.setposition(t2.xcor()-18, t2.ycor()-40)
  w2.write(letter, font=("Arial", 55))

def letter_write3():
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  w3.setposition(t3.xcor()-18, t3.ycor()-40)
  w3.write(letter, font=("Arial", 55))

def letter_write4():
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  w4.setposition(t4.xcor()-18, t4.ycor()-40)
  w4.write(letter, font=("Arial", 55))

def letter_write5():
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  assigned_letter.append(letter)
  w5.setposition(t5.xcor()-18, t5.ycor()-40)
  w5.write(letter, font=("Arial", 55))

# resets the 5 apples 
def reset():
    wn.update()
    if len(letter_list) >= 5:
        global dropped
        dropped = 0
        assigned_letter.clear()
        for i in range(5):
            draw_apple(tlist[i])
        letter_write1()
        letter_write2()
        letter_write3()
        letter_write4()
        letter_write5()
        # checks for key presses, assigned to each apple
        wn.onkeypress(drop_apple1, assigned_letter[0])
        wn.onkeypress(drop_apple2, assigned_letter[1])
        wn.onkeypress(drop_apple3, assigned_letter[2])
        wn.onkeypress(drop_apple4, assigned_letter[3])
        wn.onkeypress(drop_apple5, assigned_letter[4])
        wn.listen()
    
#-----function calls-----
reset()

wn.mainloop()

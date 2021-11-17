#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = ""
falling = False

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  global falling
  if falling == False: 
    falling = True
    wn.tracer(True)
    writer.clear()
    apple.setposition(apple.xcor(), -200)
    wn.tracer(False)
    apple.setposition(rand.randint(-180, 180), rand.randint(0, 200))
    draw_apple(apple)
    letter_write()
    falling = False
    wn.onkeypress(drop_apple, letter)

def letter_write():
  global letter
  letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  print(len(letter_list))
  writer.setposition(apple.xcor()-18, apple.ycor()-40)
  writer.write(letter, font=("Arial", 55))

#-----function calls-----
draw_apple(apple)
apple.setposition(rand.randint(-180, 180), rand.randint(0, 200))
letter_write()


wn.listen()
wn.onkeypress(drop_apple, letter)
wn.mainloop()
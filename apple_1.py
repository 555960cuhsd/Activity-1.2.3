#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
letter = trtl.Turtle()
letter.hideturtle()
letter.penup()
letter.color("white")
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  wn.tracer(True)
  letter.clear()
  apple.setposition(apple.xcor(), -200)
  wn.tracer(False)

def letter_write():
  letter.setposition(apple.xcor()-18, apple.ycor()-40)
  letter.write("A", font=("Arial", 55))
  

#-----function calls-----
draw_apple(apple)
letter_write()

wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()
import turtle as tu
  
root = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object

for i in range(3):
    # moves the pen in the 
    # forward direction in 
    # the new direction by
    # 110 pixels
    root.forward(250)
    root.left(120)

wn.exitonclick()
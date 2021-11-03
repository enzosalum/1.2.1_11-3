# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot = trtl.Turtle()

#-----game configuration----
spotColor = "pink"
spotShape = "circle"
spotSize = "2"

#-----initialize turtle-----
spot.shape(spotShape)
spot.pensize(spotSize)
spot.fillcolor(spotColor)

#-----game functions--------

def spot_clicked(x, y):
  print("this is a test, you did spot_clicked")

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()
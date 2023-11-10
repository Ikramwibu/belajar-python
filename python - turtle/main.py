from turtle import *

getscreen()
bgcolor("yellow")
shape("turtle")
pencolor("pink")
pensize(3)
shape("turtle")

speed(0)

init_size = 30

for i in range(360):
  for i in range(4):
    forward(init_size)
    left(360/4)
  left(10)

done()
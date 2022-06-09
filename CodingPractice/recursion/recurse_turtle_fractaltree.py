""" Draw a fractal tree """
import turtle, random

def f_tree(trtl, branchlen):
  if branchlen > 5:
    #turn_deg = random.randrange(5, 20)
    dim_factor = random.randrange(5,50, 5)
    trtl.pensize(branchlen // 4)
    trtl.forward(branchlen)
    trtl.right(20 )
    f_tree(trtl, branchlen - dim_factor)
    trtl.left(40)
    f_tree(trtl, branchlen - dim_factor)
    trtl.right(20)
    trtl.backward(branchlen)

if __name__ == "__main__":
  branch_factor = 100
  t = turtle.Turtle()
  win = turtle.Screen()
  t.penup()
  t.setposition(-branch_factor,-branch_factor)
  t.left(90)
  t.pendown()
  t.color("violet")
  f_tree(t, 150)
  win.exitonclick()

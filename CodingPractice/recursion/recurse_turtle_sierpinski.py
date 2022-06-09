""" Draw a fractal tree """
import turtle

from matplotlib.colors import Colormap

def draw_triangle(t_obj, points, color):
  t_obj.fillcolor(color)
  t_obj.penup()
  t_obj.setposition(points[0])
  t_obj.pendown()
  t_obj.begin_fill()
  t_obj.setposition(points[1])
  t_obj.setposition(points[2])
  t_obj.setposition(points[0])
  t_obj.end_fill()

def get_mid(p1, p2):
  return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

def sierpinski(t_obj, points, degree):
  colormap = ['blue','red','green','white','yellow',
              'violet','orange']

  draw_triangle(t_obj, points, colormap[degree])
  
  if degree > 0:
    sierpinski( t_obj, 
                [points[0],get_mid(points[0], points[1]), get_mid(points[0], points[2])],
                degree - 1 )
    
    sierpinski( t_obj, 
                [get_mid(points[0], points[1]), points[1], get_mid(points[1], points[2])],
                degree - 1 )
    
    sierpinski( t_obj, 
                [get_mid(points[0], points[2]), get_mid(points[1], points[2]), points[2]],
                degree - 1 )

if __name__ == "__main__":
  t = turtle.Turtle()
  win = turtle.Screen()
  points = [(-100,-50),(0,100),(100,-50)]
  deg = 3

  sierpinski(t, points, deg)
  win.exitonclick()

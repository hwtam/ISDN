import turtle
import random
import time

## variable
n = 100  #numbber of locations at maximum
map_size = 750  #the actual size of the map
map_size /= 2
square = 75 #define what is "near"

## setup, constant
turtle.speed(0)
turtle.listen()
turtle.title("Simulation for team 4 project")
turtle.ht()
turtle.bgcolor("light green")
screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
turtle.tracer(False)
locations = []
bus = turtle.Turtle()
bus.shape("circle")
bus.color("red")
bus.speed(4)
bus.width(4)
counter = turtle.Turtle()
counter.ht()
counter.up()
counter.goto(-300,-map_size - 70)

#just to pack the turtle instance, xcor, and ycor together
class location :
  def __init__(self, x, y) :
    self.tur = turtle.Turtle()
    self.x = x
    self.y = y
    t = self.tur
    t.up()
    t.speed(0)
    t.right(90)
    t.shapesize(2)
    t.goto(x, y)

#the function for keypressed event; set up for routing
def prepareRouting() :
  turtle.onkey(None,"space")
  turtle.tracer(False)
  bus.clear()
  generateLocation()
  turtle.tracer(True)
  time.sleep(0.5)
  routing()
  turtle.onkey(prepareRouting,"space")

#really routing
def routing() :
  global locations
  for i in range(n) :
    bus.dot(10,'green')
    next = distance(bus.xcor(), bus.ycor())
    if next == None :
      break
    stops = []
    for t in locations :
      if t.x < next.x - square :
        continue
      if t.x > next.x + square :
        continue
      if t.y < next.y - square :
        continue
      if t.y > next.y + square :
        continue
      stops.append(t)
    avgX = 0
    avgY = 0
    for t in stops :
      avgX += t.x
      avgY += t.y
    avgX /= len(stops)
    avgY /= len(stops)
    bus.goto(avgX, avgY)
    turtle.tracer(False)
    time.sleep(0.20)
    for t in stops :
      t.tur.ht()
      locations.remove(t)
      del t
    bus.pencolor('blue')
    bus.write(str(i+1), font=("Courier", 10, "bold"))
    bus.pencolor('red')
    counter.clear()
    counter.write("There are " + str(len(locations)) + " passengers in the vehicle", font=("Courier", 20, "bold"))
    turtle.tracer(True)  
  bus.home()

#detect the nearest point; return the location : obj
def distance(x, y) :
  global locations 
  a = map_size*3
  temp = None
  for t in locations :
    b = ((x-t.x)**2 + (y-t.y)**2)**0.5
    if b < a :
      a = b
      temp = t
  return temp

#generate the map
def generateMap() :
  turtle.up()
  turtle.goto(-map_size, map_size)
  turtle.down()
  turtle.pensize(5)
  turtle.fillcolor("light grey")
  turtle.begin_fill()
  for _ in range(4) :
    turtle.fd(map_size*2)
    turtle.right(90)
  turtle.end_fill()
  turtle.up()
  turtle.pencolor("red")
  turtle.goto(-map_size + 50, turtle.ycor() + 30)
  turtle.write("Map", font=("Courier", 30, "bold"))
  turtle.goto(-map_size - 325, 150)
  turtle.write("Simulate the routing", font=("Courier", 20, "bold"))
  turtle.right(90)
  turtle.fd(30)
  turtle.write("*Algorithms are used instead of AI*", font=("Courier", 10, "bold"))
  turtle.fd(20)
  turtle.write("*The route may looks strange*", font=("Courier", 10, "bold"))
  turtle.fd(20)
  turtle.write("*But it will be better with the help of AI*", font=("Courier", 9, "bold"))
  turtle.fd(100)
  turtle.pencolor("black")
  turtle.write("The arrows represent :", font=("Courier", 10, "bold"))
  turtle.fd(30)
  turtle.write("the destinations of passengers", font=("Courier", 10, "bold"))
  turtle.fd(30)
  turtle.write(str(n) + " passengers in total", font=("Courier", 10, "bold"))
  turtle.fd(50)
  turtle.write("The red dot represents :", font=("Courier", 10, "bold"))
  turtle.fd(30)
  turtle.write("the location of the vehicle ", font=("Courier", 10, "bold"))
  turtle.goto(map_size + 15, 75)
  turtle.pencolor("blue")
  turtle.write("Press 'SPACE'", font=("Courier", 30, "bold"))
  turtle.fd(50)
  turtle.write("to generate a new round", font=("Courier", 15, "bold"))
  turtle.tracer(True)


#generate locations
def generateLocation() :
  for _ in range(n) :
    x = random.randint(-map_size+75, map_size-75)
    y = random.randint(-map_size+75, map_size-75)
    new = location(x, y)
    locations.append(new)
  counter.clear()
  counter.write("There are " + str(n) + " passengers in the vehicle", font=("Courier", 20, "bold"))
    
## main program
generateMap()
turtle.onkey(prepareRouting, "space")
turtle.done()

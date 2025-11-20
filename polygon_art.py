import turtle
import random

class Shape:
    def __init__(self):
        self.num_sides = None
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def reduction_ratio(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio         


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.num_sides = 3

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.num_sides = 4

class Pentagon(Shape):
    def __init__(self):
        super().__init__()
        self.num_sides = 5


class Choice:
    def __init__(self):
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

    def user_draw(self):
        if self.choice == 1:
            for i in range(30):
                polygon_shape = Triangle()
                polygon_shape.draw_polygon()
        elif self.choice == 2:
            for i in range(30):
                polygon_shape = Square()
                polygon_shape.draw_polygon()
        elif self.choice == 3:
            for i in range(30):
                polygon_shape = Pentagon()
                polygon_shape.draw_polygon()
        elif self.choice == 4:
            for i in range(30):
                if i % 2 == 0:
                    polygon_shape = Triangle()
                    polygon_shape.draw_polygon()
                elif i % 3 == 0:
                    polygon_shape = Square()
                    polygon_shape.draw_polygon()
                else:
                    polygon_shape = Pentagon()
                    polygon_shape.draw_polygon()
        elif self.choice == 5:
            for i in range(30):
                polygon_shape = Triangle()
                for j in range(3):
                    polygon_shape.draw_polygon()
                    polygon_shape.reduction_ratio()
        elif self.choice == 6:
            for i in range(30):
                polygon_shape = Square()
                for j in range(3):
                    polygon_shape.draw_polygon()
                    polygon_shape.reduction_ratio()
        elif self.choice == 7:
            for i in range(30):
                polygon_shape = Pentagon()
                for j in range(3):
                    polygon_shape.draw_polygon()
                    polygon_shape.reduction_ratio()
        elif self.choice == 8:
            for i in range(30):
                if i % 2 == 0:
                    polygon_shape = Triangle()
                    polygon_shape.draw_polygon()
                elif i % 3 == 0:
                    polygon_shape = Square()
                    polygon_shape.draw_polygon()
                else:
                    polygon_shape = Pentagon()
                    polygon_shape.draw_polygon()
                for j in range(3):
                    polygon_shape.draw_polygon()
                    polygon_shape.reduction_ratio()
        elif self.choice == 9:
            for i in range(30):
                if i % 2 == 0:
                    polygon_shape = Triangle()
                elif i % 3 == 0:
                    polygon_shape = Square()
                else:
                    polygon_shape = Pentagon()
                get_small_or_not = random.choice([True, False])
                if get_small_or_not == True:
                    for j in range(3):
                        polygon_shape.draw_polygon()
                        polygon_shape.reduction_ratio()
                else:
                    polygon_shape.draw_polygon()


draw = Choice()
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
draw.user_draw()
turtle.done()
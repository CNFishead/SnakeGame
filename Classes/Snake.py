from turtle import Turtle

START_POS = [(0, 0), (-10, 0), (-20, 0)]


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
            # self.move()

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)
            # self.move()

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
            # self.move()

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
            # self.move()

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color('white')
        segment.shapesize(.5, .5)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def tail_increase(self):
        self.add_segment((self.segments[-1].position()))

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
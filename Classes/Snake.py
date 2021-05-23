from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            segment = Turtle("square")
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

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
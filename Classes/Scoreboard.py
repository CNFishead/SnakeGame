from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}  Highscore: {self.high_score}', align='center', font=('Arial', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()






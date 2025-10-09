from turtle import Turtle,Screen
screen = Screen()
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.keep_score()
        self.hideturtle()

    def keep_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.keep_score()

    def increase_score(self):
        self.score += 1
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER! Your score is {self.score}.", False, ALIGNMENT, FONT)










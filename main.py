import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (180, 200), (160, 200)]  # Initial snake position (head, body, tail)
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.game_over_flag = False

        self.update_snake()
        self.update_food()
        self.root.bind("<KeyPress>", self.change_direction)
        self.move_snake()

    def create_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return (x, y)

    def update_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", tag="snake")

    def update_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="red", tag="food")

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        if self.game_over_flag:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20

        new_head = (head_x, head_y)

        if (new_head in self.snake[1:] or not (0 <= head_x < 400 and 0 <= head_y < 400)):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
            self.update_food()
            self.score += 1
        else:
            self.snake.pop()

        self.update_snake()
        self.root.after(100, self.move_snake)

    def game_over(self):
        self.game_over_flag = True
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24))
        self.canvas.create_text(200, 240, text=f"Score: {self.score}", fill="white", font=("Arial", 18))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

import tkinter as tk
import random

# Constants
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.running = True
        
        self.root.bind("<KeyPress>", self.change_direction)
        self.update()
        
    def create_food(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return x, y
    
    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = {"Up", "Down", "Left", "Right"}
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        
        if new_direction in all_directions and new_direction != opposites[self.direction]:
            self.direction = new_direction
    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE
        
        new_head = (head_x, head_y)
        
        # Check for collisions
        if (
            head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT
            or new_head in self.snake
        ):
            self.running = False
            return
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()
    
    def draw(self):
        self.canvas.delete("all")
        
        # Draw snake
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1], segment[0] + CELL_SIZE, segment[1] + CELL_SIZE,
                fill="green"
            )
        
        # Draw food
        self.canvas.create_oval(
            self.food[0], self.food[1], self.food[0] + CELL_SIZE, self.food[1] + CELL_SIZE,
            fill="red"
        )
    
    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=("Arial", 20))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

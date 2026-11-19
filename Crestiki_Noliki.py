import turtle

screen = turtle.Screen()
screen.setup (1500, 1200)
screen.title("Крестики-Нолики")
screen.bgcolor("#393939")
paint = turtle.Turtle()
paint.speed(0)
paint.hideturtle()
paint.color("#FEFEFE")
paint.pensize(7)
SIZE = 100
def draw_square():
    for i in range(4):
        paint.forward(SIZE)
        paint.right(90)
# Функция для создания поля.
def draw_field(x: int, y: int):
    for y in range(y, y + SIZE*2 +1, SIZE):
        for x_changer in range(0, 2*SIZE + 1, SIZE):
            paint.penup()
            paint.goto(x + x_changer, y)
            paint.pendown()
            draw_square()
draw_field(int(-1.5*SIZE), int(-0.5*SIZE))

paint.penup()
paint.goto(0, 0)
# Функция для создания крестиков.
def draw_x(x: int, y: int):
    paint.color("#349DFF")
    paint.penup()
    paint.setheading(0)
    paint.goto(x +6, y -7)
    paint.pendown()
    paint.goto(x -6 + SIZE, y + 7 -SIZE)
    paint.penup()
    paint.goto(x + 7 , y - SIZE + 6)
    paint.pendown()
    paint.goto(x + SIZE -6, y - 8)
# Функция для создания кружков.
def draw_0(x: int, y: int):
    paint.color("#fd0000")
    paint.penup()
    paint.setheading(0)
    paint.goto(x, y + 10)
    paint.pendown()
    paint.circle(SIZE/2.5)
# Функция клика.

queue = [1]
def click(x: float, y: float):
    index_x = int((x + SIZE*1.5)//SIZE)
    index_y = int((y - SIZE*1.5)//-SIZE)
    if index_x >= 0 and index_y >= 0 and index_x <= 2 and index_y <= 2 and win[0] == False:
        print(index_x, index_y)
        if cells[index_y][index_x] == "n":
            cor_x = index_x*SIZE - 1.5*SIZE
            cor_y = index_y*-SIZE + 1.5*SIZE

            if queue[0] == 1:
                draw_x(cor_x, cor_y)
                queue[0] = 0
                cells[index_y][index_x] = "x"
                check_win("x")
            else:
                draw_0(cor_x +50, cor_y - 100)
                queue[0] = 1
                cells[index_y][index_x] = "0"
                check_win("0")

screen.onclick(click)



cells = [
    ["n","n","n"],
    ["n","n","n"],
    ["n","n","n"]
]
def check_win(player: str):
    win_comb = [
        [0, 0, 1, 0, 2, 0],
        [0, 1, 1, 1, 2, 1],
        [0, 2, 1, 2, 2, 2],
        [0, 0, 0, 1, 0, 2],
        [1, 0, 1, 1, 1, 2],
        [0, 0, 0, 1, 0, 2],
        [0, 0, 1, 1, 2, 2],
        [0, 2, 1, 1, 2, 0],
    ]
    for x1, y1, x2, y2, x3, y3 in win_comb:
        if cells[y1][x1] == player and cells[y2][x2] == player and cells[y3][x3] == player:
            win[0] = True
            paint.penup()
            paint.goto(0, SIZE*2.5)
            paint.pendown()
            paint.color("White")
            name = "Хрестик" if  player == "x" else "Нолик"
            paint.write(f"Переміг {name}", align="center", font=("Arial", 40))
            start_x = x1*SIZE-SIZE
            start_y = y1*-SIZE+SIZE
            finish_x = x3*SIZE-SIZE
            finish_y = y3*-SIZE+SIZE
            paint.penup()
            paint.pensize(10)
            paint.goto(start_x, start_y)
            paint.pendown()
            paint.goto(finish_x, finish_y)
            break
win = [False]

screen.mainloop()

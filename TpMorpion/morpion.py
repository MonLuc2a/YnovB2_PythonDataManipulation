import tkinter
import tkinter.messagebox

# create the window
window = tkinter.Tk()
window.title("Morpion")
window.geometry("300x300")

# create the canvas
canvas = tkinter.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

# create the grid
canvas.create_line(100, 0, 100, 300, fill="black")
canvas.create_line(200, 0, 200, 300, fill="black")
canvas.create_line(0, 100, 300, 100, fill="black")
canvas.create_line(0, 200, 300, 200, fill="black")

player1 = True
board = [['' for _ in range(3)] for _ in range(3)]

def draw_cross(x, y):
    canvas.create_line(x, y, x + 100, y + 100, fill="red")
    canvas.create_line(x, y + 100, x + 100, y, fill="red")

def draw_circle(x, y):
    canvas.create_oval(x, y, x + 100, y + 100, outline="blue")

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
       return True
    return False

def check_draw():
    return all([cell != '' for row in board for cell in row])

def click(event):
    global player1, board
    x = event.x // 100 * 100
    y = event.y // 100 * 100
    row = event.y // 100
    col = event.x // 100

    if board[row][col] == '':
        if player1:
            draw_cross(x, y)
            board[row][col] = 'X'
            player1 = False
        else:
            draw_circle(x, y)
            board[row][col] = 'O'
            player1 = True

        if check_winner():
            winner = "Joueur 1 (X)" if not player1 else "Joueur 2 (O)"
            tkinter.messagebox.showinfo("Victoire", f"{winner} a gagné !")
            window.destroy()
        elif check_draw():
            tkinter.messagebox.showinfo("Match nul", "Match nul !")
            window.destroy()

# launch the window
window.bind("<Button-1>", click)
window.mainloop()
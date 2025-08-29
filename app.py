# Create a 3x3 board
board = [[" x " for _ in range(3)] for _ in range(3)]

# Function to print the board in the terminal
def print_board():
    for row in board:
        print("|".join(row))
    print()

# Place a move
def place_move(player, row, col):
    if board[row][col] != " ":
        return False
    board[row][col] = player
    return True

# Check for a win
def check_win(player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for a draw
def check_draw():
    return all(cell != " " for row in board for cell in row)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Display the board in an HTML template
    return render_template("index.html", board=board)

if __name__ == '__main__':
    app.run(debug=True)
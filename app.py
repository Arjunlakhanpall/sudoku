from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Function to generate a new Sudoku puzzle
def generate_sudoku():
    # A simple, pre-defined Sudoku puzzle for the sake of example
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    return board

# Function to solve the Sudoku puzzle
def solve_sudoku(board):
    # Solve the puzzle using a backtracking algorithm
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + box_row][j + box_col] == num:
                    return False
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve(board)
    return board

# Endpoint to get a new Sudoku puzzle
@app.route('/new', methods=['GET'])
def new_puzzle():
    board = generate_sudoku()
    return jsonify({"board": board})

# Endpoint to solve a Sudoku puzzle
@app.route('/solve', methods=['POST'])
def solve_puzzle():
    data = request.get_json()
    board = data.get("board")
    
    if not board or len(board) != 9 or any(len(row) != 9 for row in board):
        return jsonify({"error": "Invalid board format. The board should be a 9x9 grid."}), 400
    
    solved_board = solve_sudoku(board)
    return jsonify({"solved_board": solved_board})

if __name__ == '__main__':
    app.run(debug=True)

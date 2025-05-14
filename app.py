from flask import Flask, jsonify, request, render_template
import random
import copy

app = Flask(__name__)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
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

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(15):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(board, row, col, num):
            board[row][col] = num
    solved = copy.deepcopy(board)
    solve(solved)
    for _ in range(40):
        r, c = random.randint(0, 8), random.randint(0, 8)
        solved[r][c] = 0
    return solved

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new', methods=['GET'])
def new_game():
    board = generate_board()
    return jsonify(board=board)

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    data = request.json
    board = data.get('board')
    if not board:
        return jsonify({'error': 'Board is missing'}), 400
    if solve(board):
        return jsonify({'solution': board})
    else:
        return jsonify({'error': 'No solution exists'}), 400

if __name__ == '__main__':
    app.run(debug=True)

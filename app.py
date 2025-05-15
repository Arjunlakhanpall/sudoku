from flask import Flask, render_template, request, jsonify

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

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    board = data["board"]
    if solve_sudoku(board):
        return jsonify({"solution": board})
    else:
        return jsonify({"error": "No solution exists!"}), 400

if __name__ == "__main__":
    app.run(debug=True)

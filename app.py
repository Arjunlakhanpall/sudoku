from flask import Flask, render_template, request
from sudoku import solve

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    board = [[0 for _ in range(9)] for _ in range(9)]
    if request.method == "POST":
        # Get board from form
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = request.form.get(f"cell-{i}-{j}")
                row.append(int(val) if val and val.isdigit() else 0)
            board.append(row)
        solved_board = [row[:] for row in board]
        if solve(solved_board):
            return render_template("solution.html", board=solved_board)
        else:
            return render_template("solution.html", board=None, error="No solution found.")
    return render_template("index.html", board=board)

if __name__ == "__main__":
    app.run(debug=True)

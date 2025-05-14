# 🧩 Sudoku Game in Python

A logic-based number placement game implemented using Python. This project includes a playable Sudoku board and an automatic solver using the backtracking algorithm.

## 📌 Description

Sudoku is a classic puzzle game where the objective is to fill a 9×9 grid so that each column, row, and 3×3 subgrid contains all the digits from 1 to 9 without repetition.

This Python application allows users to:
- Play Sudoku manually
- Solve puzzles automatically
- Generate new boards (optional feature)

## 🛠️ Features

- ✅ Interactive Sudoku grid
- 🧠 Backtracking-based solver
- 🔢 Input validation
- 🧪 CLI or GUI (Tkinter) interface
- 💾 Load predefined puzzles

## 🧰 Tech Stack

- **Language:** Python 3.x
- **Libraries:** Tkinter (for GUI) or `os`, `time`, `random`, etc. (for CLI version)

## 📂 Project Structure

```bash
sudoku-python/
├── README.md
├── main.py           # Entry point to run the game
├── solver.py         # Backtracking Sudoku solver
├── board.py          # Board generation and validation
├── gui.py            # GUI using Tkinter (if applicable)
└── puzzles/          # Optional folder with puzzle files

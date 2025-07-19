
---

### ✅ `tic_tac_toe.py` (copy this Python code)

```python
def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check_winner(board, player):
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in combos)

def is_full(board):
    return all(cell in ["X", "O"] for cell in board)

def main():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue

        move = int(move) - 1
        if board[move] in ["X", "O"]:
            print("Cell already taken. Try another.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()

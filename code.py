import random

def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else '_' for x in row))
    print()

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def move_blank(board, direction):
    x, y = find_blank(board)
    dx, dy = 0, 0
    if direction == 'up': dx = -1
    elif direction == 'down': dx = 1
    elif direction == 'left': dy = -1
    elif direction == 'right': dy = 1
    else: return False

    nx, ny = x + dx, y + dy
    if 0 <= nx < 3 and 0 <= ny < 3:
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        return True
    return False

def is_solved(board):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    return board == goal

def generate_solvable_board():
    while True:
        nums = list(range(9))
        random.shuffle(nums)
        board = [nums[i:i+3] for i in range(0, 9, 3)]
        if is_solvable(nums):
            return board

def is_solvable(nums):
    inv = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if nums[i] and nums[j] and nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0

# Main game
board = generate_solvable_board()

while True:
    print_board(board)
    if is_solved(board):
        print("🎉 Puzzle Solved!")
        break
    move = input("Enter move (up/down/left/right): ").strip().lower()
    if not move_blank(board, move):
        print("Invalid move!")

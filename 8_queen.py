import pygame
import sys

pygame.init()

n = 8
square_size = 80
width, height = n*square_size, n*square_size

blue = (66, 133, 244)
red = (234, 67, 53)
yellow = (251, 188, 4)
green = (52, 168, 83)


screen = pygame.display.set_mode((width, height))
icon_img = pygame.image.load("D:/PYTHON/N_queens_problem_solving/Artboard_24@3x.png")
pygame.display.set_icon(icon_img)
pygame.display.set_caption('8 con hau')

def draw_chessboard():
    for row in range(n):
        for col in range(n):
            color = blue if (row + col) % 2 == 0 else yellow
            pygame.draw.rect(screen, color, (col*square_size, row*square_size, square_size, square_size))

def draw_queens(row, col):
    queen_img = pygame.image.load("D:/PYTHON/N_queens_problem_solving/Artboard_24@3x.png")
    queen_img = pygame.transform.scale(queen_img, (square_size, square_size))
    screen.blit(queen_img, (col*square_size, row*square_size))

def is_valid(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end = " ")
        print()


def solve_queen(board, col, n, count):
    if col == n:
        count[0] += 1
        # print_board(board, n)
        # print("\n")
        pygame.event.pump()
        draw_chessboard()
        for c, r in enumerate(board):
            draw_queens(r, c)
        # draw_queens(board)
        pygame.display.flip()
        pygame.time.wait(500)    
        return 
    for row in range(n):
        if is_valid(board, row, col, n):
            board[col] = row
            solve_queen(board, col + 1, n, count)
            board[col] = -1

# n = 8 
board = [-1] * n
count = [0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            solve_queen(board, 0, n, count)
            text = font.render('co {} phuong an'.format(count), True, green)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
        for i in range(row):
                    if board[i] == col or \
                                       board[i] - i == col - row or \
                                                  board[i] + i == col + row:
                                                                  return False
                                                                  return True

                                                              def solve_n_queens(n, row=0, board=[]):
                                                                      if row == n:
                                                                                  result.append(board[:])
                                                                                          return

                                                                                          for col in range(n):
                                                                                                      if is_safe(board, row, col, n):
                                                                                                                      board.append(col)
                                                                                                                                  solve_n_queens(n, row + 1, board)
                                                                                                                                              board.pop()

                                                                                                                                              def print_board(board, n):
                                                                                                                                                      for row in range(n):
                                                                                                                                                                  line = ""
                                                                                                                                                                          for col in range(n):
                                                                                                                                                                                          if board[row] == col:
                                                                                                                                                                                                              line += "Q "
                                                                                                                                                                                                                          else:
                                                                                                                                                                                                                                              line += ". "
                                                                                                                                                                                                                                                      print(line)
                                                                                                                                                                                                                                                          print()

                                                                                                                                                                                                                                                          def main():
                                                                                                                                                                                                                                                                  global result
                                                                                                                                                                                                                                                                      result = []

                                                                                                                                                                                                                                                                          if len(sys.argv) != 2:
                                                                                                                                                                                                                                                                                      print("Usage: nqueens N")
                                                                                                                                                                                                                                                                                              sys.exit(1)

                                                                                                                                                                                                                                                                                                  try:
                                                                                                                                                                                                                                                                                                              n = int(sys.argv[1])
                                                                                                                                                                                                                                                                                                                      if n < 4:
                                                                                                                                                                                                                                                                                                                                      print("N must be at least 4")
                                                                                                                                                                                                                                                                                                                                                  sys.exit(1)
                                                                                                                                                                                                                                                                                                                                                      except ValueError:
                                                                                                                                                                                                                                                                                                                                                                  print("N must be a number")
                                                                                                                                                                                                                                                                                                                                                                          sys.exit(1)

                                                                                                                                                                                                                                                                                                                                                                              solve_n_queens(n)

                                                                                                                                                                                                                                                                                                                                                                                  for solution in result:
                                                                                                                                                                                                                                                                                                                                                                                              print_board(solution, n)

                                                                                                                                                                                                                                                                                                                                                                                              if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                      main()

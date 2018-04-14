#Ben Carlson
import sys
import math

def problem():
  num = int(input())
  for i in range(num):
    A = int(input())
    land = [[False for j in range(math.ceil(A / 3))] for i in range(3)]

    a, b = 1, 1
    while True:
      print(str(a + 1) + " " + str(b + 1))
      sys.stdout.flush()
      line = input().split(" ")
      c, d = int(line[0]), int(line[1])
      if c == -1 and d == -1:
        return
      if c == 0 and d == 0:
        break
      c -= 1
      d -= 1
      land[c][d] = True
      if check1(land, a, b):
        if b < len(land[a]) - 5:
          b += 3
        elif b == len(land[a]) - 2:
          break
        else:
          b = len(land[a]) - 2
      elif check2(land, a, b):
        if b < len(land[a]) - 2:
          b += 1

def check1(land, a, b):
  return (land[a - 1][b - 1] and land[a - 1][b] and land[a - 1][b + 1]
    and land[a][b - 1] and land[a][b] and land[a][b + 1]
    and land[a + 1][b - 1] and land[a + 1][b] and land[a + 1][b + 1])

def check2(land, a, b):
  return land[a - 1][b - 1] and land[a][b - 1] and land[a + 1][b - 1]

problem()



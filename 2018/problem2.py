#Ben Carlson
import sys

def main():
  out = problem()
  for i in range(len(out)):
    print("Case #" + str(i + 1) + ": " + out[i])
  sys.stdout.flush()

def problem():
  num = int(input())
  out = []
  for i in range(num):
    length = int(input())
    arr = input().split(" ")
    for i in range(length):
      arr[i] = int(arr[i])
    trouble(arr)
    tr = arr[:]
    arr.sort()
    flag = True
    for j in range(len(arr)):
      if arr[j] != tr[j]:
        flag = False
        out.append(str(j))
        break
    if flag:
      out.append("OK")
  return out

def trouble(arr):
  while True:
    flag = True
    i = 0
    while i < len(arr) - 2:
      if arr[i] > arr[i + 2]:
        arr[i], arr[i + 2] = arr[i + 2], arr[i]
        flag = False
      i += 1
    if flag:
      break

def tr_sorted(arr):
  i = 0
  while i < len(arr) - 2:
    if arr[i] > arr[i + 2]:
      return False
    i += 1
  return True

main()



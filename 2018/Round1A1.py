#Ben Carlson
import sys

def problem1():
    out = problem1_helper()
    for i in range(len(out)):
        print("Case #" + str(i + 1) + ": " + out[i])
    sys.stdout.flush()

def problem1_helper():
    cases = int(input())
    out = []

    for i in range(cases):
        R, C, H, V = input().split(' ')
        R, C, H, V = int(R), int(C), int(H), int(V)
        W = []
        for i in range(R):
            W.append(list(input()))
        cc = 0
        for i in range(R):
            for j in range(C):
                if W[i][j] == '@':
                    cc += 1 
        pieces = (H + 1) * (V + 1)
        if cc % pieces != 0:
            out.append('IMPOSSIBLE')
            continue
        cc_piece = cc // pieces

        flag = False
        for x in range(1, R):
            for y in range(1, C):
                if checkCuts(W, R, C, x, y, cc_piece):
                    out.append('POSSIBLE')
                    flag = True
                    break
            if flag:
                break
        if not flag:
            out.append('IMPOSSIBLE')
       
    return out

def checkCuts(W, R, C, row, col, cc_piece):
    cc = 0
    for i in range(row):
        for j in range(col):
            if W[i][j] == '@':
                cc += 1
    if cc != cc_piece:
        return False
    cc = 0
    for i in range(row, R):
        for j in range(col):
            if W[i][j] == '@':
                cc += 1
    if cc != cc_piece:
        return False
    cc = 0
    for i in range(row):
        for j in range(col, C):
            if W[i][j] == '@':
                cc += 1
    if cc != cc_piece:
        return False
    cc = 0
    for i in range(row, R):
        for j in range(col, C):
            if W[i][j] == '@':
                cc += 1
    if cc != cc_piece:
        return False
    return True

problem1()
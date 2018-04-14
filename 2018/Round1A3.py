#Ben Carlson
import sys
import math

def problem3():
    out = problem3_helper()
    for i in range(len(out)):
        print("Case #" + str(i + 1) + ": " + str(out[i]))
    sys.stdout.flush()

def problem3_helper():
    cases = int(input())
    out = []

    for i in range(cases):
        N, P = input().split(' ')
        N, P = int(N), int(P)
        C = []
        for i in range(N):
            dim = input().split(' ')
            dim[0], dim[1] = int(dim[0]), int(dim[1])
            dim.append(2 * dim[0] + 2 * dim[1])
            dim.append(min(2 * dim[1], 2 * dim[0]))
            dim.append(2 * math.sqrt(pow(dim[0], 2) + pow(dim[1], 2)))
            C.append(dim)
        out.append(dim)
        
        dim = C[0]
        cur_P = N * dim[2]
        count = 0
        while count < N and cur_P <= P - dim[4]:
            cur_P += dim[4]
            count += 1

        if count == N or cur_P == P:
            out.append(cur_P)
        elif cur_P <= P - dim[3]:
            out.append(P)
        else:
            out.append(cur_P)
       
    return out

problem3()
#Ben Carlson
import sys

def problem2():
    out = problem2_helper()
    for i in range(len(out)):
        print("Case #" + str(i + 1) + ": " + str(out[i]))
    sys.stdout.flush()

def problem2_helper():
    cases = int(input)
    out = []
    for i in range(cases):
        R, B, C = input().split(" ")
        R, B, C = int(R), int(B), int(C)
        cashiers = []
        for i in range(C):
            M, S, P = input().split(" ")
            M, S, P = int(M), int(S), int(P)
            cashiers.append([M, S, P])

        sols = gen_sols(R, B, C)
        least = pow(2, 63)
        for sol in sols:
        	best = min([cashiers[i][1] * sol[i] + cashiers[i][2] for i in range(cashiers)])
        	if best < least:
        		least = best
       	out.append(least)

    return out

def gen_sols():
	


problem2()



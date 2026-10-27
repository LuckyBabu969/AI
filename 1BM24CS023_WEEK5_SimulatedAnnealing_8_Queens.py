
import random
import math

def cost(s):
    n = len(s)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(s[i] - s[j]) == abs(i - j):
                c += 1
    return c

def print_board(s):
    n = len(s)
    for r in range(n):
        print(" ".join("Q" if s[c] == r else "_" for c in range(n)))

def simulated_annealing(n=8):
    s = list(range(n))
    random.shuffle(s)
    c = cost(s)

    print("Initial State:", s)
    print("Initial Board:")
    print_board(s)
    print("Initial Cost:", c)

    t = 1.0
    rate = 0.995
    steps = 0
    limit = 1000000

    while c > 0 and steps < limit:
        a, b = random.sample(range(n), 2)
        ns = s.copy()
        ns[a], ns[b] = ns[b], ns[a]

        nc = cost(ns)
        d = nc - c

        if d < 0 or random.random() < math.exp(-d / t):
            s = ns
            c = nc

        t *= rate
        if t < 0.000001:
            t = 1.0
        steps += 1

    if c == 0:
        print("\nFinal State:", s)
        print("Final Board:")
        print_board(s)
        print("Final Cost:", c)
        print("Steps:", steps)
    else:
        print("\nNo solution found within the step limit.")

    return s

result = simulated_annealing(8)

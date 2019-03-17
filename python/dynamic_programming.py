# cut-rod from CLRS
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

# memoized cut_rod -- top-down dynamic programming solution
def cut_rod2(p, n):
    r = [-1 for _ in range(0, n + 1)]
    def helper(n):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = -1
            for i in range(1, n + 1):
                q = max(q, p[i] + helper(n - i))
        r[n] = q
        return q
    return helper(n)

# cut_rod top-down dynamic programming solution
def cut_rod3(p, n):
    r = [-1 for _ in range(0, n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

# cut_rod top-down solution with optimal size of first cut
def cut_rod_solution(p, n):
    r = [-1 for _ in range(0, n + 1)]
    s = [-1 for _ in range(0, n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return (r, s)

# generates optimal solution from previous method
def print_cut_rod_solution(p, n):
    r, s = cut_rod_solution(p, n)
    while n > 0:
        print(s[n], end=' ')
        n = n - s[n]
    print()

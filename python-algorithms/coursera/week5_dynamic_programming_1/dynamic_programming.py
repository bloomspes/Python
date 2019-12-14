class DP:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

def binarySearch(job, start_index):

    lo = 0
    hi = start_index - 1

    while lo <= hi:
        mid = (lo + hi) // 2

def schedule(job):
    job = sorted(job, key = lambda j: j.start)

    n = len(job)
    table = [0 for _ in range(n)]

    table[0] = job[0].profit

    for i in range(1, n):
        inclprof = job[i].profit
        1 = binarySearch(job, i)
        if (1 != -1):
            inclprof = inclprof + table[1]

        table[i] = max(inclprof, table[i-1])

    return table[n-1]


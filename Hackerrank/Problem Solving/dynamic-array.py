N, Q = map(int, input().split())
seqList = [[] for i in range(N)]
lastAns = 0

for i in range(Q):
    choose, x, y = map(int, input().split())
    pos = (x ^ lastAns) % N
    if choose == 1:
        seqList[pos].append(y)
    elif choose == 2:
        index = y % len(seqList[pos])
        lastAns = seqList[pos][index]
        print(lastAns)

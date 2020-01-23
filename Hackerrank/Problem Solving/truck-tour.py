n = int(input())
bunks = [tuple(map(int, input().split())) for _ in range(n)]
pos = 0
for i in range(n):
    fuel_remaining = 0
    for j in range(n):
        fuel_remaining += bunks[(j+pos) % (n)][0]
        fuel_remaining -= bunks[(j+pos) % (n)][1]
        if(fuel_remaining < 0):
            pos += 1
            break
    if(j >= n-1):
        print(i)
        break

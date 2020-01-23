n, m = map(int, input().split())
arr = [0]*n
for _ in range(m):
    q = list(map(int, input().split()))
    for i in range(q[0]-1, q[1]):
        arr[i] += q[2]
print(max(arr))

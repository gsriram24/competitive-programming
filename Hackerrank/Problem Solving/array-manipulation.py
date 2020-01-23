n, m = map(int, input().split())
arr = [0]*n

for _ in range(m):
    q = list(map(int, input().split()))
    # for i in range(q[0]-1, q[1]):
    #     arr[i] += q[2]
    arr[q[0]-1] += q[2]
    if q[1] != len(arr):
        arr[q[1]] -= q[2]
sum1 = 0
max1 = 0
for i in arr:
    sum1 += i
    max1 = max(max1, sum1)
print(max1)

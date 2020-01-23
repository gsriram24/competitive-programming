n, d = map(int, input().split())
arr = list(input().split())
print(' '.join(arr[d:]) + ' ' + ' '.join(arr[:d]))

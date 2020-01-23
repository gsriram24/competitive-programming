n = int(input())
arr = list(map(int, input().split()))
result = 0
stack = []
for i in arr:
    while(len(stack) > 0):
        result = max(result, stack[-1] ^ i)  # Simplified boolean expression
        if(i < stack[-1]):
            stack.pop()
        else:
            break
    stack.append(i)
print(result)

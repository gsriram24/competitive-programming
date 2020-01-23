numStrings = int(input())
strings = [input() for _ in range(numStrings)]
numQueries = int(input())
queries = [input() for _ in range(numQueries)]
for i in queries:
    print(strings.count(i))

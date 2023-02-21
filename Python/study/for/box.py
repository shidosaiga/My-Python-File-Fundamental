m = int(input())

for i in range(m):
    for j in range(m):
        print('#' if i in [0, m-1] or j in [0, m-1] else ' ', end='')
    print()
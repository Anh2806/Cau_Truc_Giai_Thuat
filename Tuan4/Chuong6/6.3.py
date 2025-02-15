def count_bdn(N):
    count = 0
    for i in range(1, N):
        if all(c in '01' for c in str(i)):
            count += 1
    return count
T = int(input())
for _ in range(T):
    N = int(input())
    print(count_bdn(N))
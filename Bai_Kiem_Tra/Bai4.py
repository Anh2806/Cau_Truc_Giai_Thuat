def levenshtein_distance(token1, token2):
    distances = [[0]*(len(token2)+1) for i in range(len(token1)+1)]
    for ti in range(len(token1)+1):
        distances[ti][0] = ti
    for t2 in range(len(token2)+1):
        distances[0][t2] = t2
    a = 0
    b = 0
    c = 0
    for t1 in range(1, len(token1)+1):
        for t2 in range(1, len(token2)+1):
            if token1[t1-1] == token2[t2-1]:
                distances[t1][t2] = distances[t1-1][t2-1]
            else:
                a = distances[t1][t2-1]
                b = distances[t1-1][t2]
                c = distances[t1-1][t2-1]
                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    return distances[len(token1)][len(token2)]
assert levenshtein_distance("kitten", "sitting") == 3
print(levenshtein_distance("kitten", "sitting")) # 3
S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

print('\n', S, sep='')

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=' ')

print('\n', L, sep='')

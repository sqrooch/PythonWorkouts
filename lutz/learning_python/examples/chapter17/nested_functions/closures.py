def maker(N):
    def action(X):
        return X ** N

    return action


print(maker(2)(3))
print(maker(2)(4))
print(maker(3)(3))
print(maker(3)(4))

# или

f = maker(2)
print(f(3))
print(f(4))

g = maker(3)
print(g(3))
print(g(4))

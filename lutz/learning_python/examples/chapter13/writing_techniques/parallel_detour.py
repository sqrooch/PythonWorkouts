keys = ['spam', 'eggs', 'toast']
values = [1, 3, 5]
D = dict(zip(keys, values))
print(D)

DD = {k: v for (k, v) in zip(keys, values)}
print(DD)

line = 'The knights who say Ni!\n'
sub = 'Ni!\n'
print(line.endswith(sub))
print(-len(sub))
print(line[-6:])
print(line[-len(sub):] == sub)

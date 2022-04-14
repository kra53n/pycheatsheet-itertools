import itertools

dignities = [*map(str, range(1, 11)), 'валет', 'дама', 'король', 'туз']
suits = ['пики', 'трефы', 'черви', 'бубны']

print(*(itertools.product(suits, dignities)))

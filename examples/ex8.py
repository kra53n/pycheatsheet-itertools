import itertools
import csv

variables = 'a b c d e'
func = 'not(a + b) * (c + e) <= d * b'

with open("test.csv", 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(variables.replace(' ', '') + 'f')

    for row in itertools.product('01', repeat=len(variables.replace(' ', ''))):
        exec(f'{variables.replace(" ", ", ")} = map(int, row)')
        writer.writerow([*row] + ['1' if eval(func) else '0'])

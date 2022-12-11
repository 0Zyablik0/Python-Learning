values = (1, 2, (3, 4, 5), 6 , (7, 8))

_, _, (three, _, five), six, (seven, _) = values
print(three, five, six, seven)

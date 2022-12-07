x_list = [1, 2, 4, 5]
y_list = [-1, -2, -3]

product = [(x, y) for x in x_list for y in y_list]
print(product)
gen = (i**2 for i in range(10))
print(type(gen), gen)

gen_tuple = tuple(gen)
print(gen_tuple)
coordinates = (33.222344, 12.423405)
latitude, longitude = coordinates  # unpacking
print(f"latitude is {latitude}")
print(f"longitude is {longitude}")

# --------------------------------
a, b = 1, 2
b, a = a, b  # swap
print(f"a = {a}, b = {b}")

# --------------------------------
# unpacking of function arguments
args = (10, 9)
quotient, remainder = divmod(*args)
print(f"quotient = {quotient}, remainder = {remainder}")


# --------------------------------
# grab excess items:

a, b, *rest = range(5)
print(f"a = {a}, b = {b}, rest = {rest}")

a, b, *rest = range(3)
print(f"a = {a}, b = {b}, rest = {rest}")

a, b, *rest = range(2)
print(f"a = {a}, b = {b}, rest = {rest}")

a, *center, c, d = range(5)
print(f"a = {a}, center = {center}, c = {c}, d = {d}")

*begin, b, c, d = range(5)
print(f"begin = {begin}, b = {b}, c = {c}, d = {d}")


# ------------------------------

example = [*range(5), 5, 6, *range(3, 10)]
print(example)

example = {*range(5), 5, 6, *range(3, 10)}
print(example)

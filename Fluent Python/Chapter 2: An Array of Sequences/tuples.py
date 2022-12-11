### Tuples as records:

coordinates = (33.9424, -118.408056) ## Tuple as record of coordinates 
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", '12345'), ("RUS", '12321'), ("UK", '923421')] 


### Tuples as immutable lists:

a = (10, "alpha", [1, 3])##only references are immutable
b = (10, "alpha", [1, 3])
print(a == b)
a[-1].append(28)
print(a == b)
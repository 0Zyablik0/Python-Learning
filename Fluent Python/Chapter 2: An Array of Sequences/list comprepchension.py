symbols = 'alsudhfkjlcsaisdj'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
    
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)



codes = [ code := ord(symbol) for symbol  in symbols if ord(symbol) > 100]
print(codes, code)
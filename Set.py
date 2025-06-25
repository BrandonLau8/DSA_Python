s = {1,2,3}

print(2 in s)
for item in s:
    print(item)
    

s.add(4)
s.update([5,6])

s.remove(2)
s.discard(10)

element = s.pop()
print(element)

# s.clear()

# del s

# a = {1, 2, 3}
# b = {3, 4 ,5}

# print(a | b)

# print(a & b)

# print(a - b)

# print(a ^ b)
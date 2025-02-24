a = "123"
b = 456
c = int(a) + b
print(c)

abc = "With three words"
stuff = abc.split()
print(len(stuff))

x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value > x :
        x = value
print(x)

total = 0
for abc in range(5):
    total = total + abc
print(total)
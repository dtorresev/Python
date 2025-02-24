import re
count = 0
#fname = "regex_sum_42.txt"
fname = "regex_sum_2047984.txt"
total = 0
fh = open(fname)
lst = []

for lines in fh:
    numbers = re.findall('[0-9]+', lines)
    for n in numbers:
        if int(n) > 0:
            lst.append(n)

for x in lst:
    total = total + int(x)
    count = count +1

print(lst)
print(total)
print(count)


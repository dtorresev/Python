# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the 'From' 
# line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by 
# hour as shown below.

fname = "mbox-short.txt"
counts = dict()

if (len(fname) < 1) :
    fname = "mbox-short.txt"

fh = open(fname)

for lines in fh:
    lines = lines.rstrip()
    if lines.startswith("From:"):
        continue
    else: 
        if lines.startswith("From"):
            words = lines.split()
            time = words[5]
            hour = time[0:2]
             #print(hour)
            if hour not in counts:
                counts[hour] = 1
            else: 
                counts[hour] = counts[hour] +1

for k,v in sorted(counts.items()):
    #tup = (k,v)
    #print(tup)
    print(k,v)

fh.close()

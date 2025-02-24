 # Write a program that prompts for a file name,
 # then opens that file and reads through the file, 
 # looking for lines of the form: 
 # X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point 
# values from each of the lines and compute the average 
# of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution

#fname = input("Enter file name: ")
fname = "mbox-short.txt"
count = 0
total = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else: 
        raw = float(line.lstrip("X-DSPAM-Confidence:"))
        count += 1
        total += raw
    #print(line)
    #print(raw)
#print(suma)
#print(count)
print("Average spam confidence:", total/count)
#print("Done")

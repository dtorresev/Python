# Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
# number of mail messages. The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program creates a Python dictionary that 
# maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.

fname = "mbox-short.txt"
counts = dict()
largest = None
max_email = None

if len(fname) < 1:
    name = "mbox-short.txt"

fh = open(fname)

for lines in fh:
    if lines.startswith("From:"):
        continue
    else:
        if lines.startswith("From"):
            words = lines.split()
            email_address = words[1]
            if email_address not in counts:
                counts[email_address] = 1
            else: 
                counts[email_address] = counts[email_address] +1

for address, item in counts.items():
    if largest is None or item > largest:
        largest = item
        max_email = address

print(max_email, largest)
fh.close()
text = "X-DSPAM-Confidence: 0.8475"
pos_in  = text.find(' ')
#print(pos_in)
num_str  = text[pos_in+1:]
print(float(num_str))

"""#!/usr/bin/python"""

current_state = 0
next_state = 0
signal = 0
""""
if __name__ == "__main__":
    while(signal!=3):
        signal = int(input('sign (1-short 2-long 3-end)'))
        if current_state == 0:
            if signal == 1:
                next_state = 1
            elif signal == 2:
                next_state = 2
        
        current_state =next_state
        print(next_state) """

while(signal!=3):
    signal = int(input('sign (1-short 2-long 3-end)'))
    if current_state == 0:
        if signal == 1:
             next_state = 1
        elif signal == 2:
            next_state = 2
    
    current_state =next_state
    print(next_state)






 

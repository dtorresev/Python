largest = None
smallest = None

while True:
    input_str = input("Enter a number: ")
    
    if input_str == "done":
        break
    
    try:
        input_num = int(input_str)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None or input_num > largest:
        largest = input_num
    if smallest is None or input_num < smallest:
        smallest = input_num

print("Minimum", smallest)
print("Maximum", largest)
num_sum = 0
product = 1

num = raw_input("Please enter a number or STOP: ")

while num != "STOP":
    num_sum += int(num)	#have to do the conversion here
    product *= int(num)
    num = raw_input("Please enter a number or STOP: ")

operation = raw_input("Please enter an operation ('+' or '*'): ")

if operation == "+":
    print "The total sum is", num_sum
else:
    print "The total product is", product

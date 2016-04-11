num_sum=0
num_multi=1
num=raw_input("Enter the number you want to perform the mathematical operations on or STOP: ")
while num!="STOP":
    num_sum+=int(num)
    num_multi*=int(num)
    num=raw_input("Enter the number you want to perform the mathematical operations on or STOP: ")

operation=raw_input("Enter an operation ('+' or '*'):")
if operation=="+":
    print "Total sum is: ",num_sum
else:
    print "Total multi is: ",num_multi
        
    
    
    

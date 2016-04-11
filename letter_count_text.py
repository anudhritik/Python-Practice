text=raw_input("Enter the text: ")
letter=raw_input("Enter the letter: ")
count =0
for ch in text:
    if(ch.lower()==letter.lower()):
        count+=1
print "Letter" ,"was found",count, "times in text"

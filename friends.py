friends = []
while True:
    friends.sort()
    print "Current Friend's List"
    if len(friends)>0:
        for person in friends:
            print person
    else:
        print "No one!"
    print "\n"
    new_name=raw_input("Please enter a friend's name or STOP: ")
    if new_name=="STOP":
        break
    if new_name in friends:
       print new_name, "is already on your Friends List!"
       remove=raw_input("Would you like to remove this friend (Y/N)")
       if remove.upper()=="Y":
           friends.remove(new_name)
    else:
        friends.append(new_name)








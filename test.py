scores = [("Joe", 200, "A"), ("Bill", 180, "B"), ("Mary", 215, "C")]

for i in range(len(scores)):		#The outer loop defines rows
    for j in range(len(scores[i])): 	#The inner loop, columns
        print "\t", "(i=" + str(i) + ")",
        print "(j=" + str(j) + ")", scores[i][j],
    print

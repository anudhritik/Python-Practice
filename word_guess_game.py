secret_word=raw_input("Please enter the secret word")
#setting up the game
display=""
used=""
moves=0
for letter in secret_word:
    if letter!="":
        display+="_"
    else:
        display+=""

while True:
    print "The board", display
    print "Your used letters", used
    print "Number of moves", moves
    guess = raw_input("What's your guess?")

    new_display=""
    for i in range(len(secret_word)):
        if secret_word[i]==guess:
            new_display+=guess
        else:
            new_display+=display[i]
    display=new_display
    used+=guess
    moves+=1
    if secret_word==display:
        print "You guessed in" , moves, "moves"
        break




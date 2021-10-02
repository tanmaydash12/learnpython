# guess a number .Take user input and dispaly if its more or less .only 5 guesses are allowed .

# real number 
myRealNum = 26 

# check if its greater or smaller . can only guess 5 times . if guess completed game over .
# if correct congrats . output :1)  more or less 2)  number of guesses left 
numberOfGuesses = 5
while(numberOfGuesses > 0):
    # take input 
    print("Enter your guessing number")
    guessedNum = int(input())

    if guessedNum > myRealNum:
        print("Your guess is greater")
    elif(guessedNum < myRealNum):
         print("Your guess is lesser")
    else:
        print("Congrats you have won!!!")
        break
      
    numberOfGuesses = numberOfGuesses - 1
    print("You have ", numberOfGuesses, "guesses left")

if numberOfGuesses == 0: 
    print("game over")
#User guesses the secret word
#Accepts input from user
#Compares the input to the secret word
#If the guess and secret words are same, print success message
#Allow a maximum of three guesses
#If the user gives three guesses unsuccessfull, print a fail message

secret_word = "Antelope"
guess = ""
guess_count=0
guess_over=False
while secret_word != guess and guess_over == False:
    guess = input("Enter guess word: ")
    guess_count +=1
    if guess_count >2:
        guess_over = True
        print("You lost the game!")
print("Correct!")
#User guesses the secret word
#Accepts input from user
#Compares the input to the secret word
#If the guess and secret words are same, print success message
#Allow a maximum of three guesses
#If the user gives three guesses unsuccessfull, print a fail message

secret_word = "Antelope"
guess_attempt = 3
right = False

while guess_attempt ==0 and right==True:
   guess_word= input("Enter guess word: ")
    guess_attempt -=1
    if guess_word == secret_word:
        print("You are absolutely correct!")
        right = True
    else:
        print("You lost!")
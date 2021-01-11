#Import class that defines the traits of question and answer
#Predefine an array of questions with corresponding answers
#Accept user input
#Validate correctness of input against answer
#Update score
#Print score against total
from multiplechoice_class import Multiple
questions_prompts = [
        "What is the color of milk?\n (a)Red \n (b) Green \n (c) White \n",
        "Which programming language is this? \n (a)C++ \n (b) Java\n (c) Javascript \n (d) Python \n ",
        "Which of the following is not owned by Mark Zuckerberg? \n (a) Twitter \n (b) Facebook \n (c) Instagram \n (d) WhatsApp \n "
    ]
questions = [
        Multiple(questions_prompts[0], "c"),
        Multiple(questions_prompts[1], "d"),
        Multiple(questions_prompts[2], "a")
    ]
def implementation(questions):
     score = 0
     for questions in questions:
         answer = input(questions_prompts)
         if answer == questions.answer:
             score +=1
         else:
            score = score
     print("Your score is " + str(score) + " out of the possible " + str(len(questions)) + ".")
implementation(questions)
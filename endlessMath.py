#generate number of questions based on user input
#if usr_answer == sys_answer, move onto next question, else stay on question

#import random number function
import random

#allow user to set boundaries
highValue = int(input("What is the highest number you wish to work with?"))
lowValue = int(input("What is the lowest number you wish to work with?"))
qn_no = int(input("How many questions would you like generated?"))

#create multiple math question with answers
def question(qn_no):
    for qn in range(qn_no):
        #generate random integers using user input
        num1 = random.randint (lowValue, highValue)
        num2 = random.randint (lowValue, highValue)

        #logic to generate questions and answers
        if num1>num2:
            print("Q"+str(qn+1)+":", num1, "-", num2, "=",)
            sys_ans = num1-num2
            answer(sys_ans)
        
        else:
            print("Q"+str(qn+1)+":", num1, "+", num2, "=",)
            sys_ans = num1+num2
            answer(sys_ans)

    print("Congratulations! You have answered all questions correctly.")

#let user input answers, match answers to logic
def answer(sys_ans):
    usr_ans = int(input ("Input your Answer:"))
    if usr_ans != sys_ans:
        print("Incorrect Answer. Please Try Again")
        usr_ans = input ("Input Answer:")

    else:
        return True
    
#run Programme
question(qn_no)
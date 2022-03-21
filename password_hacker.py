
import random
from tkinter import *




def RandomCode(digits):
    code = []
    for x in range(digits - 1):
        num = random.randint(1,9)
        code.append(num)
    while num in code:
        num = random.randint(1,8)
        code.append(num)
        break
    mapTostr = map(str, code)
    code = "".join(mapTostr)
    return code

def user_name():
    user_INput = input("Hello please enter Your Name: ")
    
    if user_INput == "":
        print("Okay THats Weird never heard of someone without a name before!")
    elif user_INput.isdigit() == True:
        print("Why does your name a number, thats weird did your parents not love you, or is your father elon")
    else:
        print("Welcome "+ user_INput)

def check_correctness(guess,code):
    correctDigit = "*"
    correctDigitInCorrectPlace = "*"
    for x in range(len(code)):
        if guess[x] == code[x]:
            correctDigit += "*"
        elif guess[x] != code[x] and guess[x] in list(code):
            correctDigitInCorrectPlace += "*"
    return correctDigit, correctDigitInCorrectPlace



# def number_of_digits():

#     digits = int(input("please enter the amount of digits you want in your code: "))
#     return digits

def user_input__vlaidation(digits,code):
        
        while True:
            guess = input(f"please enter the {digits} code: ")
            if guess.isdigit() == False or guess == "" or len(guess) != len(code):
                print("please Enter valid input: ")
            else:
                return False, guess
        

def Run_Code(guess):
    
    # chances = 12
    # digits = 4
    code = RandomCode(4)
    # while chances >= 0:
    # do_next, guess = user_input__vlaidation(digits,code)
    if guess == code:
        acess ="Access Granted"
        fbi = "Looks like someone should be added to the FBI most wanted list"
        return acess, fbi
    elif guess != code:
        correctDigit,incorrect = check_correctness(guess,code)
        correct = f"number of correct digits in correct place {correctDigit}"
        incoreect = f"number of correct digits not in correct place {incorrect}"
        change = "Looks like Someone should consider a career change"
        return correct, incoreect
def click():
    entered_text = textentry.get()
    output.delete(0.0,END)
    # try:
    definition,x1= Run_Code(entered_text)
    output.insert(END,definition,x1)

    # except:
    #     definition = "Access Denied"
    #     output.insert(END,definition)

    






window = Tk()
window.title("Bank Code Hacker")
window.configure(background="black")
logo = PhotoImage(file="ab-logo_icon_blue_30x30-2.png")
width = 20
height = 20
Label(window,image=logo).grid(row=0,column=0,sticky=W)
Label(window, text="Welcome To Union Bank", bg="black", fg="white", font= "none 12 bold").grid(row=1, column =0,sticky=W) 
Label(window, text="Please Enter Your pin Code: ",bg="black",fg="white",font="none 12 bold").grid(row=2, column=0,sticky=W)
Label(window, text="Correctness Of 4 Digit Code:",bg="black",fg="white",font="none 12 bold").grid(row=6, column=0,sticky=W)
textentry =Entry(window,width=29,bg="white")
textentry.grid(row=3, column=0,sticky=W)
Button(window, text = "Enter", width=6, command=click).grid(row=4,column=0, sticky=W)
Button(window, text="Cancel", width=6,command=click).grid(row=5,column=0,sticky=W)
output = Text(window, width=30, height=2, wrap=WORD, background="White")
output.grid(row=7,column=0,columnspan=1,sticky=W)
window.mainloop()
click()
        






    





        

        

            
        

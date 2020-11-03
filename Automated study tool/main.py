


###########

# In main: Flow: 1.Print Question 2. use <while> askQuestion(q,a)  3. Turn left and false to default status
# Notice: global variables have to be restated in each def function

# The way python run code: 1. Everything other than functions ( def and main) ie. from the top   2. main function
# In this case, while loop operate in the main function, so askQuestion is repeated, and variables in this function change
# ie, the change of score happen inside the askQuestion other than the global variable outside. 





########


# project: p4
# submitter-netid: yzhou344
# partner-netid: none

false=1

times=input("How many tries do you want for each question:")
times=int(times)
left=times

total_q=3
score=total_q


def  askQuestion(q,a, hint="check the textbook"):
    global false
    global times
    global left
    global score
    global total_q
    input1=input("Your answer:")
                
    input_final=str.strip(str.lower(input1))

    if input_final==a:
        print("\nCongratulations! You got it right.")
        
        false=0
    elif left==2:
        left=left-1
        print("\n"+hint)
        
        
        print("You have this many remaining tries:", left)

        
    elif left==1:
        left=left-1
        score=score-1
        print("\nYou answered '"+input1+"'. The correct answer is "+"'"+ a+"'.")
        
        print("You have this many remaining tries:", left)
        
        



    else: 
        left=left-1
        print("\nYou answered '"+input1+"'. The correct answer is "+"'"+ a+"'.")
        
        print("You have this many remaining tries:", left)
            


def main():
    global false
    global times
    global left
    global score
    global total_q
    
    q1="\n What is the type of the following? \"1.0\" + \"2.0\"\n a) int \n b) float \n c) str \n d) bool \n e) NoneType"
    print (q1)

    while (left>0 and false==1):
        askQuestion(q1,"c")

        
# the following turns false and left to the original status
    false=1
    left=times

    q2="\n What is the type of the following? \"1\" * 2"
    print(q2)
    
    
    while (left>0 and false==1):
        askQuestion(q2,"str","notice the quotes!")


    false=1
    left=times

    q3="\n What does this expression evaluate to? \n True != (3 < 2)"
    print(q3)

    while(left>0 and false==1):
        askQuestion(q3,"true","Calcuate the right side first. Don't forget != means not equal to.")



    print("You tried 3 questions and got", score, "right.")

    






















if __name__ == '__main__':
    main()







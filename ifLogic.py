def main():
    gameRunning = True
    might = 0
    print("Hello Welcome to the Game - 'Test your Might' inspired by Mortal Kombat\n", "Answer the questions below to build your might and break the brick")
    while gameRunning:
        
        question1 = input("Choose your character: 1 for Scorpion, 2 for Sub-Zero, 3 for Jax, and 4 for Cassie Cage\n")
        if question1 == "1":
            print("Get over here!")
            might += 4
        elif question1 == "2":
            print("Whats cooler than being cool,  Ice Cold!")
            might += 4
        elif question1 == "3":
            print(" Got'cha")
            might += 5
        elif question1 == "4":
            might += 4
        else:
            might += 1
        print(f"current might is {might}")

        question2 = input("What year was mortal kombat released? A for 1990, B for 1992, C for 1988\n").strip().lower()    
        if question2 =="A".lower():
            print("incorrect, nice guess tho")
            might += 1
        elif question2 == "B".lower():
            print("Correct!")
            might += 5
        else:
            print("incorrect input. You gained 0 might")
            might += 0
        print(f"current might is {might}")
        
        question3 = input("What is the finisher in mortal kombat called?\n").strip().lower()
        if question3 == "Fatality".lower():
            print("Correct! Finish him/her!!!")
            might += 5
        else:
            print("Incorrect, You've been finished!")
            might += 0
        
        if might >= 11: # current mortal kombat game iteration
            print("Congratulations, You Win!")
            gameRunning = False
        else:
            print("You lose, try again")
            gameRunning = False

main()

import random
uAge = int(input("Please enter your age:"))
uMoney = 5000
if uAge > 17 and uAge < 60:
    print("==== Welcome to the MILLIONAIRE game ====")
    print("First, we will hide a random 2-digit number between 10 and 99, and you have to guess it.")
    print("Each time you play, you have to bet $1000.")
    print("If you win, you will get 20 times the amount you bet!")
    print("Here are the rules you need to know before playing the game:")
    print("Rule No.1 >> We will give you $5000 to start with.")
    print("Rule No.2 >> Every time you play, you have to bet at least $500.")
    print("Rule No.3 >> If you don't have any money left, the game is over.")
    print("Rule No.4 >> Any money you win over $5000 is yours.")
    print("Rule No.5 >> You can add 1-5 lucky numbers.")
    print("Let's start right now!")

    while uMoney > 499:
        randomNum = random.randint(10,99)
        print(randomNum)
        lquan = int(input("How many lucky numbers do you want to add? (Enter a number between 1 and 5):"))
        i = 0
        luckyNumber = []
        amount = []
        if lquan <= 5:
            while i < lquan:
                if uMoney > 499:
                    print("Enter your lucky number for lucky number {}".format(i+1))
                    luckyNumber.append(int(input("Enter a number between 10 and 99:")))
                    amount.append(int(input("Enter how much you want to bet (minimum $500):")))
                    if amount[i] < uMoney + 1:
                        if amount[i] > 499:
                            uMoney -= amount[i]
                            i += 1
                            print("You now have ${} left to bet.".format(uMoney))                        
                        else:
                            print("Rule No.2 >> Every time you play, you have to bet at least $500.")
                    else:
                        print("You don't have enough money to make that bet. Please choose another amount.")
                        luckyNumber.pop(i)
                        amount.pop(i)
                else:
                    break
        else:
            print("Rule No.4>>You can add 1-5 lucky Numbers")
            continue
        
        print("Random Number is ===>",randomNum)
        
        i = 0;
        while i < len(luckyNumber):
            if luckyNumber[i] == randomNum:
                amount[i] *= 20
                uMoney += amount[i]
                print("Congratulations! Your lucky number {} from list {} matched the random number {}!".format(luckyNumber[i],i+1,randomNum))
                print("You have got $",amount[i])
                break
            else:
                print("You lose")
                print("Sorry! Your lucky number {} from list {} did not match the random number {}!".format(luckyNumber[i],i+1,randomNum))
            i+=1
            
        if uMoney > 5000:
            print("After deducting the initial $5000, you now have {}.".format(uMoney-5000))
            option = input("Would you like to Quit now: press 'y' to quit and 'n' to stay.\nEnter:")
            if option == 'y':
                print("Thank you for playing the Game of Fortune! We hope to see you again soon.")
                break
            elif option == 'n':
                print("Okay, let's continue playing!")       
                i = 0
                while i < len(amount):
                    luckyNumber.pop(i)
                    amount.pop(i)
                    
    if uMoney < 499:
        print("Sorry, you have run out of money.")
        print("Rule No.3 >> If you don't have any money left, the game is over.")
elif uAge >= 60:
    print("You are too old now")
elif uAge < 18:
    print("Sorry...you are too young! Try again after {} years later".format(18-uAge))


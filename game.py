import random
uAge = int(input("Please enter your age:"))
uMoney = 5000
if uAge > 17 and uAge < 60:
    print("====Welcome to ``MILLIONAR`` game====")
    print("Here is some rules you need to know before play the game")
    print("Rule No.1>>We will give you only 5000$")
    print("Rule No.2>>Everytime you play, you have to use at least 500$")
    print("Rule NO.3>>If you don't have any money, game is over")
    print("Rule No.4>>Money over 5000$ is yours")
    print("SO, Every one can be the MILLIONAR\nLet's get start....")
    print("Wait! how do we play the game and what is the game to be a MILLIONAR")
    print("Game is very simple")
    print("We will hide a random  2 digits  which is  between 10 and 99 and you have to guess it")
    print("Each time you play you  have to use 1000$")
    print("If you win you will get 20 times of your money charged")
    print("Let's get start rignt now")
    while uMoney > 499:
        randomNum = random.randint(10,99)
        luckyNumber = int(input("\n\nEnter your Lucky Number:"))
        amount = int(input("Enter how many amount you want to charge?\nEnter:"))
        if amount < uMoney + 1:#uMOney <
            if amount > 499:#amount >
                uMoney -= amount
                print("Random Number is ===>",randomNum)
                if luckyNumber == randomNum:#luckyNum 4
                    amount *= 20
                    uMoney += amount
                    print("You win!!!!")
                    print("You have got $",amount)
                    if uMoney > 5000:
                        print("After -5000$ Your money is  $",uMoney - 5000)
                        option = input("Would you like to Quit now: press 'y' to quit and 'n' to stay.\nEnter:")
                        if option == 'y':
                            print("Thank you for your attention..See you soon")
                            break 
                        elif option == 'n':
                            print("OKAY, let's dig more and more")
                else:#lucky number
                    print("You lose")
                    print("You left $",uMoney)
            else:#amount 3
                print("Rule No.2>>Everytime you play, you have to use at least 500$")
                print("You kill this time")
        else:#uMoney <
            print("How stupid><You charge more than you have")
    if uMoney < 499:
        print("Rule NO.3>>If you don't have any money, game is over")#while break
elif uAge > 60:
    print("You are too old now")
else:#age
    age = 18-uAge
    print("Sorry...you are too young! See you soon after {} years later".format(age))

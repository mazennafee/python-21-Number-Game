#21 Number Game in python
# ask player if he will paly first or second
turn = input("Enter 1 to play first or 2 to play second: ")
# check if player entered any value other than 1 or 2
if turn != "1" and turn != "2":
    print("you entered wrong value see you next time! ")
    exit()
# list to add inputs to it
nums = []
j = 1
# create loop so game will continue to the end 
while True:
    # check who play first to start
    if turn == "1":
        # if player will start ask him for input
        x = input("Enter your number: ")
        #check is the number
        try:
            x = int(x)
        except Exception:
            print("you entered wrong value see you next time! ")
            exit()
        nums.append(x)
        if nums[-1] == 21:
            print("Good luck next time")
            exit()
        elif x in nums:
            if nums.count(x) >1:
                print("Good luck next time")
                exit()
        comp = x + 1
        nums.append(comp)
        if nums[-1] == 21:
            print("You won the game")
            exit()
        print(nums)
    else:
        comp = j
        nums.append(comp)
        if nums[-1] == 21:
            print("You won the game")
            exit()
        print(nums)
        x = input("Enter your number: ")
        #check is the number
        try:
            x = int(x)
        except Exception:
            print("you entered wrong value see you next time! ")
            exit()
        nums.append(x)
        if nums[-1] == 21:
            print("Good luck next time")
            exit()
        elif x in nums:
            if nums.count(x) >1:
                print("Good luck next time")
                exit()
        print(nums)
        j = x + 1
        

#23
guess=10
correct_guess=""
while correct_guess!=guess:
    correct_guess=int(input("Enter your guess"))
    if correct_guess!=guess:
        print("try again")
    else:
        print("correct!!!")

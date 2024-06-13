if Guess in fruit:
    for i in range(len(fruit)):
        if Guess == list[i]:
            print("n")
            pass
    print("_" * len(Fruit))
    Guess = input("Guess the single letters from fruit: ")
else:
    attempts -= 1
    print(f"you have {attempts} attempts left")
    if attempts == 5:
        print("+----+----")
        print("|\n|\n|\n|\n|  /" + "\n|")
        print("_____________")
        continue
    elif attempts == 4:
        print("+----+----")
        print("|\n|\n|\n|\n|  / \ \n|")
        print("_____________")
        continue
    elif attempts == 3:
        print("+----+----")
        print("|\n|\n|\n|  /" + "\n|  / \ \n|")
        print("_____________")
        continue
    elif attempts == 2:
        print("+----+----")
        print("|\n|\n|\n|  / \ \n|  / \ \n|")
        print("_____________")
        continue
    elif attempts == 1:
        print("+----+----")
        print("|\n|\n|\n|  /|\ \n|  / \ \n|")
        print("_____________")
        continue
    else:
        print("+---+----")
        print("|   |\n|   |\n|   O\n|  /|\ \n|  / \ \n|")
        print("_____________")
    continue

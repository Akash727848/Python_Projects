import random
import warnings
warnings.filterwarnings('ignore')
Fruits=["apple","banana","grapes","mango","gauva","cherry"]
Fruit=random.choice(Fruits)
fruit=list(Fruit)
attempts=6
print("Hey Guess the fruit\nYou only have 6 attempts")
display=[]
for i in range(len(Fruit)):
    display += '_'
display=''.join(display)
print(display)
display=[i for i in display]
game_over=False
while not game_over:
    if '_' not in display:
        print("You Won")
        game_over = True
    else:
        Guess = input("Guess the single letters from fruit: ") #p  _pp__
    for position in range(len(Fruit)): #0 1 2 3 4
        letter = Fruit[position]
        if Guess == letter:
            display[position] = Guess
            display=''.join(display)
            print(display)
            display=[i for i in display]
    if Guess not in Fruit:
        attempts-=1
    if game_over != True:
        if attempts == 5:
            print(f"You only have {attempts} attempts")
            print("+----+----")
            print("|\n|\n|\n|\n|  /" + "\n|")
            print("_____________")
        elif attempts == 4:
            print(f"You only have {attempts} attempts")
            print("+----+----")
            print("|\n|\n|\n|\n|  / \ \n|")
            print("_____________")
        elif attempts == 3:
            print(f"You only have {attempts} attempts")
            print("+----+----")
            print("|\n|\n|\n|  /" + "\n|  / \ \n|")
            print("_____________")
        elif attempts == 2:
            print(f"You only have {attempts} attempts")
            print("+----+----")
            print("|\n|\n|\n|  / \ \n|  / \ \n|")
            print("_____________")
        elif attempts == 1:
            print(f"You only have {attempts} attempts")
            print("+----+----")
            print("|\n|\n|\n|  /|\ \n|  / \ \n|")
            print("_____________")
        elif attempts == 0:
            print(f"You only have no attempts left")
            game_over= True
            print("Game over! \n You dead")
            print("+---+----")
            print("|   |\n|   |\n|   O\n|  /|\ \n|  / \ \n|")
            print("_____________")
        elif '_' not in display:
            print("You Won")
            game_over = True

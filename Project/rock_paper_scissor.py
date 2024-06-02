import random
options=['R','P','S']
comp_choice=random.choice(options)
user_choice=input("Enter R/P/S.... ").upper()
if user_choice not in options:
    user_choice = input("Please enter only R/P/S.... ").upper()
if user_choice not in options:
    print("YOU LOSE!")
print("AI CHOICE IS "+comp_choice)
chances=[['R','P','LOSE'],['P','S','LOSE'],['S','R','LOSE'],['R','S','WIN'],['P','R','WIN'],['S','P','WIN']]
if user_choice==comp_choice:
    print("DRAW")
else:
    for i in range(0,6):
        for j in range(0,2):
            if chances[i][j]==user_choice and chances[i][j+1]==comp_choice:
                print(f"You {chances[i][2]}")
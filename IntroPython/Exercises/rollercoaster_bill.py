#here we are calculatin the bill for rollercoaster

height=int(input("please nter your height"))
if height >= 10:
    age=int(input("you are allowed!!! nter age"))
    if age < 12:
        rupee=150
    elif age <18:
        rupee=200
    else:
        rupee=250
    photo=input("want photo (y/n)? ")
    if photo == 'y':
        rupee+=50
    print(f"bill is {rupee}! enjoy the ride")

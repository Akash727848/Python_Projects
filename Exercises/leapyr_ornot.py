year=int(input("Nter the year "))
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yay {year} is leap year")
        else:
            print(f"Sorry {year} is not leap year")
    else:
        print(f"Yay {year} is leap year")
else:
    print(f"Sorry {year} is not leap year")
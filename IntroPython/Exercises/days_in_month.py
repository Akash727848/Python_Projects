def check_days(year,month):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year=True
            else:
                leap_year=False
        else:
            leap_year=True
    else:
        leap_year=False
    #ranganatha
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month ==2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return "'Yedhava sachinoda yearki enni nelalo kuda telida? chi!!!'"

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
print(f"{check_days(year,month)} days in {month} month of {year}year")

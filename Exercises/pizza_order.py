pi=int(input("Hey! please enter the options(1/2/3)size of pizza!\n1.small\n2.Medium\n3.Large\n   "))
cost=0
if pi==1:
    cost=100
elif pi==2:
    cost=200
elif pi==3:
    cost=300
else:
    pi=int(input("Hey! enter only numbers ra yedhava (1/2/3)"))
pepp=input("Want Pepperoni (Y/N) ")
Cheese=input("Want Cheese (Y/N) ")
if pepp=='Y':
    if pi==1:
        cost+=30
    else:
        cost+=50
if Cheese=='Y':
    cost+=20
else:
    print("needhi oka brathukena, cheese lekunda thintava! sare odhiley inka")
print(f"you opt for size {pi} pizza with pepperoni{pepp} and cheese{Cheese}.Please pay the bill {cost}")

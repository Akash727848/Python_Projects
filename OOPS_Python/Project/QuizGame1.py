import random
print("*****************************\n\tWelcome to My Quiz\n*****************************")
qs = ["Q1", "Q2", "Q3", "Q4", "Q5"]
l = []
Q1=""
Q2=""
Q3=''
Q4=''
Q5=''
for i in range(5):
    r = random.choice(qs)
    print(r)
    if r not in l:
        if r == "Q1":
            Q1 = input("1").upper()
        elif r == "Q2":
            Q2 = input("2").upper()
        elif r == "Q3":
            Q3 = input("3").upper()
        elif r == "Q4":
            Q4 = input("4").upper()
        elif r == "Q5":
            Q5 = input("5").upper()
        l.append(r)

score=0
if Q1=="D":
    score+=1
elif Q2=="A":
    score+=1
elif Q3=="B":
    score+=1
elif Q4=="C":
    score+=1
elif Q5=="D":
    score+=1
print(score)

# for i in range(len(ques)):
#     print(i)

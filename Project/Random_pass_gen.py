import random
print("Welcome to password Generator!")
letters=int(input("How many letters do you want in password:\n "))
numbers=int(input("How many numbers do you want in password:\n "))
symbol=int(input("How many symbols do you want in password:\n "))
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums=['0','1','2','3','4','5','6','7','8','9']
symb=['!','@','#','$','%','^','&','*','(',')']
pas=""
for i in range(0,letters):
    pas+=random.choice(alphabets)
for i in range(0,numbers):
    pas+=random.choice(nums)
for i in range(0, symbol):
    pas += random.choice(symb)
print(pas)
pas=''.join(random.sample(pas,len(pas)))
print("Your password is: "+pas)
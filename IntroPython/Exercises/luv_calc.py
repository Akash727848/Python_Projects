n1=(input("Enter your name to calculate love ")).lower()
n2=(input("enter your lover name ")).lower()
t=n1.count('t')+n2.count('t')
r=n1.count('r')+n2.count('r')
u=n1.count('u')+n2.count('u')
e=n1.count('e')+n2.count('e')
l=n1.count('l')+n2.count('l')
o=n1.count('o')+n2.count('o')
v=n1.count('v')+n2.count('v')
count= t+r+u+e+l+o+v
if count ==0:
    print("avsarama mawa neeku pelli")
elif count ==1:
    print("single king mawa nuvvu")
elif 2<=count and count<4:
    print("rasikudive mawa")
elif 5<=count and count<8:
    print("Lover boy ra")
else:
    print("Pelli cheskune avakasm undi mava")
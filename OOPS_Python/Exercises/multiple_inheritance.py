class Father:
    def __init__(self,strength2):
        self.strength2=strength2
        self.firstname = "Madishetti"
        self.name = "Ramesh"
    def acquire(self):
        print(f"I may not cook daily but can cook {self.strength2}\n And I am {self.firstname+" "+self.name}. ") #tasty
class Mother:
    def __init__(self,strength1):
        self.strength1=strength1
        self.firstname = "Madishetti"
        self.myname = "Premalatha"
    def acquire(self):
        print(f"I will cook food {self.strength1}. \n And I am {self.firstname+" "+self.myname}") #daily
class Boy(Father,Mother):
    firstname = "Madishetti"
    myname = "AkashAkshay"
    def __init__(self,strength1,strength2):
        Father.__init__(self,strength2)
        Mother.__init__(self,strength1)
    print(f"My Name is {firstname+" "+myname}")


calling=Boy("daily","tasty")
#Here the below funnction will manually refer the first parent function given to Child function
calling.acquire() #This will inherit the properties of father

#But to refer the seconf parent function, below is the way
Mother.acquire(calling) #This will  inherit the properties of Mother


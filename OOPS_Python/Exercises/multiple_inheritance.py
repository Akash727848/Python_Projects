class Mother:
    firstname = "Madishetti"
    myname = "Premalatha"

    def acquire(self):
        print("I will cook food daily. ")
class Father:
    firstname = "Madishetti"
    myname = "Ramesh"
    def acquire(self):
        print("I may not cook daily and but can cook tasty. ")
class Boy(Father,Mother):
    firstname = "Madishetti"
    myname = "AkashAkshay"
    print(f"My Name is {firstname+" "+myname}")


calling=Boy()
#Here the below funnction will manually refer the first parent function given to Child function
calling.acquire() #This will inherit the properties of father

#But to refer the seconf parent function, below is the way
Mother.acquire(Boy) #This will  inherit the properties of Mother


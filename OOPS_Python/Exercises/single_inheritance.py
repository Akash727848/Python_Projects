class human:
    def __init__(self,num_eyes,num_hands):
        self.num_eyes = num_eyes
        self.num_hands = num_hands
    def organs(self):
        print(f"I have {self.num_eyes} eyes and {self.num_hands} hands. ")
    def actions(self):
        print("i can work")
class Male(human):
    def __init__(self):
        super().__init__(2,2)
        print("Am Wealthy")
    def name(self,my_name):
        self.name=my_name
        print(f"My Name is {self.name}")
    def actions(self):
        super().actions()
        print("I can code and play")
p=Male()
p.name("Akash")
p.organs()
p.actions()

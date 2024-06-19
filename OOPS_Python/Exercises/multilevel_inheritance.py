class grandpa:
    strength = "responsibility"
    def __init__(self,grandpa_name):
        self.granny=grandpa_name
    def  acquire(self):
        print(f"Hey am Grandpa {self.granny} having {self.strength}.")
class papa(grandpa):
    strength1 = "patience"
    def __init__(self,papa_name):
        self.pa_name=papa_name
    def  acquire(self):
        super().acquire()
        print(f"Hey am papa {self.pa_name} having {self.strength1} and {grandpa.strength}. ")
class boy(papa):
    strength2 = "ishwararadhana"
    def __init__(self,grandpa_name,papa_name,boy_name):
        papa.__init__(self,papa_name)
        grandpa.__init__(self,grandpa_name)
        self.myname=boy_name
    def  acquire(self):
        super().acquire()
        print(f"Hey am boy {self.myname} having {self.strength2}, {papa.strength1} and {grandpa.strength}. ")

boy1=boy("Pullaiah Narayan","Ramesh Narayan","AkashAkshay Narayan")
boy1.acquire()



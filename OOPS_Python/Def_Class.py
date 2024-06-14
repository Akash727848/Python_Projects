class CarDesign:
    def __init__(self,model_name,color):
        self.model_name=model_name
        self.colors=color
    def greet(self,name):
        #self.name=name
        print(f"Hi {name}! Am Lamborghini and my model is : {self.model_name}")
initi=CarDesign('REVUELTO','Green')
# initi.model_name="REVUELTO"
initi.greet("Munna")
class om:
    l1=[{
        "gender":"Female",
        "hands":8,
        "husband":True
    },{
        "gender": "Male",
        "hands": 4,
        "husband": False
    },{
        "gender": "Male",
        "hands": 2,
        "husband": False
    }]
    def qualities(self):
        print("Nirakar")

class durga(om):
    def name(self):
        print("Durge Dugathi nashinye")
        for i in range(len(om.l1)):
            if om.l1[i]["gender"]=="Female":
                print(om.l1[i])


class shiva(om):
    def name(self):
        print("Chithanandha rupa shivoham shivoham")
        for i in range(len(om.l1)):
            if om.l1[i]["gender"]=="Male" and om.l1[i]["hands"]==2:
                print(om.l1[i])

class vishnu(om):
    def name(self):
        print("Jai Srimannarayana")
        for i in range(len(om.l1)):
            if om.l1[i]["gender"]=="Male" and om.l1[i]["hands"]==4:
                print(om.l1[i])

dev=input("enter name of god to see characteristics: \nvishnu\nshiva\ndurga: ")
if dev=="vishnu":
    call=vishnu()
    call.name()
elif dev=="shiva":
    call=shiva()
    call.name()
else:
    call=durga()
    call.name()


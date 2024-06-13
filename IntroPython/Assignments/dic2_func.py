list1=[{'Name': 'Akash', 'Roll_num': 44, 'Branch': 'ECE'}]
def add_item_dict(Name,Roll_num,Branch):
    dict1=dict()
    dict1['Name']=Name
    dict1['Roll_num'] = Roll_num
    dict1['Branch'] = Branch
    list1.append(dict1)
add_item_dict("Renuka",45,'ECE')
print(list1)

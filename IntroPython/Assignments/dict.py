dict1={
    "Jenani":93,
    "Hari":78,
    "Deepa":56,
    "Rahu":41,
    "Ankit":99,
    "Prej":34
}
print(dict1)
dict2=dict1.copy()
for i in dict2:
    mark=dict2[i]
    if mark>90:
        dict2[i]='A+'
    elif 90>mark>80:
        dict2[i]='A'
    elif 80>mark>70:
        dict2[i]='B'
    elif 70>mark>60:
        dict2[i]='C'
    elif 60>mark>50:
        dict2[i]='D'
    else:
        dict2[i] = 'Fail! yedhava brathuku enduku bathiki'
print(dict2)

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
hello_world=['h','e']#,'l','l','o',' ','w','o','r','l','d']
str=''
for i in range(0,len(hello_world)):
    for j in range(0,len(alphabets)):
        if hello_world[i]!=alphabets[j]:
        #    str+=hello_world[i]
            print(str)
        else:
            str+=alphabets[j]
        print(str)



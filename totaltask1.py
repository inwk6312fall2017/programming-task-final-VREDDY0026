wor=[]
maxo=[]
with open('Book1.txt', encoding="utf8") as b_1:
     for line in b_1:
         line=line.split()
         for word in line:
             wor.append(word)
    
     b1_max=max(wor,key=len)
     maxo.append(b1_max)

grp=[]
with open('Book2.txt', encoding="utf8") as b_2:
    for line2 in b_2:
        line2=line2.split()
        for words in line2:
            grp.append(words)
    
    b2_max = max(grp, key=len)
    maxo.append(book2_max)


lt=[]

with open('Book3.txt', encoding="utf8") as b_3:
    for line3 in b_3:
        line3=line3.split()
        for words in line3:
            lt.append(words)
    
    b3_max = max(lt , key=len)
    maxo.append(b3_max)
    print(maxo)

    print("The biggest word is "+str(max(maxo,key=len)))



wor=[]
with open('Book1.txt',encoding='utf8')as b_1:
   for line in b_1:
      line=line.split()
      for word in line:
         wor.append(word)
   print(wor)
   print(max(wor))



##CAN ALSO BE TRIED USING THIS FUNCTION TO FIND LONGEST WORD##
def Words():
    qfile=open('Book1.txt','r')
    long=''
    for line in qfile:
    if len(line)>len(long):
        long=line
    return long

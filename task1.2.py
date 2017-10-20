grp=[]
with open('Book2.txt',encoding='utf8')as b_2:
   for line in b_2:
      line=line.split()
      for word in line:
         grp.append(word)
   print(grp)
   print(max(grp))








##another method to find maximum letters in a word##
def Words():
    qfile=open('Book2.txt','r')
    long=''
    for line in qfile:
    if len(line)>len(long):
        long=line
    return long
print(l)


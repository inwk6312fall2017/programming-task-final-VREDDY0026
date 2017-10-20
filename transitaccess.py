with open ('Access_list.cfg','r')as aclis:
   d={}
   a=[]
   b=[]
   
   for line in acl:
      if 'transit_access' in line:
            a.append(line)
   d['transit_access']=a
   print(d)
   
   for line in aclis:
   print(line)            

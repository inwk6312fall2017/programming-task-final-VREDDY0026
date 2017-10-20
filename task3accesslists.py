##access lists file###



with open('running-config.cfg','r') as run:
    with open('Access_list.cfg','w') as new:
       for line in run:
            lines=run.readline()
            if 'access-list' in lines:
                new.write(lines)

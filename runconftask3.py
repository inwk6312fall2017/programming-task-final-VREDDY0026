


#replacing#
with open('running-config.cfg','r') as run:
    with open('runconftask3.cfg','w') as new:

        for line in run:
         new.write(line.replace('172','192'))
        new.close()

#location = weather.lookup_by_location('halifax')
#condition = location.condition()

# Get weather forecasts for the upcoming days.
#
#for forecasts in location.forecast():
#    print (forecasts['text'])
#    print (forecasts['date'])
#    print (forecasts['high'])
#    print (forecasts['low'])





from weather import Weather
weather = Weather()

location = weather.lookup_by_location('halifax')
condition = location.condition()
print (condition['text'])

five_days=[]

i=0
for forecasts in location.forecast():
    if i<5:
        every = []
        every.append(forecasts['text'])
        every.append(forecasts['date'])
        every.append(forecasts['high'])
        every.append(forecasts['low'])
        five_days.append(every)
        i+=1

print(five_days)

mxtmp=0
for day in five_days:
    if int(day[2])>int(mxtmp):
        mxtmp=day[2]
        to_day=day[1]
print("The max.temperature is  "+to_day +'and it is'+ mxtmp)

some=100
for day in five_days:
    if int(day[3])<int(some):
        some=day[3]
        to_day=day[1]
print("The low temperature is  "+to_day +'and it is'+ some)

for day in five_days:
    if day[0]=='foggy':
        to_day=day[1]
        print("The rain on "+to_day+" is possible "+day[0])
    else:
        pass

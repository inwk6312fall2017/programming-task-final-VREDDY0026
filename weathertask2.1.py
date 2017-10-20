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
for day in all_days:
    if int(day[2])>int(mxtmp):
        mxtmp=day[2]
print("The max.temperature is  "+day[1] +'and it is'+ mxtmp)




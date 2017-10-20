from weather import Weather
weather = Weather()


location = weather.lookup_by_location('Halifax')
condition = location.condition()

# Get weather forecasts for the upcoming days.

forecasts = location.forecast()
    Max_temp=[]
    Min_temp=[]
    cloud=[]

for forecast in forecasts range(5):
    Max_temp.appand(forecasts.temperature.max())
    Min_temp.appand((forecasts.temperature.min())
    cloud.appand(forecasts.cloud())

M_temp=Max_temp[0]
Mi_temp=Min_temp[0]
 

for item in Max_temp:
  if  Max_temp[item]>M_temp:
   M_temp=Max_temp[item]
  else:
   pass..


for item in Min_temp:
  if  Min_temp[item]<Mi_temp:
   Mi_temp=Min_temp[item]
  else:
   pass..
    

for item in cloud:
  if  cloud[item]=='cloudy':
  dic={}
  dict.setvalue("day[item]" , "cloudy")  
  else:
   pass..

print(M_temp , Mi_temp ,dict)

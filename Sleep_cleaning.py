import pandas as pd

data = pd.read_csv("Sleep_Efficiency.csv")
data = pd.DataFrame(data)

data = data.drop('ID',axis=1)
data = data.rename(columns= {'Wakeup time':'Wakeup_time','Sleep duration':'Sleep_duration',
                             'Sleep efficiency':'Sleep_efficiency','REM sleep percentage':'REM_percentage',
                             'Deep sleep percentage':'Deep_percentage','Light sleep percentage':'Light_percentage',
                             'Caffeine consumption':'Caffeine','Alcohol consumption':'Alcohol',
                             'Smoking status':'Smoking','Exercise frequency':'Exercise_frequency'})

data.to_csv("Sleep.csv", index=False)
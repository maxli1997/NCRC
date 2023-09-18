import pandas as pd

df = pd.read_excel('Shuttle_bus_coding.xlsx')
df2 = pd.read_csv('Shuttle_time_series.csv')
stoptimes = []
for i,r in df.iterrows():
    temp = df2[df2['Trip']==r['Trip']]
    temp = temp[temp['Starttime']==r['Starttime']]
    stoptime = 0
    for j,r2 in temp.iterrows():
        if r2['speed']<=0.1:
            stoptime += 10
    stoptimes.append(stoptime)
ndf = pd.DataFrame(stoptimes)
ndf.to_csv('stoptime.csv',index=False)
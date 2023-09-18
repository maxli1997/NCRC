import pandas as pd

num_intersections = 7
for i in range(1,num_intersections+1):
    df = pd.read_csv('Data/Pedestrian/NCRC-'+str(i)+'.csv',usecols=['Device','Trip','Time','NumTargets','Speed'])
    new_df = pd.DataFrame(columns=['Event','Device','Trip','Starttime','Endtime','Duration','Pedestrians','Stoptime'])

    event = 1
    device = df['Device'][0]
    trip = df['Trip'][0]
    time = df['Time'][0]
    starttime = time
    endtime = time
    stoptime = 0
    target = df['NumTargets'][0]
    for index,row in df.iterrows():
        if row['Device'] == device and row['Trip'] == trip and row['Time'] == time:
            continue
        elif row['Device'] == device and row['Trip'] == trip and abs(row['Time'] - time) <= 500:
            time = row['Time']
            endtime = time
            if row['NumTargets'] > target:
                target = row['NumTargets']
            if row['Speed'] == 0:
                stoptime += 10
        else:
            new_df = new_df.append({'Event':event,'Device':device,'Trip':trip,'Starttime':starttime,'Endtime':endtime,'Duration':endtime-starttime,'Pedestrians':target,'Stoptime':stoptime}, ignore_index=True)
            #write row
            event += 1
            device = row['Device']
            trip = row['Trip']
            time = row['Time']
            starttime = time
            endtime = time
            stoptime = 0
            target = row['NumTargets']
    new_df.to_csv('Events/Pedestrian/NCRC_Events-'+str(i)+'.csv',index=False,float_format='%.0f')
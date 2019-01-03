#Pandas homework
#put this in jupyter ok
#now let's get started
#look @ jupyter for instructions 
#path: Users/carolinemiller/Documents/github/PandasHomework pandashw.py 
#for uploading this dataset in ju put after pandashomeowrk purchase_data2.csv)

import pandas as pd
import numpy as np

purchase_data = pd.read_csv("purchase_data2.csv")

#print(purchase_data.head())

#enter total amount of players
#make a list of each unique value in sn column
unique_sn = pd.unique(purchase_data['SN'])
#print(unique_sn)

#use a count sort of function on the SN column
total_players = len(unique_sn)
print(total_players)
#make a new dataframe showing the total number of unique usernames


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

#use a count sort of function on the Unique SN column
total_players = len(unique_sn)

#make a new dataframe showing the total number of unique usernames
total_unique_players = pd.Series(["Total Players", total_players])
print(total_unique_players)



#Purchasing Analysis (Total)

#Run basic calculations to obtain number of unique items. Similar approach to finding the number of unique players
unique_items = pd.unique(purchase_data['Item ID'])
total_items = len(unique_items)

#Find average price. Make variable that stores output of average to put variable in dataframe
avg_price = np.mean(purchase_data['Price'])
avg_price_rounded = round(avg_price, 2)

#Find number of purchases. Again, use the len feature to get this total. May have to exclude nulls.
total_purchases = len(purchase_data['Purchase ID'])

#Find total revenue. make var and run sum function on needed column. Go to 2 decimal places.
total_revenue = sum(purchase_data['Price'])
total_revenue_rounded = round(total_revenue, 2)

#Create a summary data frame to hold the results
purchase_analysis = pd.DataFrame([{"Number of Unique Items": total_items, "Average Price": avg_price_rounded, 
"Number of Purchases": total_purchases, "Total Revenue": total_revenue}])
print(purchase_analysis)
#need to unsort the titles


#Gender Demographics

#make a new dataframe that doesn't store duplicate sns. find the counts of each gender and percent w this new df
unique_gender = pd.unique(purchase_data[['SN','Gender']])
print(unique_gender)

#Count of genders that purchased (use above variable for gender count and gender percent)
gender_count = purchase_data['Gender'].value_counts()
#print(gender_count)

#Percentage of genders
gender_percent = purchase_data['Gender'].value_counts(2) * 100
#how did adding an integer to the value_counts() method make them all turn into percents???? Is this a bug?
#either way it gave me what I'm looking for

#round the percent to two decimal places
gender_percent_rounded = round(gender_percent, 2)
#print(gender_percent_rounded)

#make a dataframe to put the total and percent next to each other for each gender
gender_demographics = pd.DataFrame({"Count": gender_count, "Percent": gender_percent_rounded})
print(gender_demographics)


#Purchasing Analysis (Gender)

#make three segmented dataframes that hold information on only males, only females, and only others

#run a purchase count function on each segmented df, make three variables to store

#do a mean function on price for each segmented df, make three variables to store

#run sum function for each segmented df, make three variables to store




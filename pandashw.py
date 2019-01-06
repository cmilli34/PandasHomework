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
unique_gender = pd.DataFrame(purchase_data[['SN', 'Gender']]).drop_duplicates()

#Count of genders that purchased (use above variable for gender count and gender percent)
gender_count = unique_gender['Gender'].value_counts()

#Percentage of genders
gender_percent = unique_gender['Gender'].value_counts(2) * 100
#how did adding an integer to the value_counts() method make them all turn into percents???? Is this a bug?
#Even if you add in a string or boolean it gives a percent. either way it gave me what I'm looking for

#round the percent to two decimal places
gender_percent_rounded = round(gender_percent, 2)

#make a dataframe to put the total and percent next to each other for each gender
gender_demographics = pd.DataFrame({"Count": gender_count, "Percent": gender_percent_rounded})
print(gender_demographics)




#Purchasing Analysis (Gender)
#groupby dataframe
genders = purchase_data.groupby('Gender')

#run a purchase count function on groupby df
total_genders_count = genders['Gender'].count()

#do a mean function on price for genders
genders_mean = round(genders['Price'].mean(), 2)

#run sum function for each segmented df, make three variables to store
genders_sum = genders['Price'].sum()

#find avg total per person, make three var to store
avg_per_person_genders = round(genders_sum/gender_count, 2)

#store in DF
gender_summary_purchase = pd.DataFrame({"Purchase Count": total_genders_count, 
"Average Purchase Price": genders_mean,
"Total Purchase Value": genders_sum, 
"Average Total Purchase Per Person": avg_per_person_genders})
print(gender_summary_purchase)
#revisit this df in jupyter to be sure it looks ok 




#Age Demographics

#make a frame that finds the unique screennames and the ages corresponding
unique_age = pd.DataFrame(purchase_data[['SN', 'Age']]).drop_duplicates()

#Establish bins for ages (<10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40+)
age_range= pd.cut(unique_age['Age'], [0, 9, 14, 19, 24, 29, 34, 39, 45],
labels= ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+'])

#Calculate the numbers and percentages by age group. Need to fix the setup of bins and put the <10 at top
count_age = age_range.value_counts()
percentage_age = round(age_range.value_counts(2), 4) * 100

#Create a summary data frame to hold the results and print
age_df = pd.DataFrame({"Count": count_age, "Percent": percentage_age}).sort_index()
print(age_df)




#Purchasing Analysis (Age)

#Create a new column to og dataframe that will show the age ranges of each category. Duplicates don't matter here.
purchase_data['Age Range'] = pd.cut(purchase_data['Age'], [0, 9, 14, 19, 24, 29, 34, 39, 45],
labels= ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+'])

#make a groupby dataframe to make it quicker to manipulate all of the age ranges
age_range_group = purchase_data.groupby('Age Range')

#Run basic calculations to obtain purchase count
total_agerange_count = age_range_group['Age Range'].count()

# avg. purchase price
age_group_mean = round(age_range_group['Price'].mean(), 2)
 
#total purchase value
age_group_sum = age_range_group['Price'].sum()

# avg. purchase total per person
avg_per_person_agerange = round(age_group_sum/count_age, 2)

#Create a summary data frame to hold the results
purchasing_analysis_agerange = pd.DataFrame({"Purchase Count": total_agerange_count, 
"Average Purchase Price": age_group_mean, "Total Purchase Value": age_group_sum, 
"Avg Total Purchase Per Person": avg_per_person_agerange}).sort_index()
print(purchasing_analysis_agerange)




#Top Spenders
#groupby function in terms of SN
sn_group = purchase_data.groupby('SN')

#count of each sn purchases
count_SN_purchase = sn_group['SN'].count()

#average purchase value
avg_sn_purchase = round(sn_group['Price'].mean(), 2)

#sum of how much each sn purchase
sum_sn_purchase = sn_group['Price'].sum()

#store variables in df, ascending order by total purchase value, only display top 5
user_purchases = pd.DataFrame({"Purchase Count": count_SN_purchase, "Average Purchase Size": avg_sn_purchase, 
"Total Purchase Value": sum_sn_purchase,}).sort_values(by = ['Total Purchase Value'], ascending = False)
print(user_purchases.head())




#Most popular items
#Retrieve the Item ID, Item Name, and Item Price columns
items_purchased = pd.DataFrame(purchase_data[['Item ID', 'Item Name', 'Price']])

#Group by Item ID and Item Name
item_group = items_purchased.groupby(['Item ID', 'Item Name'])

#Purchase count
item_count = item_group['Item ID'].count()

#Total Purchase Value
item_sum = item_group['Price'].sum()

#Item Price
item_price = item_sum/item_count

item_price2 = item_group['Price'].unique()
#ask which variable I should use 

#Create a summary data frame to hold the results, descending order, print head
item_popularity = pd.DataFrame({"Purchase Count": item_sum, "Item Price": item_price, 
"Total Purchase Value": item_sum}).sort_values(by = ['Purchase Count'], ascending = False)
print(item_popularity.head())



#Most Profitable items
item_profitability = pd.DataFrame({"Purchase Count": item_sum, "Item Price": item_price, 
"Total Purchase Value": item_sum}).sort_values(by = ['Total Purchase Value'], ascending = False)
print(item_profitability.head())
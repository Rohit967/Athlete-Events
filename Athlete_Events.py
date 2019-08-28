
# There are ten questions about 120 years of Olympic history: 
# athletes and results dataset in this task. 

#Download the file athlete_events.csv from the following Kaggle page:
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

#1. Import pandas
import pandas as pd

#2. read the dataset as dataframe and save to the variable data
data = pd.read_csv('athlete_events.csv')

#3. print out all the columns of the dataset
data.columns

#4. print out the first 5 rows of the data to take a look the data
data.head()

#1. How old were the youngest male and female participants of the 1996 Olympics?
# 10 points (You can use the methods: .max(), .min())

#Ans B

#A. 16 and 15
#B. 14 and 12
#C. 16 and 12
#D. 13 and 11

#Please write your code here

# You code here 
data_1996 = data[data['Year']==1996]

male_1996_min = data_1996[data_1996['Sex']=='M']['Age'].min()
female_1996_min = data_1996[data_1996['Sex']=='F']['Age'].min()


print('male min:{}'.format(male_1996_min))
print('female min:{}'.format(female_1996_min))


#2. How old were the oldest male and female participants of the 1996 Olympics?
# 10 points

# Ans C

#A. 46 and 35
#B. 50 and 45
#C. 63 and 58
#D. 30 and 41

#Please write your code here

male_1996_max = data_1996[data_1996['Sex']=='M']['Age'].max()
female_1996_max = data_1996[data_1996['Sex']=='F']['Age'].max()

print('male max:{}'.format(male_1996_max))
print('female max:{}'.format(female_1996_max))


#3. What are the mean and standard deviation of height for female basketball players 
# participated in the 2000 Olympics? Round the answer to the first decimal.
# 10 points (You can use the methods: .mean(), .std()

# Ans: D
#A. 178.5 and 7.2
#B. 179.4 and 10
#C. 180.7 and 6.7
#D. 182.4 and 9.1

#Please write your code here

# You code here 
female = data[data['Sex']=='F']
female_2000 = female[female['Year']==2000]

#print(data['Sport'].unique())
print(data.columns)
female_2000_basketball = female_2000[female_2000['Sport']=='Basketball']
print('2000 female basketball player mean: {:.1f}'.format(female_2000_basketball['Height'].mean()))
print('2000 female basketball player std: {:.1f}'.format(female_2000_basketball['Height'].std()))



#4. What are the mean and standard deviation of height for male basketball players 
# participated in the 2000 Olympics? Round the answer to the first decimal.
# 10 points

#Ans B

#A. 178.5 and 7.2
#B. 199.5 and 9.0
#C. 180.7 and 6.7
#D. 182.4 and 9.1

#Please write your code here

# You code here 
female = data[data['Sex']=='M']
female_2000 = female[female['Year']==2000]

#print(data['Sport'].unique())
print(data.columns)
female_2000_basketball = female_2000[female_2000['Sport']=='Basketball']
print('2000 female basketball player mean: {:.1f}'.format(female_2000_basketball['Height'].mean()))
print('2000 female basketball player std: {:.1f}'.format(female_2000_basketball['Height'].std()))



#5. How many silver medals in tennis did Australia (AUS) win at the 2000 Olympics?
# 10 points ()

#Ans C

#A. 0
#B. 1
#C. 2
#D. 3

#Please write your code here

# You code here 
print(data.columns)
data_2000 = data[data['Year']==2000]
data_2000_AUS = data_2000[data_2000['NOC']=='AUS']
data_2000_AUS_Tennis = data_2000_AUS[data_2000_AUS['Sport']=='Tennis']
print(data_2000.shape)
print(data_2000_AUS.shape)
print(data_2000_AUS_Tennis.shape)
#print(data_2000['NOC'].unique())
print(data_2000_AUS_Tennis[data_2000_AUS_Tennis['Medal']=='Silver'].count())


#6. How many silver medals did India (IND) win at the 2016 Olympics? 
# 10 points

#Ans B

#A. 0
#B. 1
#C. 2
#D. 3

#Please write your code here

data_2016 = data[data['Year']==2016]
data_2016_IND = data_2016[data_2016['NOC']=='IND']

print(data_2016_IND[data_2016_IND['Medal']=='Silver'].count())


#7. How many medals (Gold, Silver and Bronze) did USA win in total at the 2016 Olympics?
# 10 points (You can use the method .count())

#A. 100
#B. 139
#C. 193
#D. 264
 
#Please write your code here

USA_2016 = data[(data['NOC']== 'USA') &(data['Year'] == 2016)]
USA_2016['Medal'].count()



#8. What is the absolute difference between the number of unique sports at the 
# 1995 Olympics and 2016 Olympics?
# 10 points (You can use the method .nunique())

#Ans D

#A. 16
#B. 24
#C. 26
#D. 34

#Please write your code here

data_1995 = data[data['Year']==1995]
print(data_1995)
data_2016 = data[data['Year']==2016]
print(data_2016['Sport'].nunique())

#9. How many Gold medals and Silver medals did 'Michael Fred Phelps, II' win 
# at the 2016 Olympics?

#Ans: D

# 10 points
#A. Gold 2, Silver 4
#B. Gold 3, Silver 3
#C. Gold 4, Silver 2
#D. Gold 5, Silver 1

#Please write your code here

data[data['Name']=='Michael Fred Phelps, II'].shape
print(data[(data['Name']=='Michael Fred Phelps, II') & (data['Year']==2016)] )


#10. Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics? 
# Do not consider NaN values in Medal column.
# 10 points

#Ans A. Yes
#A. Yes
#B. No

#Please write your code here

data_2016 = data[data['Year']==2016].dropna()
#print(data.columns)
Switzerland_2016 = data_2016[data_2016['Team']=='Switzerland']['Medal']
Serbia_2016 = data_2016[data_2016['Team']=='Serbia']['Medal']
print(Switzerland_2016.count() < Serbia_2016.count())
print(Switzerland_2016.count())
print(Serbia_2016.count())



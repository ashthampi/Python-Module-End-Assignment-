#!/usr/bin/env python
# coding: utf-8

# ### 1. Determine the distribution of employees across each team and calculate the percentage split relative to the total number of employees.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("salary - myexcel.csv")
df['Height'] = np.random.randint(150, 181, size=df.shape[0])

TD = df['Team'].value_counts()
TP = (TD / df.shape[0]) * 100
TDP = pd.DataFrame({'Count': TD, 'Percentage': TP})
print(TDP)

TDP['Count'].plot(kind='bar')
plt.title('Employees Distribution')
plt.xlabel('Team')
plt.ylabel('Employees')
plt.show()


# ### Segregate employees based on their positions within the company.

# In[9]:


PD = df['Position'].value_counts()
print(PD)
PD.plot(kind='bar')
plt.title('Position Based Distribution of Employees')
plt.xlabel('Position')
plt.ylabel('Employees')
plt.show()


# ###  Identify the predominant age group among employees.

# In[17]:


AD = df['Age'].value_counts().sort_index()
print(AD)

AD = df['Age'].value_counts()
SAD = AD.sort_values(ascending=False)
n = 5
MPA = SAD.head(n)
print(f"Most predominant age groups:",MPA)

AD.plot(kind='bar')
plt.title('Age Based Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Employees')
plt.show()


# ### Discover which team and position have the highest salary expenditure.

# In[7]:


TS = df.groupby('Team')['Salary'].sum().sort_values(ascending=False)
PS = df.groupby('Position')['Salary'].sum().sort_values(ascending=False)

print("\nTeam Salary Expenditure:\n", TS)

TS.plot(kind='bar')
plt.title('Team Based Salary Expenditure')
plt.xlabel('Team')
plt.ylabel('Total Salary')
plt.show()

print("\nPosition Salary Expenditure:\n", PS)

PS.plot(kind='bar')
plt.title('Position Based Salary Expenditure')
plt.xlabel('Position')
plt.ylabel('Total Salary')
plt.show()

HTS = TS.head(1)
HT = HTS.index[0]
HTE = HTS.values[0]

HPS = PS.head(1)
HP = HPS.index[0]
HPE = HPS.values[0]

print("\nTeam with highest salary expenditure:", HT)
print("Total salary expenditure for team:", HTE)

print("\nPosition with highest salary expenditure:", HP)
print("Total salary expenditure for position:", HPE)


# ### Investigate if there's any correlation between age and salary, and represent it visually.

# In[21]:


sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Age and Salary Correlation')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


# ### Insights Gained
# 
# 1. Team Distribution: The team with most number of employees is New Orleans Pelicans which shows that they have the highest need of employees.
# 
# 2. Position Distribution: This helps in identifying the most popular positions held by employees. Which are SG, SF, and PF. This helps in comprehending how jobs and talent are distributed around the company.
# 
# 3. Age Group: The majority of employees fall into a specific age range, the predominant age group within the company fall within the 25-30 age range., showing that they have more of young or middle-aged workforce.
# 
# 4. Salary Expenditure: Certain teams and positions command higher salaries, highest salary expenditure indicate which roles are most valued.
# 
# 5. Age-Salary Correlation: The scatter plot reveals how salary scales with age, providing insights into the company's  practices. Ages around 23-33 have higher salaries compared to others.

# In[ ]:





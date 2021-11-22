#!/usr/bin/env python
# coding: utf-8

# ### Loading and assessing data

# In[4]:


# first import the libraries
import pandas as pd


# In[5]:


# import the World Cup T20 data
data = pd.read_csv(r'C:\Users\Mairaj-PC\Desktop\worldt20_data.csv')
data.head()


# In[6]:


# check the description of data in detail
data.info()


# In[7]:


# check the basic statistical summary of data
data.describe()


# ### Sorting, counting and applying a condition to data

# In[36]:


# sort the data from highest to lowest target of each match
data.sort_values('target', ascending = False).head(3)


# In[9]:


# sorting with multiple columns (lowest by target and highest by temperature)
data.sort_values(['target', 'avg_temperature'], ascending = [True, False]).head(3)


# In[10]:


# find the player those have 50 plus individual scores and target not achieved
data[(data['high_indvidual_scores'] > 50) & (data['target_achieved'] == 0)].head()


# In[11]:


# find the count of matches in each venue
data['venue'].value_counts()


# In[12]:


# find the most number of wins by each country
most_wins = data['Winner'].value_counts()
most_wins.head(4)


# ### Group Summary Statistics from data (groupby)

# In[13]:


# average temperatue in each venue
data.groupby('venue')['avg_temperature'].mean()


# In[14]:


# find the summary statistics of strike rate and target for each winning country
data.groupby('Winner')[['strike_rate', 'target']].agg([min, max])


# In[15]:


# find the most economical bowler 
data.groupby('best_bowler')['economy'].mean().sort_values().head(3)


# ### Indexing and Slicing

# In[33]:


# make the index set to winner toss to see which have more toss win
new_data = data.set_index('Winner_toss')
new_data.head(3)


# In[17]:


# subset the new data with few columns
selective_new_data = new_data[['team_2', 'stage']]

# print result of Pakistan
print(selective_new_data.loc['Pakistan'])


# In[18]:


# we also use indexing by number using .iloc[]
# See the match 15 to 18
data.iloc[14:18,:5]


# ### Plotting with Pandas

# In[19]:


# Create a vraible most_wins that show number of matches won by every team
# lets see result with bar plot
most_wins.plot(kind = 'bar')


# In[20]:


# lets find a relation with strike rate and target set in those game when target is chased
target_chased = data[data['target_achieved'] == 1]

# for this, we use scatter plot
target_chased.plot(x = 'target', y = 'strike_rate', kind = 'scatter')


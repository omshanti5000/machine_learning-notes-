
# coding: utf-8

# In[1]:


import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')
users.head()


# In[3]:


users_cols=['user_id','age','sex','occupation','zip_code']
users=pd.read_csv('http://bit.ly/movieusers',sep='|',header=None,names=users_cols,
                 index_col='user_id')
users.head()


# In[4]:


users.zip_code.duplicated().sum()


# In[5]:


users.duplicated().sum()


# In[6]:


users.duplicated(subset=['age','zip_code']).sum()


# In[7]:


users.drop_duplicates(subset=['age','zip_code']).shape


# In[19]:


users.duplicated(subset=['age','zip_code']).sum()


# In[33]:


users.duplicated(subset=['age'],keep=False).sum()


# In[41]:


import pandas as pd
df = pd.DataFrame({"A":["foo", "foo", "foo", "bar"], "B":[0,1,1,1], "C":["A","A","B","A"]})
df.head()


# In[45]:


df.drop_duplicates(subset=['A', 'C'], keep='first')


# #how to avoid a seeting with copy warning in pandas??? 

# In[48]:


import pandas as pd
movies=pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[49]:


movies=pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[51]:


movies.content_rating.isnull().sum()


# In[52]:


movies[movies.content_rating.isnull()]


# In[53]:


movies.content_rating.value_counts()


# In[55]:


movies[movies.content_rating=='NOT RATED'].head()


# In[59]:


movies[movies.content_rating=='NOT RATED']


# In[62]:


import numpy as np
movies[movies.content_rating=='NOT RATED'].content_rating=np.nan


# In[63]:


movies.content_rating


# In[66]:


movies.content_rating.isnull().sum()


# In[69]:


movies.loc[movies.content_rating=='NOT RATED','content_rating']=np.nan


# In[70]:


movies.content_rating.isnull().sum()


# In[71]:


movies.star_rating


# In[73]:


top_movies=movies.loc[movies.star_rating>=9,:]
top_movies


# In[74]:


top_movies.loc[0,'duration']=150


# In[75]:


top_movies


# In[76]:


movies.head(1)


# In[80]:


top_movies=movies.loc[movies.star_rating>=9,:].copy()
top_movies.loc[0,'duration']=172
top_movies


# how do i chage display option in pandas 

# In[81]:


drinks=pd.read_csv('http://bit.ly/drinksbycountry')
drinks


# In[84]:


pd.get_option('display.max_rows')


# In[86]:


pd.set_option('display.max_rows',None)
drinks


# In[89]:


pd.reset_option('display.max_rows')
drinks


# In[90]:


pd.get_option('display.max_columns')


# In[93]:


train=pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[92]:


pd.get_option('display.max_colwidth')


# In[94]:


pd.set_option('display.max_colwidth',1000)
train.head()


# In[95]:


pd.set_option('display.precision',2)
train.head()


# In[97]:


drinks['x']=drinks.wine_servings *1000
drinks['y']=drinks.total_litres_of_pure_alcohol * 1000
drinks.head()


# In[99]:


pd.set_option('display.float_format','{:,}'.format)
drinks.head()


# In[100]:


drinks.dtypes


# In[101]:


pd.describe_option()


# In[102]:


pd.describe_option('rows')


# In[103]:


pd.reset_option('all')


# In[104]:


drinks.head()


# # how do i create a pandas DataFrame from another project

# In[137]:


pd.DataFrame({'id':'[100,200,300]','color':'[100,2000,3000]'},index=
            [0])


# The error message says that if you're passing scalar values, you have to pass an index. So you can either not use scalar values for the columns -- e.g. use a list:
# 
# >>> df = pd.DataFrame({'A': [a], 'B': [b]})
# >>> df
#    A  B
# 0  2  3
# or use scalar values and pass an index:
# 
# >>> df = pd.DataFrame({'A': a, 'B': b}, index=[0])
# >>> df
#    A  B
# 0  2  3

# In[140]:


df=pd.DataFrame({'id':[100,200,300],'color':['red','blue','red']},columns=['id','color'],
               index=['a','b','c'])
df


# In[141]:


pd.DataFrame([[100,'red'],[200,'red'],[300,'blue']],columns=['id','color'])


# In[142]:


import numpy as np
arr=np.random.rand(4,2)
arr


# In[143]:


pd.DataFrame(arr,columns=['one','two'])


# In[146]:


pd.DataFrame({'student':np.arange(100,110,1),'test':np.random.randint(60,101,10)
             })


# In[148]:


s=pd.Series(['round','square'],index=['c','b'],name='shape')
s


# In[149]:


df


# In[151]:


pd.concat([df,s],axis=1)


# In[152]:


train=pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[155]:


train['sex_num']=train.Sex.map({'female':0,'male':1})
train.head()


# In[156]:


train.loc[0:4,['Sex','sex_num']]


# In[158]:


train['Name_length']=train.Name.apply(len)
train.loc[0:4,['Name','Name_length']]


# In[161]:


import numpy as np
train['Fare_cell']=train.Fare.apply(np.ceil)
train.loc[0:4,['Fare','Fare_cell']]


# In[162]:


train.Name.head()


# In[163]:


train.Name.str.split(',').head()


# In[164]:


def get_element(my_list,position):
    return my_list[position]
train.Name.str.split(',').apply(get_element,position=1).head()


# In[167]:


train.Name.str.split(',').apply( lambda x:x[1]).head()


# In[168]:


drinks=pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[169]:


drinks.loc[:,'beer_servings':'wine_servings'].head()


# In[170]:


drinks.head()


# In[173]:


drinks.loc[:,'beer_servings':'wine_servings'].apply(max,axis=1).head()


# In[174]:


drinks.loc[:,'beer_servings':'wine_servings'].applymap(float).head()


# In[176]:


drinks.loc[:,'beer_servings':'wine_servings']=drinks.loc[:,'beer_servings':'wine_servings'].applymap(float)
drinks.head()


# 
# 140
# down vote
# accepted
# It means you just love to code, not necessarily for work or for school. The <3 characters represent a heart symbol (❤️), which means "love".
# 
# 

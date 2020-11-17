#!/usr/bin/env python
# coding: utf-8

# # App Profiles Project
# ## Profitable Apps for App Store & Google Play Store
# 
# ## Introduction:
# ### Summary:
# The purchase of this project is to prepare data to help our developers understand what types of apps are most profitable.  To accomplish this goal, we will collect and analyze data for apps availalbe on the App Store and Google Play.
# ### Goals:
# ## Data Sets
# ### App Store
# Data for approximately 7,000 apps on the App Store was collected in July, 2017. 
# #### Download
# [Download CSV File](https://dq-content.s3.amazonaws.com/350/AppleStore.csv)
# 
# ### Google Play Store
# Data for approximately 10,000 apps on the Google Play Store was collected in August, 2018. 
# #### Download
# [Download CSV File](https://dq-content.s3.amazonaws.com/350/googleplaystore.csv)

# ## Reading Data Sets

# In[1]:


from csv import reader

# Source Data
app_store_file = 'AppleStore.csv'
google_play_file = 'googleplaystore.csv'

# Opening Data Set Files
opened_app_store_file = open(app_store_file)
opened_google_play_file = open(google_play_file)
# Reading Files
read_app_store_file = reader(opened_app_store_file)
read_google_play_file = reader(opened_google_play_file)
# Creating List
app_store_data = list(read_app_store_file)
google_play_data = list(read_google_play_file)


# ## Exploring Data

# ### explore_data()

# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')
        
    if rows_and_columns:
        print('Number of rows: ', len(dataset))
        print('Number of columns: ', len(dataset[0]))
        print('\n')


# In[3]:


print(explore_data(app_store_data, 0, 3, True))
print(explore_data(google_play_data, 0, 3, True))


# ## Incorrect Data
# ### Google Play Store - Missing Column and Data Shift
# The following error was reported in [this discussion](https://www.kaggle.com/lava18/google-play-store-apps/discussion/66015).  Based on review it appears that the "Category" column was deleted and the data was shifted accordingly.

# In[4]:


print(explore_data(google_play_data, 0, 1, False))
print(explore_data(google_play_data, 10473, 10474, False))


# #### Action:
# Row was deleted and confirmed by accessing row 10472 and comparing total number of rows.

# In[5]:


del google_play_data[10473]
print(explore_data(google_play_data, 10473, 10474, True))


# ## Duplicate Data

# In[6]:


def duplicate_data(app_store, app_name_col):
    # Empty dictionary to contain the name and number of duplicate entries
    app_store_unique = []
    app_store_duplicates = {}

    # Loops over all data skipping the header row
    for app_data in app_store[1:]:
        name = app_data[app_name_col]

        # Checks if app is a duplicate (already exists in unique set)
        if name in app_store_unique:
            # Adds app or increments the dictionary
            if name in app_store_duplicates:
                app_store_duplicates[name] += 1
            else:
                app_store_duplicates[name] = 1
        else:
            app_store_unique.append(name)

    print("Number of unique apps in the store: " + str(len(app_store_unique)))
    print("Number of apps with at least one duplicate: " + str(len(app_store_duplicates)))
    return app_store_unique, app_store_duplicates


# ### Results
# #### App Store

# In[7]:


app_store_unique, app_store_duplicates = duplicate_data(app_store_data, 1)


# #### Google Play Store

# In[ ]:


google_play_unique, google_play_duplicates = duplicate_data(google_play_data, 0)


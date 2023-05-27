#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pyodbc
import pandas as pd
import numpy as np


# In[2]:


country = pd.read_csv (r'C:\Program Files\Input_Data\Country.csv',header=None,quotechar="'")
country.columns=["A","B","C","D"]
print(country)


# In[4]:


import mysql.connector
mydb = mysql.connector.connect(host="acadmysqldb001p.uta.edu",user="vxk2690",passwd="rebmetpeSowTxiS!2022",database="vxk2690")
mydb
mycursor = mydb.cursor()   
#for i,row in country.iterrows():
    #sql="INSERT INTO country (country_name,population,no_of_worldcup_won,manager) values (%s, %s, %s, %s)"
    #mycursor.execute(sql,(row.A,row.B,row.C,row.D))
#mydb.commit()
mycursor.execute("select * from country")
result = mycursor.fetchall()
result 


# In[3]:


players = pd.read_csv (r'C:\Program Files\Input_Data\Players.csv',header=None, quotechar="'")
players.columns=["A","B","C","D","E","F","G","H","I","J","K"]
print(players)


# In[36]:


for i,row in players.iterrows():
    sql="INSERT INTO players (player_id,name,fname,lname,dob,country,height,club,position,caps_for_country,is_captain) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql,(row.A,row.B,row.C,row.D,row.E,row.F,row.G,row.H,row.I,row.J,row.K))
mydb.commit()
mycursor.execute("select * from players")
result = mycursor.fetchall()
print(result)


# In[105]:


match_results = pd.read_csv(r'C:\Users\sbhar\Downloads\Input_Data_Project1_Fall_2022_002\Input_Data\Match_results.csv', header=None, quotechar="'")
match_results.columns=["A","B","C","D","E","F","G","H","I"]
print(match_results)


# In[39]:


for i,row in match_results.iterrows():
    sql="INSERT INTO match_results (match_id,date_of_match,Start_time_of_match,team1,team2,team1_score,team2_score,stadium_name,host_city) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql,(row.A,row.B,row.C,row.D,row.E,row.F,row.G,row.H,row.I))
mydb.commit()
mycursor.execute("select * from match_results")
result = mycursor.fetchall()
print(result)


# In[7]:


player_assists_goals = pd.read_csv(r'C:\Users\sbhar\Downloads\Input_Data_Project1_Fall_2022_002\Input_Data\Player_Assists_Goals.csv',header=None )
player_assists_goals.columns=["A","B","C","D","E"]
player_assists_goals = player_assists_goals.astype({"A":'object', "B":'object',"C":'object',"D":'object',"E":'object'})
player_assists_goals


# In[6]:


for i,row in player_assists_goals.iterrows():
    sql="INSERT INTO player_assists_goals (player_id,no_of_matches,goals,assists,minutes_played) values (%s, %s, %s, %s, %s)"
    mycursor.execute(sql,(row.A,row.B,row.C,row.D,row.E))
mydb.commit()
#mycursor.execute("select * from player_assists_goals")
#result = mycursor.fetchall()
#print(result)


# In[22]:


player_cards = pd.read_csv(r'C:\Users\sbhar\Downloads\Input_Data_Project1_Fall_2022_002\Input_Data\Player_Cards.csv',header=None, quotechar="'")
player_cards.columns=["A","B","C"]
player_cards = player_cards.astype({"A":'object', "B":'object',"C":'object'})


# In[23]:


for i,row in player_cards.iterrows():
    sql="INSERT INTO player_cards (player_id,yellow_cards,red_cards) values (%s, %s, %s)"
    mycursor.execute(sql,(row.A,row.B,row.C))
mydb.commit()
# mycursor.execute("select * from player_cards")
# result = mycursor.fetchall()
# print(result)


# In[ ]:





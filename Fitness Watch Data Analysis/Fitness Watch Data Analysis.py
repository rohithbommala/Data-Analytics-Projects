#!/usr/bin/env python
# coding: utf-8

# # Fitness Watch Data Analysis

# Fitness Watch Data Analysis involves analyzing the data collected by fitness wearables or smartwatches to gain insights into users’ health and activity patterns. These devices track metrics like steps taken, energy burned, walking speed, and more. So, if you want to learn how to analyze the data of a fitness watch, this is for you.

# In[2]:


import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import plotly.express as px

data = pd.read_csv("Apple Fitness Data")
data.head()


# In[3]:


print(data.isnull().sum())


# In[4]:


# Step Count Over Time
fig1 = px.line(data, x="Time",
               y="Step Count",
               title="Step Count Over Time")
fig1.show()


# In[5]:


# Distance Covered Over Time
fig2 = px.line(data, x="Time",
               y="Distance",
               title="Distance Covered Over Time")
fig2.show()


# In[6]:


# Energy Burned Over Time
fig3 = px.line(data, x="Time",
               y="Energy Burned",
               title="Energy Burned Over Time")
fig3.show()


# In[7]:


# Walking Speed Over Time
fig4 = px.line(data, x="Time",
               y="Walking Speed",
               title="Walking Speed Over Time")
fig4.show()


# In[8]:


# Calculate Average Step Count per Day
average_step_count_per_day = data.groupby("Date")["Step Count"].mean().reset_index()

fig5 = px.bar(average_step_count_per_day, x="Date",
              y="Step Count",
              title="Average Step Count per Day")
fig5.update_xaxes(type='category')
fig5.show()


# In[9]:


# Calculate Walking Efficiency
data["Walking Efficiency"] = data["Distance"] / data["Step Count"]

fig6 = px.line(data, x="Time",
               y="Walking Efficiency",
               title="Walking Efficiency Over Time")
fig6.show()


# In[11]:


# Create Time Intervals
time_intervals = pd.cut(pd.to_datetime(data["Time"]).dt.hour,
                        bins=[0, 12, 18, 24],
                        labels=["Morning", "Afternoon", "Evening"], 
                        right=False)

data["Time Interval"] = time_intervals

# Variations in Step Count and Walking Speed by Time Interval
fig7 = px.scatter(data, x="Step Count",
                  y="Walking Speed",
                  color="Time Interval",
                  title="Step Count and Walking Speed Variations by Time Interval",
                  trendline='ols')
fig7.show()


# In[13]:


# Reshape data for treemap
daily_avg_metrics = data.groupby("Date").mean().reset_index()

daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], 
                                                  value_vars=["Step Count", "Distance", 
                                                              "Energy Burned", "Flights Climbed", 
                                                              "Walking Double Support Percentage", 
                                                              "Walking Speed"])

# Treemap of Daily Averages for Different Metrics Over Several Weeks
fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics")
fig.show()


# In[17]:


# Select metrics excluding Step Count
metrics_to_visualize = ["Distance", "Energy Burned", "Flights Climbed", 
                        "Walking Double Support Percentage", "Walking Speed"]

# Reshape data for treemap
daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], value_vars=metrics_to_visualize)

fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics (Excluding Step Count)")
fig.show()


# # Summary
# So this is how to perform Fitness Data Analysis using Python. Fitness Watch Data Analysis is a crucial tool for businesses in the health and wellness domain. By analyzing user data from fitness wearables, companies can understand user behaviour, offer personalized solutions, and contribute to improving users’ overall health and well-being. I hope you liked this article on Fitness Watch Data Analysis using Python.

# In[ ]:





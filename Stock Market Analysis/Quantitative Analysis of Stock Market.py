#!/usr/bin/env python
# coding: utf-8

# # Quantitative Analysis of Stock Market

# * Quantitative Analysis in the stock market involves the use of mathematical and statistical techniques to understand, predict, and make decisions about financial investments. 
# * If you want to learn how to perform Quantitative Analysis on stock market data

# # Quantitative Analysis of Stock Market: Process We Can Follow

# * Quantitative Analysis in the stock market is a financial methodology that utilizes mathematical and statistical techniques to analyze stocks and financial markets.

# * Below is the process we can follow for the task of Quantitative Analysis of the stock market:
# 
#     * Clearly define the objectives and questions to be answered.
#     * Identify the key performance indicators (KPIs) relevant to the analysis.
#     * Gather historical stock market data, including prices, volumes, and other relevant financial indicators.
#     * Clean and preprocess the data to handle missing values, outliers, and errors.
#     * Conduct initial analysis to understand data distributions, patterns, and correlations.
#     * Implement various strategies based on quantitative analysis.

# # Code Starts from here

# In[4]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.templates.default = "plotly_white"

# Load the dataset
stocks_data = pd.read_csv("stocks")

# Display the first few rows of the dataset
stocks_data.head()


# The dataset contains the following columns for stock market data:
# 
#     Ticker: The stock ticker symbol.
#     Date: The trading date.
#     Open: The opening price of the stock for the day.
#     High: The highest price of the stock during the day.
#     Low: The lowest price of the stock during the day.
#     Close: The closing price of the stock for the day.
#     Adj Close: The adjusted closing price, which accounts for all corporate actions such as dividends, stock splits, etc.
#     Volume: The number of shares traded during the day.

# In[8]:


stocks_data['Ticker'].unique()


# # To perform a quantitative analysis, we can explore various statistical concepts like descriptive statistics, time series analysis, correlation analysis, and more. Here are some potential analyses we can perform:
# 
#     Descriptive Statistics: Summary statistics (mean, median, standard deviation, etc.) for each stock.
#     Time Series Analysis: Trends and patterns over time, especially for closing prices.
#     Volatility Analysis: How much the stock price fluctuates over a period.
#     Correlation Analysis: How stock prices of different companies are related to each other.
#     Comparative Analysis: Comparing the performance of different stocks.
#     Risk-Return Trade-off Analysis: Analyzing the balance between the potential risks and rewards of different stocks,aiding in portfolio management.

# # Descriptive Statistics
# * Descriptive Statistics will provide summary statistics for each stock in the dataset. We’ll look at measures such as mean, median, standard deviation, and more for the Close prices:

# In[9]:


descriptive_stats = stocks_data.groupby('Ticker')['Close'].describe()


# In[10]:


descriptive_stats


# # Let’s break down the results for each stock:
# 
# * AAPL (Apple Inc.)
#     * Count: 62.0 (The number of observations or trading days included in the dataset for AAPL)
#     * Mean: 158.24 (The average closing price)
#     * Standard Deviation: 7.36 (Measures the amount of variation or dispersion of closing prices)
#     * Minimum: 145.31 (The lowest closing price in the dataset)
#     * 25th Percentile: 152.08 (25% of the closing prices are below this value)
#     * Median (50%): 158.06 (The middle value of the closing prices)
#     * 75th Percentile: 165.16 (75% of the closing prices are below this value)
#     * Maximum: 173.57 (The highest closing price in the dataset)
# * GOOG (Alphabet Inc.)
#     * Similar statistics as AAPL, but for GOOG. The mean closing price is 100.63, with a standard deviation of 6.28, indicating less variability in closing prices compared to AAPL.
# 
# * MSFT (Microsoft Corporation)
#     * The dataset includes the same number of observations for MSFT. It has a higher mean closing price of 275.04 and a higher standard deviation of 17.68, suggesting greater price variability than AAPL and GOOG.
# 
# * NFLX (Netflix Inc.)
#     * NFLX shows the highest mean closing price (327.61) among these stocks and the highest standard deviation (18.55), indicating the most significant price fluctuation.

# # Time Series Analysis

# In[12]:


# Time Series Analysis
stocks_data['Date'] = pd.to_datetime(stocks_data['Date'])
pivot_data = stocks_data.pivot(index='Date', columns='Ticker', values='Close')

# Create a subplot
fig = make_subplots(rows=1, cols=1)

# Add traces for each stock ticker
for column in pivot_data.columns:
    fig.add_trace(
        go.Scatter(x=pivot_data.index, y=pivot_data[column], name=column),
        row=1, col=1
    )

# Update layout
fig.update_layout(
    title_text='Time Series of Closing Prices',
    xaxis_title='Date',
    yaxis_title='Closing Price',
    legend_title='Ticker',
    showlegend=True
)

# Show the plot
fig.show()


# * The above plot displays the time series of the closing prices for each stock (AAPL, GOOG, MSFT, NFLX) over the observed period. Here are some key observations:
# 
#     * Trend: Each stock shows its unique trend over time. For instance, AAPL and MSFT exhibit a general upward trend in this period.
#     * Volatility: There is noticeable volatility in the stock prices. For example, NFLX shows more pronounced fluctuations compared to others.
#     * Comparative Performance: When comparing the stocks, MSFT and NFLX generally trade at higher price levels than AAPL and GOOG in this dataset.

# # Volatility Analysis

# In[15]:


# Volatility Analysis
volatility = pivot_data.std().sort_values(ascending=False)

fig = px.bar(volatility,
             x=volatility.index,
             y=volatility.values,
             labels={'y': 'Standard Deviation', 'x': 'Ticker'},
             title='Volatility of Closing Prices (Standard Deviation)')

# Show the figure
fig.show()


# # Correlation Analysis

# In[19]:


# Correlation Analysis
correlation_matrix = pivot_data.corr()

fig = go.Figure(data=go.Heatmap(
                    z=correlation_matrix,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='blues',
                    colorbar=dict(title='Correlation'),
                    ))

# Update layout
fig.update_layout(
    title='Correlation Matrix of Closing Prices',
    xaxis_title='Ticker',
    yaxis_title='Ticker'
)

# Show the figure
fig.show()


# * Values close to +1 indicate a strong positive correlation, meaning that as one stock’s price increases, the other tends to increase as well.
# * Values close to -1 indicate a strong negative correlation, where one stock’s price increase corresponds to a decrease in the other.
# * Values around 0 indicate a lack of correlation.

# # Comparative Analysis

# In[27]:


pivot_data.tail()


# In[22]:


# Calculating the percentage change in closing prices
percentage_change = ((pivot_data.iloc[-1] - pivot_data.iloc[0]) / pivot_data.iloc[0]) * 100

fig = px.bar(percentage_change,
             x=percentage_change.index,
             y=percentage_change.values,
             labels={'y': 'Percentage Change (%)', 'x': 'Ticker'},
             title='Percentage Change in Closing Prices')

# Show the plot
fig.show()


# * The bar chart and the accompanying data show the percentage change in the closing prices of the stocks from the start to the end of the observed period:
# 
#     * MSFT: The highest positive change of approximately 16.10%.
#     * AAPL: Exhibited a positive change of approximately 12.23%. It indicates a solid performance, though slightly lower than MSFT’s.
#     * GOOG: Showed a slight negative change of about -1.69%. It indicates a minor decline in its stock price over the observed period.
#     * NFLX: Experienced the most significant negative change, at approximately -11.07%. It suggests a notable decrease in its stock price during the period.

# # Daily Risk Vs. Return Analysis

# In[29]:


daily_returns = pivot_data.pct_change().dropna()

# Recalculating average daily return and standard deviation (risk)
avg_daily_return = daily_returns.mean()
risk = daily_returns.std()

# Creating a DataFrame for plotting
risk_return_df = pd.DataFrame({'Risk': risk, 'Average Daily Return': avg_daily_return})


# In[36]:


risk_return_df


# In[37]:


fig = go.Figure()

# Add scatter plot points
fig.add_trace(go.Scatter(
    x=risk_return_df['Risk'],
    y=risk_return_df['Average Daily Return'],
    mode='markers+text',
    text=risk_return_df.index,
    textposition="top center",
    marker=dict(size=10)
))

# Update layout
fig.update_layout(
    title='Risk vs. Return Analysis',
    xaxis_title='Risk (Standard Deviation)',
    yaxis_title='Average Daily Return',
    showlegend=False
)

# Show the plot
fig.show()


# So, AAPL shows the lowest risk combined with a positive average daily return, suggesting a more stable investment with consistent returns. GOOG has higher volatility than AAPL and, on average, a slightly negative daily return, indicating a riskier and less rewarding investment during this period.
# 
# MSFT shows moderate risk with the highest average daily return, suggesting a potentially more rewarding investment, although with higher volatility compared to AAPL. NFLX exhibits the highest risk and a negative average daily return, indicating it was the most volatile and least rewarding investment among these stocks over the analyzed period.

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Stock Market Comparison Analysis

# * Stock Market Comparison Analysis is the process of evaluating and comparing the performance of multiple stocks or financial instruments within the stock market. It aims to provide insights into how different stocks have performed relative to each other and the broader market indices. So, if you want to learn how to compare the stock prices of different companies.

# # Stock Market Comparison Analysis: Process We Can Follow

# In[1]:


import pandas as pd
import yfinance as yf
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"


# In[2]:


# Now collect the stock price data
# Define the tickers for Apple and Google
apple_ticker = 'AAPL'
google_ticker = 'GOOGL'

# Define the date range for the last quarter
start_date = '2023-07-01'
end_date = '2023-09-30'

# Fetch historical stock price data using yfinance
apple_data = yf.download(apple_ticker, start=start_date, end=end_date)
google_data = yf.download(google_ticker, start=start_date, end=end_date)


# In[3]:


# Calculate daily returns
apple_data['Daily_Return'] = apple_data['Adj Close'].pct_change()
google_data['Daily_Return'] = google_data['Adj Close'].pct_change()


# In[4]:


# Create a figure to visualize the daily returns
fig = go.Figure()

fig.add_trace(go.Scatter(x=apple_data.index, y=apple_data['Daily_Return'],
                         mode='lines', name='Apple', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=google_data.index, y=google_data['Daily_Return'],
                         mode='lines', name='Google', line=dict(color='green')))

fig.update_layout(title='Daily Returns for Apple and Google (Last Quarter)',
                  xaxis_title='Date', yaxis_title='Daily Return',
                  legend=dict(x=0.02, y=0.95))

fig.show()


# In[5]:


# Calculate cumulative returns for the last quarter
apple_cumulative_return = (1 + apple_data['Daily_Return']).cumprod() - 1
google_cumulative_return = (1 + google_data['Daily_Return']).cumprod() - 1

# Create a figure to visualize the cumulative returns
fig = go.Figure()

fig.add_trace(go.Scatter(x=apple_cumulative_return.index, y=apple_cumulative_return,
                         mode='lines', name='Apple', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=google_cumulative_return.index, y=google_cumulative_return,
                         mode='lines', name='Google', line=dict(color='green')))

fig.update_layout(title='Cumulative Returns for Apple and Google (Last Quarter)',
                  xaxis_title='Date', yaxis_title='Cumulative Return',
                  legend=dict(x=0.02, y=0.95))

fig.show()


# In[7]:


apple_data.head()


# In[8]:


google_data.head()


# # Volatility of Apple and Google:

# In[9]:


# Calculate historical volatility (standard deviation of daily returns)
apple_volatility = apple_data['Daily_Return'].std()
google_volatility = google_data['Daily_Return'].std()


# In[21]:


# Create a figure to compare volatility
fig = go.Figure()
fig.add_bar(x=['Apple', 'Google'], y=[apple_volatility, google_volatility],
           text=[f'{apple_volatility:.4f}', f'{google_volatility:.4f}'],
           textposition='auto', marker=dict(color=['blue','green']))
fig.update_layout(title='Volatility Comparison (Last Year)',
                 xaxis_title='Stock', yaxis_title='Volatility (Standard Deviation)', 
                 bargap=0.7)
fig.show()


# We first calculated the historical volatility for both Apple and Google stocks. Volatility is a measure of how much the stock’s price fluctuates over time. In this case, we are calculating the standard deviation of daily returns to measure the volatility. Then we visualized the calculated volatility to assess and compare the volatility or risk associated with both Apple and Google stocks during the specified period. We can see that Google’s volatility is higher than Apple’s.
# 
# * It indicates that Google’s stock price experienced larger price fluctuations or greater price variability over the last quarter. Here’s what this difference in volatility may indicate:
# 
#     * Google’s stock is considered riskier compared to Apple. Investors generally associate higher volatility with higher risk because it implies that the stock price can change significantly in a short period.
#     * Google’s stock may be more sensitive to market conditions, economic factors, or company-specific news and events. This heightened sensitivity can result in larger price swings.
#     * Traders and investors with a higher risk tolerance might find Google’s stock appealing if they are looking for opportunities to profit from short-term price movements

# # Now let’s compare the stock market of Google and Apple according to the stock market benchmark:

# In[22]:


market_data = yf.download('^GSPC', start=start_date, end=end_date)  # S&P 500 index as the market benchmark


# In[23]:


market_data.head()


# In[24]:


market_data['Daily_Return'] = market_data['Adj Close'].pct_change()
market_data.head()


# In[25]:


# Calculate Beta for Apple and Google
cov_apple = apple_data['Daily_Return'].cov(market_data['Daily_Return'])
var_market = market_data['Daily_Return'].var()

beta_apple = cov_apple / var_market

cov_google = google_data['Daily_Return'].cov(market_data['Daily_Return'])
beta_google = cov_google / var_market


# In[27]:


# Compare Beta values
if beta_apple > beta_google:
    conclusion = "Apple is more volatile (higher Beta) compared to Google."
else:
    conclusion = "Google is more volatile (higher Beta) compared to Apple."

# Print the conclusion
print("Beta for Apple:", beta_apple)
print("Beta for Google:", beta_google)
print(conclusion)


# In the above code, we are assessing how sensitive Apple and Google stocks are to overall market movements, providing insights into their relative volatility and risk about the broader U.S. stock market represented by the S&P 500 index.
# 
# The Standard & Poor’s 500, often referred to as the S&P 500, is a widely recognized stock market index in the United States. The S&P 500 index includes 500 of the largest publicly traded companies in the United States, chosen for their market capitalization, liquidity, and industry representation. These companies span various sectors of the U.S. economy and provide a comprehensive view of the health and performance of the stock market.
# 
# In the above output, the beta value for Apple is approximately 1.2257. This beta value suggests that Apple’s stock is estimated to be approximately 22.57% more volatile or sensitive to market movements (as represented by the S&P 500 index) compared to the overall market. The beta value for Google is approximately 1.5303. This beta value suggests that Google’s stock is estimated to be approximately 53.03% more volatile or sensitive to market movements.
# 
# A beta greater than 1 suggests that a stock tends to be more volatile than the market. In this case, both Apple and Google have beta values greater than 1, indicating that they are expected to be more volatile and sensitive to market movements. Google’s higher beta value (1.5303) compared to Apple’s (1.2257) suggests that Google’s stock is estimated to have a higher degree of market sensitivity or risk compared to Apple. Investors should consider this information when making investment decisions, as higher-beta stocks can provide greater potential for returns but also carry a higher level of risk.

# # Summary
# So this is how you can perform Stock Market Comparison Analysis using Python. Stock Market Comparison Analysis is a methodical examination of multiple stocks or financial assets within the stock market. It involves analyzing the performance of various stocks or assets to gain insights into how they have fared relative to each other and the broader market. It helps investors, financial analysts, and decision-makers make informed investment decisions.

# In[ ]:





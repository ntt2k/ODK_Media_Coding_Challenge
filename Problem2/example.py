# README
# Install Pytrends
# 'pip install pytrends'
# Put in your Google username and password
# Not actually completed! I got tied up with other work at the moment. 
# Sorry, no time to do more on this problem! ... 


from pytrends.request import TrendReq

# enter your own credentials
google_username = "XXX@gmail.com"
google_password = "XXXXX"
path = "."

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')

# Create payload related to "Korean Drama" in range of from Past day to now
pytrend.build_payload(kw_list=['Korean Drama'], timeframe='now 1-d')


# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print("\nRelated Queries, returns a dictionary of dataframes:")
print(related_queries_dict)



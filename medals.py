# -*- coding: utf-8 -*-
"""
@author: Nj_neeraj
"""

import pandas
medals_df = pandas.read_csv('medal.csv')
medals_df.head()
medals_df.tail()


"""
prune the tail that doesn't contain data for use
"""
medals_df = medals_df.dropna()
medals_df.tail()

#sort the data by country, year, event, and type of medal. 1 sorts ascendingly and 0 sorts descendingly.

medals_df.sort(['NOC', 'Year', 'Event', 'Medal'], ascending=[1, 1 ,1 ,0])

#time period does the data apply to
medals_df.Year.min(), medals_df.Year.max()

# only those rows of years that have medals data
medals_df.Year.unique()

#no. of medals awarded.
len(medals_df)

#sanity check on no. of medals distict in colors. and their count
medals_df.Medal.unique()
medals_df.Medal.value_counts()

#list all the winter olympic sports and disciplines that have awarded medals
discipline = medals_df.groupby(['Sport','Discipline'])
discipline.groups.keys()

#Which discipline and event has awarded the most gold medals?
gold_df = medals_df[medals_df.Medal == 'Gold']
by_event = gold_df.groupby(['Discipline','Event'])

#no. of gold by events
golds_by_event = by_event.Medal.count()

#otp 10 events in descending order
golds_by_event.sort(ascending=False)
golds_by_event.head(10)

#country that has won the most gold, silver, and bronze medals?
medals_by_country = medals_df.groupby(['NOC','Medal']).size()
# We calculate the medal counts for each group using the resulting DataFrame's size() function, which gives us the number of rows in each group
medals_by_country.head(10)
#convert series to data frame
medals_by_country_df = medals_by_country.unstack()
medals_by_country_df.head()

#countries with no medals of each color
medals_by_country_df.fillna(0, inplace=True)

# we use idxmax(), which gives us the index (in this case, the country code) corresponding to the maximum count for each medal color (column in our DataFrame).
medals_by_country_df.idxmax()

"""
plotting
"""

import matplotlib
%matplotlib inline
medals_by_country_df.sort('Gold', ascending=False, inplace=True)

#Now we can use the DataFrame plot() function to produce our plot. We plot individual medal counts for the top 15 countries.
medals_by_country_df[['Gold','Silver','Bronze']][:15]\
.plot(kind='bar', figsize=(12,10))

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



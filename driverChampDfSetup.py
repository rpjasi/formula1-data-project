import pandas as pd
import numpy as np 

#Set up variables for data scraping from url
url_template = 'https://www.statsf1.com/en/{year}.aspx'
results = {}
years = [i for i in range(2019,1990,-1)]
for yr in years:
    #cleaning and reorganising data 
    df = pd.read_html(url_template.format(year=yr))
    raw_data = df[0]
    raw_data = raw_data.drop([0])
    raw_data = raw_data.drop([0], axis=1)
    raw_data.insert(0, 'Year', yr)
    header = [x for x in range(len(raw_data.columns))]
    header.insert(0, 'Year')
    header[1] = 'Driver'
    header.pop(-1)
    header[-1] = 'Points'
    raw_data.columns = header
    results[yr] = raw_data

driverChamp = pd.concat([results[i] for i in results.keys()])
driverChamp.to_csv('driverChamp.csv')

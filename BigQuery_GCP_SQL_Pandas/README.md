# Overview

#### Problem statement

#### Summary of results

## Part I
#### Initial queries
- What's the size of this dataset? (i.e., how many trips)
    '''SELECT COUNT( trip_id )
FROM `bigquery-public-data.san_francisco.bikeshare_trips` '''
    * 983,648 trips
- What is the earliest start date and time and latest end date and time for a trip?
    '''SELECT min( start_date ), max( end_date )
FROM `bigquery-public-data.san_francisco.bikeshare_trips` '''
    * Earliest start date & time: 2013-08-29 09:08:00 UTC
    * Latest start date & time: 2016-08-31 23:48:00 UTC
- How many bikes are there?
    '''SELECT COUNT( distinct bike_number ) as total_bikes
FROM `bigquery-public-data.san_francisco.bikeshare_trips` '''
    * 700 bikes total
#### Questions of your own

#### Bonus activity

- What deals do you offer though? Currently, your company has several options which can change over time.  Please visit the website to see the current offers and other marketing information. Frequent offers include: 
  * Single Ride 


#### Summary of recommendations 

#### Tools
- BigQuery
- Ipynb
- Command Line 
- 

#### Link to code

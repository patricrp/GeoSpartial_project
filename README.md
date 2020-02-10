# geo_project

Find the best location for your new business office. Consider your workers desires: 

1. Developers want to be near successful tech startups which raised more than $1M.
2. Account managers need to travel a lot, so there might be airports and train stations. 
3. Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
4. Executives like Starbucks A LOT. Ensure there's a starbucks not to far.

Solution:

1. Filter the crunchbase database to look for startups founded after 2003, accomplishing that 'Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.'
Look for startups founded before 2003.

There are 9.297 companies founded after 2003 and 3.839 founded before. There are 5.665 companies without founded year declared.

2. Filter tech startups that raised more than $1M. Look for tech startups on the category_code and (despite the total raised money amount should be greated than $1M), I selected raised_amount greater or equal to 1000000 in a round. Later I'll try to aggreate data from all the funding_round. 

3. Import Starbucks location dataset and create a DataFrame.

4. Import Airports csv and create a DataFrame

5. Create a DataFrame with companies founded before 2003.

4. Explode offices serie, as JSON, to different rows to see different offices of a company.

5. Expand offices into different series to have address, city, zip code, latitude and longitude separately. Concatenate both DataFrames.

5. Cleaning DataFrames dropping unnecessary columns and null values for latitude and longitude.

6. Create a GEOJSON - type point.

7. Transform de DataFrame into a GeoDataFrame

8. Select 3 cities from the original DataFrame based on the number of value_counts of startups in the original DataFrame 

9. Filter offices DataFrame, Starbucks DataFrame and offices founded before 2003 DataFrame with cities San Francisco, New York or Mountain View.

10. Create JSON to import to MongDB with GEO

11. Create a DataFrame with number of nearest Starbucks, airports and old companies to each office. 

12. Add a new column with Ranking weighted based on number of nearby Starbucks, airports and old companies.

13. Rank DataFrame based on Ranking column and sort it descending.

14. Select the top office, paint it on a map and add Starbucks, airports and old companies to the map.



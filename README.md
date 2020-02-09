# geo_project

Find the best location for your new business office. Consider your workers desires: 

1. Developers want to be near successful tech startups which raised more than $1M.
2. Account managers need to travel a lot, so there might be airports and train stations. 
3. Some place to go to party, due to young people part of the team.

Solution:

1. Filter the crunchbase database to look for startups founded after 2003, accomplishing that 'Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.'
Look where startups founded before 2003.

There are 9.297 companies founded after 2003 and 3.839 founded before. There are 5.665 companies without founded year declared.

2. Filter tech startups that raised more than $1M. Look for tech startups on the category_code and (despite the total raised money amount should be greated than $1M), I selected raised_amount greater or equal to 1000000 in a round. Later I'll try to aggreate data from all the funding_round. 

3. Explode offices serie, as JSON, to different rows to see different offices of a company.

4. Expand offices info into different series to have address, city, zip code, latitude and longitude separately.

5. Cleaning the DataFrame dropping unnecessary columns and null values for latitude and longitude.

6. Create a GEOJSON - type point to paint later a map with the offices.

7. Transform de DataFrame into a GeoDataFrame

8. Import Starbucks location dataset and create a DataFrame.

9. Create a offices map with Starbucks markers  :(

9. 



## GeoSpartial Project - TODO's
You recently created a new company in the `GAMING industry`. The company will have the following scheme:
- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President
As a data engineer you have asked all the employees to show their preferences on where to place the new office.
Your goal is to place the **new company offices** in the best place for the company to grow.
You have to found a place that more or less covers all the following requirements.
Note that **it's impossible to cover all requirements**, so you have to prioritize at your glance.
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan
## Help
- Geospatial range Queries in MongoDB with `pymongo`
- GeoJSON Point `{ type: "Point", coordinates: [ 40, 5 ] }`
- Create sphere2d index in python with pymongo: `db.collection.createIndex( { <location field> : "2dsphere" } )`
- Query `$near` operator: https://docs.mongodb.com/manual/reference/operator/query/near/#op._S_near
## How to deliver the project
- You must justify your decision with tableau slides. Provide us the public tableau link inside a README.md
  file at dir `module-2/project-mongodb-geospartial-queries`.
- Provide `lat` and `long` for the new office proposals.
## Links & Resources
- https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/geocoding-reverse
- https://docs.mongodb.com/manual/geospatial-queries/
- https://developers.google.com/maps/documentation/geocoding/intro
- https://developers.google.com/maps/documentation/geocoding/start
- https://data.crunchbase.com/docs
- https://developers.google.com/places/web-service/search
- https://www.youtube.com/watch?v=PtV-ZnwCjT0

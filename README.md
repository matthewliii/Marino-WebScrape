I made this project to optimize my schedule and not provide myself any excuses for going to the gym anymore.
Being able to see a visualization of when people go to these facilities has helped me identify the best time to go and work my schedule around them.
The data is being scraped in 30 minute intervals from the Northeastern Campus Recreation Website which has employee reported data regarding the counts of people at each facility.

Here are the technologies that are being used:

Backend: 
Flask app for handling requests and generating a matplotlib graph from the scraped data which is hosted on Render
Webscraper built with beautiful soup and Pandas deployed on GitHub Actions using a Cron Job Scheduler

Frontend: 
React app hosted on Vercel

Please Experiment with this app here:
https://marino-scrape.vercel.app/

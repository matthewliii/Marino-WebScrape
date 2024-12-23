# Marino Facility Usage Tracker

This project was created to help optimize my schedule and eliminate excuses for skipping the gym. By visualizing when people use these facilities, I’ve been able to identify the best times to go and plan my schedule accordingly.

The app scrapes data from the Northeastern Campus Recreation Website every 30 minutes, which reports employee-provided data on the number of people at each facility. This information is then processed and presented in an intuitive, interactive format.

## Features

- **Real-time Visualization**: See usage trends across various gym facilities.
- **Data-Driven Scheduling**: Plan your gym visits during off-peak hours.
- **Fully Automated**: Data is automatically scraped and updated at regular intervals.

---

## Technologies Used

### **Backend**

- **Flask**: Handles API requests and generates graphs using Matplotlib.
- **Beautiful Soup & Pandas**: Scrape and process data from the Northeastern Campus Recreation Website.
- **GitHub Actions**: Automates the web scraping process with a Cron Job Scheduler.
- **Hosting**: The Flask backend is hosted on [DigitalOcean](https://www.digitalocean.com/).

### **Frontend**

- **React**: Provides a dynamic and responsive user interface.
- **Hosting**: The React app is deployed and hosted on [Vercel](https://vercel.com).

---

## How to Use

Experiment with the app and discover the best times to visit the gym!  
👉 [Try it out here!](https://marino-scrape.vercel.app/)

---

### Why This Project?

By providing a clear, data-driven visualization of facility usage, this app helps users plan their fitness routines effectively and without uncertainty. Whether you’re looking to avoid crowds or fit the gym into a busy schedule, this tool ensures you can always make informed decisions.

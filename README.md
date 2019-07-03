# bloomies-web-scraper
Scrapes Bloomingdales.com's website for product data. 

## Prerequisites

 + Anaconda 3.7

 + Python 3.7

 + Pip

 Environment Setup Create and activate a new Anaconda virtual environment:

 conda create -n stocks-env python -3.7 # (first time only) conda activate stocks-env From within the virtual environment, install the required packages below:

  + csv
  + requests
  + bs4

 ## Setup

Make sure to have a valid internet connection and install all of the necessary prerequisites!

## Finding a valid Category Code

There are a number of different ways to find a valid category code. The easiest is to simply navigate to a category page (a page that shows multiple products) and look at the url. Right after the ?id= is the category code!

 ## Usage

 To run the program: 

 '''
 python app/web-scraper.py
 '''


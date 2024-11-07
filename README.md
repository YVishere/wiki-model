Author:  Aditya Yellapuntula Venkata

A program to create a dataset of nouns based on weights = [Absolute Importance, Relative Importance] scraped from Wikipedia website and using hyperlinks.
All elements in the scraped array is considered as a keyword and the indices determine relative importance using the formula w = baseW / (index^1/k), where k is some constant and baseW is the relative importance of the root word with respect to its own root word.

A short description of files:
something.ipynb: Used  for testing code in Jupyter notebook
main.py: Master file which calls all commands
Scraper.py: Helper file to scrape through wikipedia. If fast fast scrape is enabled, only return the number of keywords in the given wikipedia page
Slave.py: Helper file for Multiprocess related commands.

Possible algorithm:
~~Parellel process on a constant number of links per wikipedia page --- Adds more importance on filtering out non noun wikipedia links.~~

# SwissBau Scaper
A simple Scraper to get all Exhibitors of the SwissBau-Trade Fare


## Setup

Before you can start scraping you have to make sure that pip is installed:
(this command works on most linux distros)
```
sudo apt-get install python-pip
```


After that you can install BeautifulSoup with pip:
```
pip install bs4
```



## Usage
Start the script and type in the total number of the Exhibitor-Pages
After that the data gets downloaded and written to a CSV file


**Attention:**

To open the CSV file correctly make sure to use the semicolons as separating-option!


## Output

The Data will be formated into following output:

(company_name; country; link)


## Usecase

If you are using a Linux machine you can easily make this script executable.

Include following code in the first line of the scaper.py script:
```
#!/usr/bin/env python3
```

Then make the scraper.py script executable with following command in the terminal:
```
chmod +x scraper.py
```

After that you can simply add a shortcut on your desktop or start it with:
```
./scraper.py
```

# SwissBau Scaper
A simple scraper to get all Exhibitors of the SwissBau-Trade Fare


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
Start the scraper.py script to get all url and company names

After that you can complete A lot of the profile details with the details_scraper.py


**Attention:**
To open the CSV file correctly make sure to use the semicolons as separating-option!


## Output

The Data will be formated into following CSV-Output:

[link; company_name; adress; postal; city; country; phone; website; contact_name; contact_position; contact_link]


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


## Optional

If you want to automatically delete the buffer and/or start the details_scraper include the os.system comment at the end of the given file:

```
#os.system("python3 details_scraper.py"
```

```
#os.system("rm buffer.csv")

```

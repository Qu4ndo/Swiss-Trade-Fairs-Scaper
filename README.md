# SwissBau Scaper
A simple scraper to grab all Exhibitors of some Swiss Fares


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
Start the scraper.py script with:
```
python3 scraper.py
```
Or with the steps under Usecase.

Choose your fare from the list (with numbers)!


**Attention:**
To open the CSV file correctly make sure to use the semicolons as separating-option!


## Output

The Data will be formated into following CSV-Output:

[link; company_name; adress; postal; city; country; phone; website; contact_name; contact_position; contact_link]


## Optional

If you want do not want to automatically delete the buffer you have to exclude the os.system comment at the end of the scraper.py file:

```
#os.system("rm buffer.csv")

```


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

## Web scraper using Beautiful Soup

#### Scope
In this project - I am practicing web scraping objects and saving them down into CSV for data analysis.

Scraping is website specific & not generic. In this case I used https://www.money.co.uk mortgage section.

#### Pre-requisites

Make sure you have the latest version of python and pip

```
python3 --version
which pip3
```

in my case now is `3.7.5` & `/usr/local/bin/pip3`

Install the requirements, included is:
- `bs4` - beautiful soup (reverse HTML content in python)

```
pip3 install -r requirements.txt
```

#### Download the Repository & execute the script

```
git clone "https://github.com/JayFarei/webscraping_beautiful_soup.git"
```

```
cd webscraping_beautiful_soup
```
```
python3 webscraper.py
```

#### Notes:

**About HTML:** - I have used [https://htmlformatter.com](https://htmlformatter.com) to make sense of the HTML that was scraped - I saved the outcome in `extract.html`. That should is an example of the scraped HTML section defined in the script as `offerDescription` - with that you'll be able to make sense of the scraping for each variable.

**About REGEX:** I have used REGEX to parse the numbers in the right format from the text contained in the HTML - I found a really useful webpage to test the configuration of the function: [regex101.com](https://regex101.com/r/hU4vO7/12)

**About BeautifulSoup:** - worth noting that the outcome of the function page_soup.find_all is a list (in their format) - irrespective if there is only one entry or not.

**About exporting in CSV:** - I had to remove `,` from numbers > 999 to avoid pagination issues.

**About selenium**:
Key actions:
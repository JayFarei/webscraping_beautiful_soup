from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

# Target scraping URL
my_url = 'https://www.money.co.uk/mortgages/first-time-buyer-mortgages.htm'

# Export Target
fileName = "mortgages.csv"
f = open(fileName, "w")
headers = "offerName , fixedRate in % , variableRate in % , totalCost in % , teaserPayment in £  , ongoingPayment in £ , teaserPeriod in £\n"
f.write(headers)

# Open connection using urlopen
uClient= uReq(my_url)

# Saving it down
page_html = uClient.read()

# Close web uClient
uClient.close()

# Need to parse the HTML
page_soup = soup(page_html, "html.parser")

# Grab each mortgage name
offerName_ResultSet = page_soup.find_all("div",{"class": "ctName"})
# It puts them in an array
# check the lenght with len(offerName) / check the first entry with offerName[0]

# Grab each mortgage details
offerDescriptions = page_soup.find_all("div",{"class": "ctCols ctCols-4"})
# to identify the data I want to scrape / copy the outcome of offerDescription[1] in https://htmlformatter.com / copy it in Atom & identify the classes I need.

# For testing purposes: offerDescription = offerDescriptions[0]

i = -1
for offerDescription in offerDescriptions:
    i = i+1
    offerName=offerName_ResultSet[i].text
    ## obtaining the soup
    offerValue_ResultSet = offerDescription.find_all("div", { "class" : "ctColVal" })

    # obtaining teaser rate | type=float
    fixedRateSentence = offerValue_ResultSet[0].text
    fixedRate_ResultSet=re.findall(r"[-+]?\d*\.\d+|\d+",fixedRateSentence)
    fixedRate = float(fixedRate_ResultSet[0])/100

    # obtaining variable rate  | type=float
    variableRateSentence = offerValue_ResultSet[1].text
    variableRate_ResultSet=re.findall(r"[-+]?\d*\.\d+|\d+",variableRateSentence)
    variableRate = float(variableRate_ResultSet[0])/100

    # obtaining total cost rate | type=float
    totalCostSentence = offerValue_ResultSet[2].text
    totalCost_ResultSet=re.findall(r"[-+]?\d*\.\d+|\d+",totalCostSentence)
    totalCost = float(totalCost_ResultSet[0])/100

    # Parsing monthly payment column
    monthlyPayment_ResultSet = offerValue_ResultSet[3].find_all("span", { "class" : "emphasis" })

    # extracting ongoing payement | type=float
    ongoingPaymentSentence = monthlyPayment_ResultSet[1].text
    ongoingPayment_ResultSet=re.findall(r"(\d[0-9,.]+)",ongoingPaymentSentence)
    ongoingPayment = ongoingPayment_ResultSet[0]

    # extracting teaser payment and period | type=float
    teaser = offerValue_ResultSet[3].find_all("span", { "class" : "primary" })
    teaserSentence = teaser[0].text
    teaserNumbers = re.findall(r"(\d[0-9,.]+)",teaserSentence)
    teaserPeriod = float(teaserNumbers[1])
    teaserPayment = float(teaserNumbers[0])

    print(">>> offerName : " + str(offerName) )
    print("fixedRate in % : " + str(fixedRate) )
    print("variableRate in % : " + str(variableRate) )
    print("totalCost in % : " + str(totalCost) )
    print("teaserPayment in £ : " + str(teaserPayment) )
    print("ongoingPayment in £ : " + str(ongoingPayment) )
    print("teaserPeriod in £  : " + str(teaserPeriod) )

    f.write(offerName + "," + str(fixedRate) + "," + str(variableRate) + "," + str(totalCost) + "," + str(teaserPayment) + "," + ongoingPayment.replace("," , "") + "," + str(teaserPeriod) + "\n")

# StockMarket X Coronavirus Relationship 

## Abstract:
The purpose of this script is to determine how the markets are reacting to the recent coronavirus outbreak. The script currently looks at two markets the **SPY**(Designed to track the S&P 500 stock market index. This fund is the largest ETF in the world). As well as the **MCHI** iShares China ETF(Designed to track the large and mid-sized companies in China. This ETF seeks to track the investment results of an index composed of Chinese equities that are available to international investors.)

## Running The Script:
To Run this scipt simply download the .py file titled "Market_Relationship.py". After the python file has been successfully downloaded, ensure Python has the following modules installed: Pandas, Matplotlib, yfinance. If any of these modules are missing, please go to terminal and install them using the pip command: "pip install pandas" , "pip install matplotlib", "pip install yfinance". 

## Output--Twin Axis Plot:
From the script, a twin axis plot is created with one Y-axis counting the number of coronavirus cases around the world, the other Y-axis measuring the change in the normalized closing prices of the two different market ETFs. The X-axis of the twin axis plot is the date value. Normalized values are used for the market ETFS as it allows for quantifying the difference in the closing prices of the two differnt ETFs(SPY & MCHI) as they have differenct market prices. They way the market ETF close prices are normalized is by using the respective market ETF's close price on the date of 2020-01-21 as the baseline and divinding that ETF's close prices for all dates including and after 2020-01-21 by that close price. Once this done, the normalized values for both ETFs are obtained and can be compared comparatively from the date 2020-01-21 and after. 

![alt text](https://github.com/akalia25/StockMarket_Virus_Relationship/blob/master/Screenshots/Market_Virus_Relationship.png)

## Recommendations/Conclusion:
From the output of this script, we are able to identify an ***inverse relationship between the market indexes observed(SPY & MCHI) and the number of cases of the coronavirus.*** As the number of coronavirus cases are increasing the market indexes observerd are decreasing in value(close price). What is interesting to note is that the SPY market has a slower decrease in value in comparison to the MCHI ETF. This is due to the fact that the companies most directly affected by this virus outbreak are geographically located in China, therefore the ETFs that track Chinese equities like the MCHI are facing a much higher impact in value than ETFs tracking equities in the USA(SPY). However, overall the general markets around the world are suffering from the virus outbreak, those more close to the outbreak are affected more. The purpose of this analysis is to examine how epidemics like the coronavirus can directly impact the stock market, and to what extent the markets are impacted.

## Please Help Out!
If you are able to financially help out, please consider donating to foundations that are immediately trying to assist in combating this epidemic we are facing that is known as the coronavirus.
https://ca.gofundme.com/f/ch8bf-medical-supplies-for-wuhan



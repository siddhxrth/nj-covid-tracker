# Siddharth Lohani
# 2/22/2021

# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# schedule imports
import schedule
import time
from datetime import date

# settings import
import settings

# twitter api wrapper import
import tweepy

# set up chrome
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

#set up selenium
driver = webdriver.Chrome(options=chrome_options)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

def fetchDataAndTweet():

    print("function called")

    today = date.today()

    d = today.strftime("%B %d, %Y")

    # fetch the link with covid cases
    driver.get("https://projects.nj.com/coronavirus-tracker/")

    time.sleep(20)

    newCases = driver.find_element(By.XPATH, '//*[@id="day-cases-disp"]/div[2]').text

    totalCases = driver.find_element(By.XPATH, '//*[@id="cum-cases-disp"]/div[2]').text

    newDeaths = driver.find_element(By.XPATH, '//*[@id="day-deaths-disp"]/div[2]').text

    totalDeaths = driver.find_element(By.XPATH, '//*[@id="cum-deaths-disp"]/div[2]').text

    newTests = driver.find_element(By.XPATH, '//*[@id="day-tests-disp"]/div[2]').text

    totalTests = driver.find_element(By.XPATH, '//*[@id="cum-tests-disp"]/div[2]').text

    todaysPositivity = driver.find_element(By.XPATH, '//*[@id="day-pos-disp"]/div[2]').text

    overallPositivity = driver.find_element(By.XPATH, '//*[@id="cum-pos-disp"]/div[2]').text


    firstLine = "#COVID updates for " + d + ": \n \n"

    newCasesLine = "new cases: " + newCases + "\n"

    totalCasesLine = "total cases: " + totalCases + "\n \n"
    
    newDeathsLine = "new deaths: " + newDeaths + "\n"

    totalDeathsLine = "total deaths: " + totalDeaths + "\n \n"

    newTestsLine = "new tests: " + newTests + "\n" 

    totalTestsLine = "total tests: " + totalTests + "\n \n"

    todaysPositivityLine = "today's positivity: " + todaysPositivity

    overallPositivityLine = "overall positivity: " + overallPositivity + "\n"

    message = firstLine + newCasesLine + totalCasesLine + newDeathsLine + totalDeathsLine + newTestsLine +  totalTestsLine + overallPositivityLine
    
    print(message)

    # tweet the update
    api.update_status(message)

    print("TWEETED")

fetchDataAndTweet()

schedule.every().day.at(settings.WHEN_TO_RUN).do(fetchDataAndTweet)

while True:
    schedule.run_pending()
    time.sleep(1)

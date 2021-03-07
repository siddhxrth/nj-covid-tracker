# Siddharth Lohani -> Forked by @carcraftz
# 2/22/2021


# schedule imports
import schedule
import time
from datetime import date
import requests

# settings import
import settings

# twitter api wrapper import
import tweepy



# Authenticate to Twitter
auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

def fetchDataAndTweet():
		countr = requests.get("https://projects.nj.com/coronavirus-tracker/data/counts.json")
		countjson = countr.json()[-1]
		totalCases = countjson["Total state cases"]
		newCases = countjson["New cases in state"]
		deathr = requests.get("https://projects.nj.com/coronavirus-tracker/data/deaths.json")
		deathjson = deathr.json()[-1]
		totalDeaths = deathjson["STATE TOTAL-MUST MATCH D"]
		newDeaths = deathjson["New deaths"]
		testsr = requests.get("https://projects.nj.com/coronavirus-tracker/data/tests.json")
		testsjson = testsr.json()[-1]
		totalTests = testsjson["Total Tests"]
		hospitalr = requests.get("https://covidtracking.com/page-data/data/page-data.json")

		hospitaljson = hospitalr.json()["result"]["data"]["allCovidState"]
		totalHospitalized = ""
		newHospitalized = ""
		for statedata in hospitaljson["nodes"]:
			if(statedata["state"] =='NJ'):
				totalHospitalized = str(statedata["hospitalizedCumulative"])
				newHospitalized = str(statedata["hospitalizedCurrently"])
		#TODO: figure out how to get new tests (prob need to access site on a weekday)
		newTests = "0"
		todaysPositivity = "0"
		overallPositivity = str(round(int(totalCases)/int(totalTests)*100,3))+"%"
		today = date.today()
		d = today.strftime("%B %d, %Y")
		
		firstLine = "#COVID updates for " + d + ": \n \n"
		newCasesLine = "new cases: " + newCases + "\n"
		totalCasesLine = "total cases: " + totalCases + "\n \n"
		newDeathsLine = "new deaths: " + newDeaths + "\n"
		totalDeathsLine = "total deaths: " + totalDeaths + "\n \n"
		newTestsLine = "new tests: " + newTests + "\n" 
		totalTestsLine = "total tests: " + totalTests + "\n \n"
		totalHospitalizedLine = "total hospitalized: " + totalHospitalized + "\n" 
		newHospitalizedLine = "new hospitalized: " + newHospitalized + "\n\n" 
		todaysPositivityLine = "today's positivity: " + todaysPositivity
		overallPositivityLine = "overall positivity: " + overallPositivity + "\n"
		message = firstLine + newCasesLine + totalCasesLine + newDeathsLine + totalDeathsLine + newTestsLine + totalTestsLine + totalHospitalizedLine + newHospitalizedLine +  overallPositivityLine
		print(message)

    # tweet the update
		api.update_status(message)

fetchDataAndTweet()

schedule.every().day.at(settings.WHEN_TO_RUN).do(fetchDataAndTweet)

while True:
    schedule.run_pending()
    time.sleep(1)

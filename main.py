# Siddharth Lohani
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
try:
	auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
	auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
except:
	print("error authenticating with twitter")

def fetchDataAndTweet():

	totalStatsr = requests.get("https://services7.arcgis.com/Z0rixLlManVefxqY/arcgis/rest/services/survey123_cb9a6e9a53ae45f6b9509a23ecdf7bcf/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=CreationDate%20desc&resultOffset=0&resultRecordCount=1&resultType=standard&cacheHint=true").json()
	totalProbableCasesr = requests.get("https://services7.arcgis.com/Z0rixLlManVefxqY/arcgis/rest/services/DailyCaseCounts/FeatureServer/0/query?f=json&where=COUNTY%20IS%20NOT%20NULL&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22TOTAL_AG_CASES%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&resultType=standard&cacheHint=true").json()
	newCasesr = requests.get("https://services7.arcgis.com/Z0rixLlManVefxqY/arcgis/rest/services/DailyCaseCounts/FeatureServer/0/query?f=json&where=OBJECTID%20IS%20NOT%20NULL&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22NEW_PCR_CASES%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&resultType=standard&cacheHint=true").json()
	newDeathsr = requests.get("https://services7.arcgis.com/Z0rixLlManVefxqY/arcgis/rest/services/DailyCaseCounts/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22NEW_DEATHS%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&outSR=102100&resultType=standard&cacheHint=true").json()

	d = date.today().strftime("%B %d, %Y")

	header = "#COVID19 updates for " + d + ": \n \n"
	
	# cases
	newCases = "new cases: " + str(newCasesr['features'][0]['attributes']['value']) + "\n"

	totalConfirmedCases = totalStatsr['features'][0]['attributes']['total_positives']
	totalProbableCases = totalProbableCasesr['features'][0]['attributes']['value']

	totalCases = "total cases: " + str(totalConfirmedCases+totalProbableCases) + " (" + str(totalConfirmedCases) + " confirmed, " + str(totalProbableCases) + " probable)" + "\n"

	# deaths
	newDeaths = "new deaths: " + str(newDeathsr['features'][0]['attributes']['value']) + "\n"
	totalDeaths = "total deaths: " + str(totalStatsr['features'][0]['attributes']['total_deaths']) + "\n"

	# hospitalizations
	totalHospitalized = ""
	currentHospitalized = ""

	hospitalr = requests.get("https://covidtracking.com/page-data/data/page-data.json")

	data = hospitalr.json()["result"]["data"]["allCovidState"]

	for stateData in data["nodes"]:

		if(stateData["state"] == "NJ"):
			totalHospitalized = "total hospitalized: " + str(stateData["hospitalizedCumulative"]) + "\n"
			currentHospitalized = "current hospitalized: " + str(stateData["hospitalizedCurrently"]) + " (" + str(stateData['inIcuCurrently']) + " in ICU, " + str(stateData['onVentilatorCurrently']) + " on ventilator)" + "\n"
	
	# rate of transmission
	rateOfTransmission = "transmission rate: " + str(totalStatsr['features'][0]['attributes']['rate_of_transmission_rt'])


	tweet = header + newCases + totalCases + "\n" + newDeaths + totalDeaths + "\n" + currentHospitalized + totalHospitalized + "\n" + rateOfTransmission


	print(tweet)

	api.update_status(tweet)

	print("\nTWEETED ON " + d)

schedule.every().day.at(settings.WHEN_TO_RUN).do(fetchDataAndTweet)

while True:
    schedule.run_pending()
    time.sleep(1)
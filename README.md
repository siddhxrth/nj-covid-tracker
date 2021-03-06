# New Jersey COVID-19 Tracker
#### Coronavirus tracker for the state of New Jersey. Built with Selenium, implemented in Python. Seeing that cases keep rising, it's important to be aware of the new developments in cases, vaccines, and tests.

## Setup
#### To get this web scraper running locally, the setup is very minimal. The only step is to edit the ```.env``` file with your information.

### The first step is to fill out the Twitter Developer API keys:

    API_KEY = 
    API_SECRET = 
    
    BEARER_TOKEN = 
    
    ACCESS_TOKEN = 
    ACCESS_TOKEN_SECRET =  
### You can get your own API keys from the [Twitter Developer](https://developer.twitter.com/en) page. Just create a Twitter Developer Account, and create an app. Generate its API keys, and this is important: you must give it permissions to write and read to your twitter account. Once you do that, copy the keys and paste them into their appropriate fields in the ```.env  ``` file.

### 2) Second, in the ```WHEN_TO_RUN``` field, specify when you want the program to run in 24H time. For example, if you want it to run at ```4:30 PM```, enter ```16:30```.

### 3) Last, you need to install the dependencies. Run these commands, and then you should be good to run the program!
    pip install selenium
    pip install tweepy
    pip install python-dotenv
    pip install schedule
    
### You also need Selenium installed and in your PATH. In order to learn how to do this, follow the [docs](https://selenium-python.readthedocs.io/installation.html).

# About
#### Hi! I'm Sid, a Full Stack developer currently in High School. You can learn more about me on [my website](https://siddharthlohani.dev), or you can follow me on [Twitter](https://twitter.com/sidlohani)! If you found this project helpful, star it on Github!

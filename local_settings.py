'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'HyrxSI1lStECEJ60qRibxmSKn'
MY_CONSUMER_SECRET = 'rUPAILbFDFAwsrA10RxmUzBlSDpN9pzvJGzx7wh45dw1Qu4dXK'
MY_ACCESS_TOKEN_KEY = 'Y725394666657566725-XONPTaNHM0K75S6rj1e7EW1fYGsBZB6'
MY_ACCESS_TOKEN_SECRET = '	vbUc86Pzot2q9xVI28uzIFcYjYzgtRj7sFG56DEun19Wd'

SOURCE_ACCOUNTS = ["nba"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "mattgu_ebooks" #The name of the account you're tweeting to.

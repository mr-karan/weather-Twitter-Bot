#Made by Karan Sharma
#Python Twitter Bot
#karansh.in
import tweepy
import pywapi
import time
from time import strftime

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

timenow=strftime("%d %b %Y %H:%M:%S")

result = pywapi.get_weather_from_weather_com('INXX1886', units = 'metric' )
while(True):
	timenow=strftime("%d %b %Y %H:%M:%S")
	api.update_status(status=(timenow+
		" ->It is " +result['current_conditions']['text'].lower()+" and Temp is "+result['current_conditions']['temperature'] + "C." +"Max Temp is:"+
		result['forecasts'][0]['high']+"C "+"and Min Temp is "+result['forecasts'][0]['low']+"C "+" in Dadri"))

	time.sleep(3600)
	


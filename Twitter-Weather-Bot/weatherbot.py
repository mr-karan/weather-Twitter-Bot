#Made by Karan Sharma
#Python Twitter Bot
#karansh.in
import tweepy
import pywapi
import time
from time import strftime

auth = tweepy.OAuthHandler('HHztO8jPvGbjQIxXCYG4a50xF', 'VUy76dSmwXEd2hEcfKSVQyGj4GVt3u5iUTyijQLKrXIwPhcFBL')
auth.set_access_token('3065251800-swm9cu1Z1Nbjz48wm7Zw0Ofd0R7o2og55Udn4JA', 'qUAdW0SVwd0Lcx5tgmpkZkGHoSw4S9iYuNmyqgK3EprMc')

api = tweepy.API(auth)

timenow=strftime("%d %b %Y %H:%M:%S")

result = pywapi.get_weather_from_weather_com('INXX1886', units = 'metric' )
while(True):
	timenow=strftime("%d %b %Y %H:%M:%S")
	api.update_status(status=(timenow+
		" ->It is " +result['current_conditions']['text'].lower()+" and Temp is "+result['current_conditions']['temperature'] + "C." +"Max Temp is:"+
		result['forecasts'][0]['high']+"C "+"and Min Temp is "+result['forecasts'][0]['low']+"C "+" in Dadri"))

	time.sleep(3600)
	


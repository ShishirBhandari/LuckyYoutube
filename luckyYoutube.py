#! python3
# luckyYoutube.py - opens several youtube videos from search result.

print("Lucky Youtube")

import sys						#python standard library
import requests

def search_youtube(search_term):
	print("Searching Youtube...")
	import requests										#library for getting response from webpages
	res = requests.get('https://www.youtube.com/results?search_query=' + '+'.join(search_term)		#get response from the youtube search results page.
	
	return res


try:
	if len(sys.argv) > 1:
		res = search_youtube(sys.argv[1:])					#get response from the youtube search results page.
		res.raise_for_status()								#check if the response has been downloaded from the internet
	else:
		s = input('Enter search text: ')
		sl = s.split(' ')

		res = search_youtube(sl)							#get response from the youtube search results page.
		res.raise_for_status()								#check if the response has been downloaded from the internet
except:
	print("Network Error! Quiting...")	

import webbrowser									#python standard libraries to open default web browser
import bs4											#library for manipulating html 

soup = bs4.BeautifulSoup(res.text, 'html5lib')		#make soup to parse the response using html5

linkElems = soup.select('.yt-lockup-title > a')		#select the list of 'a' (links) elements which are in class "yt-lockup-title" 

numOpen = min(5, len(linkElems))					#number of videos to open automatically (max 5 links)

for i in range(numOpen):								#runs 'numOpen' times to open numOpen videos (max 5 videos)
	hr = linkElems[i].get('href')						#extract relative link of video
	webbrowser.open('https://www.youtube.com' + hr)		#combines the extracted relative link to "youtube.com" and opens the link of the video in the browser.

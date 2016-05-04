#pip install all the packages selenium,urllib(not used but will be),bs4,MySQLdb,re 

from selenium import webdriver							
from urllib import urlencode
import urllib2
import timeit
from bs4 import BeautifulSoup
import MySQLdb
import re



"""Defines the public inteface of the API."""
driver=webdriver.Firefox()
db = MySQLdb.connect("localhost","","","" )
cursor = db.cursor()

url="https://www.google.co.in"							#open Google
driver.get(url)
ans=1
ctr=0
while(ans==1):
	curr=driver.current_url							#constantly check which url is currently open in the browser
	if('google' in curr and ctr==0):					#if the current url contains keyword "google" and ctr=0 check if user has entered some query for search and set ctr=1 m
		#m = re.search('(?<=#q)\w+', curr)
		m=re.search("#q(.*)$",curr)					#search for everything after #q
		print curr
		print m
		if(m):
			print m.group(0)					#get the value of query in the form "#q=query"
			q="""select link from search where term = "%s" """%(m.group(0))  #check if it exists in the database
			#print q
			cursor.execute(q)
			data = cursor.fetchone()
			
			ctr=1
			if(data):
				print data					# if it does print the link
			
			
	elif 'google' in curr:							#if the current url contains keyword "google" and user has searched something continue checking the url to see which link has
		continue                                                        # been opened
	else:
		ans=0
		q="""Insert into search values (null,"%s","%s")"""%(m.group(0),curr)	# if the query wasn't in our db ,insert into the db the query and the link opened by user
		print q		
		db.query(q)
		db.commit()
		print curr

#of = open(term, "w")
#of.write(ps.encode("utf-8"))
# of.flush()
#of.close()
#request.add_header("User-Agent", header)



import urllib, re, sys, sqlite3

#links = file('sites.txt','wt')
#initializing the sql database connection, and the cursor.
conn = sqlite3.connect('sites.db')
c = conn.cursor()


#this function is recursively called to crawl the site.
def webCrawl(url, depth):
	if depth>10:
		print ("Reached maximum depth here, trying elsewhere \n")
	elif (lambda x: x=="ico" or x=="png" or x=="jpg" or x=="ttf" or x=="css")(url.split(".")[-1]):
		print ("Found a waste of time. Skipping Reason:1")
	elif (lambda x: x=="googleapis" or x=="youtube" or x=="gstatic" or x=="google" or x=="google-analytics")(url.split(".")[1]):
		print ("Found a waste of time. Skipping Reason:2")
	else:
	#	try:
			site = urllib.urlopen(url).read()
			for link in re.findall('''href=["'](.[^"']+)["']''', site, re.I):
				if(link[0]=="/"):
					#gotta do something to handle the different cases of / use here
					link = (url+link)
				print (link)
#				links.write(link+'\n')
#This is where I'm testing using an sqlite3 database to check redundancy
				c.execute("SELECT * FROM sites;")
				flag = 0
				for row in c:
					if(row[0]==link):
						flag = 1
						print ("Found a repeated page")
				if(flag!=1):
					webCrawl(link, depth+1)
					c.execute("INSERT INTO sites VALUES ('%s', 1);" % link)
					print ("I just inserted %s into the table" % link)
	#	except:
	#		print ("You dun goofed")

if __name__=="__main__":
	from sys import argv
	if len(argv)<=1:
		print ("Usage: python2 scrape.py <site to start>")
		sys.exit()
	else:
		print ("Beginning scrape from %s" % argv[1])
		depth=1
		webCrawl(argv[1], depth)






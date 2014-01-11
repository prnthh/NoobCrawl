import urllib, re, sys

links = file('sites.txt','wt')

def webCrawl(url, depth):
	if depth>10:
		print ("Reached maximum depth here, trying elsewhere \n")
	elif (lambda x: x=="ico" or x=="png" or x=="jpg" or x=="ttf" or x=="css")(url.split(".")[-1]):
		print ("Found a waste of time. Skipping Reason:1")
	elif (lambda x: x=="googleapis" or x=="youtube" or x=="gstatic" or x=="google" or x=="google-analytics")(url.split(".")[1]):
		print ("Found a waste of time. Skipping Reason:2")
	else:
		try:
			site = urllib.urlopen(url).read()
			for link in re.findall('''href=["'](.[^"']+)["']''', site, re.I):
				if(link[0]=="/"):
					link = (url+link)
				print (link)
				links.write(link+'\n')
				webCrawl(link, depth+1)
		except:
			print ("You dun goofed")

if __name__=="__main__":
	from sys import argv
	if len(argv)<=1:
		print ("Usage: python2 scrape.py <site to start>")
		sys.exit()
	else:
		print ("Beginning scrape from %s" % argv[1])
		depth=1
		webCrawl(argv[1], depth)






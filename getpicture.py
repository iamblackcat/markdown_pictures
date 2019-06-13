#-*-coding : utf-8-*-

import requests
import sys
import time

print(sys.argv[1])

def getPicture(url):
	i = 0
	imghtml = requests.get(url)
	with open("%d.%s" %(time.time(),url[-3:]),'wb') as f:
		f.write(imghtml.content)
		f.close
		i += 1


url = sys.argv[1]
getPicture(url)

#-*-coding : utf-8-*-

import requests
import pyperclip
import sys

#print(sys.argv[1])
current_time = time.time()

def getPicture(url):
	i = 0
	imghtml = requests.get(url)
	with open("%d.%s" %(current_time,url[-3:]),'wb') as f:
		f.write(imghtml.content)
		f.close
		i += 1

"""def addToClipboard( string ):
			from tkinter import Tk
			r = Tk()
			r.withdraw()
			r.clipboard_clear()
			r.clipboard_append(string)
			r.update()
			r.destroy()
		"""		


url = sys.argv[1]
getPicture(url)
address = "https://raw.githubusercontent.com/iamblackcat/markdown_pictures/master/%d.%s" % (current_time,url[-3:])	
pyperclip.copy(address)

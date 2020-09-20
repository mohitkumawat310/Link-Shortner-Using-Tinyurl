import pyshorteners

usrlink = input("Please Enter Your Link : \n")

shortner = pyshorteners.Shortener()
shorturl = shortner.tinyurl.short(usrlink)
print("Your Shortn URL is : ",shorturl)

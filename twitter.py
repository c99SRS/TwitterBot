import sys,time,tweepy

textfile= str(sys,srgv[1])
con = key 
consumer = secret key
acces  = key
access secret = secret 


auth = tweepy.OAuthHandler(cons,consumer)
auth.set_access_token(Access,Access)
appi = tweepy.Api(auth)

file = open(textfile,"r")
f = file.readLines()
file.close()

for line in f:
    api.update_status(line)
time.sleep(5000)
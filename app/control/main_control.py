__author__ = 'pointschan'

from sys import argv
import os

script, env = argv

file_location =  "/home/vagrant/workspaces/projects/app/docs/"
stagingUrlFileName = "staging_url.txt"
ftUrlFileName = "ft_url.txt"
urlList = []


#Open and read a file line by line and append each line into urlList
def getUrlfile(filename):
    tmpUrlList = []
    try:
        f = open(os.path.join(file_location, filename))
    except IOError:
        print "%s file not found" % filename
    else:
        for line in f:
            tmpUrlList.append(line.rstrip('\n'))
        f.close()
        return tmpUrlList

#Split the each member (each line from file) and put them in "action" and "url", print the line
def processUrl():
    while urlList:
        x = urlList.pop()
        action, url = x.split(',', 1)
        print action + ' ' + url

if env=="staging":
    urlList = getUrlfile(stagingUrlFileName)
elif env=="ft":
    urlList = getUrlfile(ftUrlFileName)
else:
    print ("%s is not a valid environment") % env

print "Url list from file: "+str(urlList)

if urlList:
    processUrl()



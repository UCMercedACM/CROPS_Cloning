#This file contains functions to parse input files, like a list of CROPS sites,
#or a credentials file.

#Given a list of CROPS URLs (as copied directly from CROPS)
def parseURLlist(filename):
  urlfile = open(urlfilename,"r")

  #List of sites that we will be connecting to
  sites = urlfile.readlines()

  #Easywebdav has some idiosyncrasies: in particular, when we connect to a URL
  #like "https://ucmcrops.ucmerced.edu/dav/201430-35200-MATH-101-01", the "URL"
  #part easywebdav is https://ucmcrops.ucmerced.edu, and the "directory" part is
  #the rest of the URL. The next block of code partitions the URL list into two
  #sections: the directories (dirs) and the url prefix we will use to connect
  #to CROPS. Sorry for the long comment...

  dirs = []
  cropsprefix = re.split("dav",sites[0],maxsplit=1)[0]

  for site in sites:
    #re.split will drop "dav" from the name, manually reintroduce it to dirname
    dirname = ("dav" + re.split("dav",site,maxsplit=1)[1])
    dirname.rstrip() #kill any whitespace incl. line break
    dirs.append(dirname)

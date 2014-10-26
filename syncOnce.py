# Functions to sync CROPS to your computer one time only.

import easywebdav
import re           #I hate regular expressions :(

username = "ksong8"
password = "Nope. Not putting that up here."

#URLfile is assumed to be a text file with the URLs of the CROPS sites
#listed one per line, no repeats or other lines
urlfilename = "sites.txt"

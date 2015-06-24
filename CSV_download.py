#-------------------------------------------------------------------------------
# Name:     Alberta Wildfire
# Purpose:  Display wildfire locations
#
# Author:      rasagwara
#
# Created:     28/05/2015
# Copyright:   (c) rasagwara 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.path.append(r'C:/modules')
import csv
import urlparse
import urllib2
import os
from bs4 import BeautifulSoup


url = 'http://wildfire.alberta.ca/wildfire-status/default.aspx'
url1 = 'http://wildfire.alberta.ca'
save_output = r'C:\csv_download_test'

u = urllib2.urlopen(url)
soup = BeautifulSoup(u.read(), )
print soup

try:
    for links in soup.find_all('a', 'msExcel'):
        url2 = links.get('href')
        fullPath = urlparse.urljoin(url, url2)
        print fullPath
        print url2
        print os.path.basename(url2)
        with open(os.path.join(save_output, os.path.basename(url2)), 'wb') as f:
            a = urllib2.urlopen(fullPath)
            f.write(a.read())
            f.close()
            print 'done'

except:
    print 'failed'
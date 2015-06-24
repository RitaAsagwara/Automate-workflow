#-------------------------------------------------------------------------------
# Name:     CNSOPB Data Download
# Purpose:  Download Excel data
#
# Author:      rasagwara
#
# Created:     28/05/2015
# Copyright:   (c) rasagwara 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.path.append(r'C:/modules')
import urllib2
import urllib
import os
from bs4 import BeautifulSoup


url = 'http://www.cnsopb.ns.ca/lands-management/maps-coordinates'                  # --- Page with excel files to download
main_url = 'http://www.cnsopb.ns.ca'                                               # --- main url linke CNSOPB webpage
save_output = r'C:\csv_download_test\excel'                                        # --- change output location
download_link = []

# Scrape through the url
request = urllib2.urlopen(url)
soup = BeautifulSoup(request.read(), )

# Find all xls and xlsx files using wildcard (.+xls.*)
for links in soup.find_all('a', {'href': re.compile(r'.+xls.*')}):
        link = links.get('href')
        fullPath = urlparse.urljoin(main_url, link)                                 # --- Create excel full path using cnsopb main url link and the basename of the excel files you are downloading
        print "Fullpath: ", fullPath
        print "Basepath: ", os.path.basename(link)
        # save all excel files with orginal basename to output folder
        with open(os.path.join(save_output, os.path.basename(link)), 'wb') as f:
            a = urllib2.urlopen(fullPath)
            f.write(a.read())
            f.close()
            print 'Success!!!!!!!!!!!!!!!!!!!!!!!'





#-------------------------------------------------------------------------------
# Name:     DECC UK Oil & Gas Download
# Purpose:  Download Shapefile/zip files from DECC website
#
# Author:      rasagwara
#
# Created:     08/06/2015
# Copyright:   (c) rasagwara 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import modules
import sys
sys.path.append(r'I:\WM_presentation\modules')
from bs4 import BeautifulSoup
import urllib2
import urlparse
import zipfile
import re
import os

# variables
input_list = [
                {'input_directory': r'I:\WM_presentation\DECC_demo\Data\DECC_OFF_Hydrocarbon_Fields.zip',
                'zip_save_directory': r'I:\WM_presentation\DECC_demo\Data',
                'output_directory': r'I:\WM_presentation\DECC_demo\Data\Unzip'
                }]

# Function to unzip zipped folder
def unzip(input_directory, output_directory):

    # open up folder and read
    fh = open(input_directory, 'rb')
    z = zipfile.ZipFile(fh)
    # Loop through folder content
    for name in z.namelist():
        z.extract(name, output_directory)
    fh.close()

    print 'Folder unzipped succesfully'

# Function to extract shapefile data off of a website
def main():

    # DECC UK Oil and gas offshore data site
    url = 'https://www.gov.uk/oil-and-gas-offshore-maps-and-gis-shapefiles'
    zip_file = r'I:\WM_presentation\DECC_demo\Data'
    download_link = []

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    # loop through input list
    for input in input_list:
        input_directory = input['input_directory']
        zip_save_directory = input['zip_save_directory']
        output_directory = input['output_directory']


    # finds all .zip file in a page -- output list of zips
    for links in soup.findAll('a', {'href': re.compile(r'\DECC_OFF_Hydrocarbon_Fields.zip')}):
        download_link.append(links.get('href'))
    print 'done'

    # Saves zip list in folder and assign names to each zipfile

    for i in download_link:
        print i
        req = urllib2.Request(i)
        res = urllib2.urlopen(req)
        print res
        with open(os.path.join(zip_save_directory, os.path.basename(i)), 'wb') as f:
            f.write(res.read())
            print 'Done'

    print "Success!!!!"


    print ('Start unzip...')
    print unzip(input_directory, output_directory)
    print ('Done unzip')

    print ('Script completed')

if __name__ == '__main__':
    main()
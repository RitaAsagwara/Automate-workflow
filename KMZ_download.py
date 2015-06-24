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
import urllib2
from urllib2 import Request
import os
import subprocess
from subprocess import call

url = 'http://wildfire.alberta.ca/apps/wildfirestatusmap/status-map-handler.ashx?type=map'
kmz_file = r'C:\csv_download_test\wildfire.kmz'
json_file = r'C:\csv_download_test\wildfire.geojson'

req = urllib2.Request(url)
res = urllib2.urlopen(req)
print "donwloading : " + url

##Open our localfile
localFile = open(kmz_file, 'wb')
print localFile

##Write to Local file
localFile.write(res.read())
localFile.close()
print "Download Completed"

##ogr2
os.chdir(r'C:\Applications\release-1500-gdal-1-10-1-mapserver-6-4-0\bin\gdal\apps')
print "done"
os.system(r'C:\Applications\release-1500-gdal-1-10-1-mapserver-6-4-0\bin\gdal\apps\ogr2ogr.exe')
print"done"
os.startfile(r'C:\Applications\release-1500-gdal-1-10-1-mapserver-6-4-0\bin\gdal\apps\ogr2ogr.exe')
##print "done"
subprocess.call('C:\Applications\release-1500-gdal-1-10-1-mapserver-6-4-0\bin\gdal\apps\ogr2ogr.exe -f "GeoJSON" json_file  kmz_file')
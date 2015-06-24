#-------------------------------------------------------------------------------
# Name:     List and convert
# Purpose:  List layer files in folder and convert to shapefile
#
# Author:      rasagwara
#
# Created:     28/05/2015
# Copyright:   (c) rasagwara 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import system modules
import os, sys
import os.path
import arcpy
from arcpy import env

# variables
input_list = [
                {'input_directory': r'C:\csv_download_test\Lyr',
                 'input_filename': item,
                 'output_directory': r'C:\csv_download_test\Python',
                 'field_name': new_name
                 }

#Environment setting
arcpy.env.overwriteoutput = True

def main():

    dirs = os.listdir(input_directory)

    for item in dirs:
        item_full_path = os.path.join(input_directory, item)
        split_items = item.split('.')
        layer_name = split_items[0]
        ext = '.shp'
        new_name = ''.join([layer_name, ext])
        print new_name
        completePath = os.path.join(output_directory, new_name)
        print completePath
        arcpy.CopyFeatures_management(item_full_path, completePath)

        print "done"


if __name__ == '__main__':
    main()
